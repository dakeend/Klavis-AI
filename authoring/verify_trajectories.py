"""Verify published exploratory evidence without re-running models or trusting reports as new trials."""
from collections import Counter
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tarfile
import tempfile

PACKAGE = Path(__file__).resolve().parents[1]
EVIDENCE = PACKAGE / 'reports/trajectories'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def legacy_main():
    archive_path = PACKAGE / 'tasks/prefect-monitor/environment/data/baseline.tar.gz'
    results = []
    for label in ['gpt61-sol-xhigh', 'claude-deepseek41-flash-max']:
        trial = EVIDENCE / label
        rows = [json.loads(line) for line in (trial / 'trajectory.jsonl').read_text('utf-8').splitlines()]
        assert all(r['kind'] in {'assistant_message', 'tool_call', 'tool_result'} for r in rows)
        assert [r['sequence'] for r in rows] == list(range(1, len(rows) + 1))
        calls = Counter(r['call_id'] for r in rows if r['kind'] == 'tool_call')
        returns = Counter(r['call_id'] for r in rows if r['kind'] == 'tool_result')
        assert calls == returns and all(v == 1 for v in calls.values())
        for row in rows:
            assert 'payload' not in row and 'internal_chat_message_metadata_passthrough' not in row
        audit = json.loads((trial / 'export-audit.json').read_text('utf-8'))
        assert len(rows) == audit['exported_records']
        outcome = json.loads((trial / 'evaluation/result.json').read_text('utf-8'))
        assert outcome['formal_tb3_trial'] is False
        summary = (trial / 'evaluation/behavior.log').read_text('utf-8').strip().splitlines()[-1]
        match = re.search(r'(\d+) failed, (\d+) passed', summary)
        assert match and int(match[1]) == outcome['historical_behavior_failed_raw']
        assert int(match[2]) == outcome['historical_behavior_passed'] + 1
        assert '4 passed' in (trial / 'evaluation/retry.log').read_text('utf-8').strip().splitlines()[-1]
        changed = json.loads((trial / 'candidate-files.json').read_text('utf-8'))
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory)
            with tarfile.open(archive_path) as archive:
                for member in archive:
                    if not member.name.startswith('src/prefect/'):
                        continue
                    assert not member.name.startswith('/') and '..' not in Path(member.name).parts
                    assert member.isfile() or member.isdir()
                    archive.extract(member, source)
            patch = (trial / 'candidate-production.patch').resolve()
            apply = ['git', '-c', 'core.autocrlf=false', 'apply', '--whitespace=nowarn']
            subprocess.run([*apply, '--check', str(patch)], cwd=source, check=True, capture_output=True)
            for item in changed:
                path = source / item['path']
                if item['baseline_lf_sha256'] is not None:
                    assert sha(path.read_bytes()) == item['baseline_lf_sha256']
            subprocess.run([*apply, str(patch)], cwd=source, check=True, capture_output=True)
            for item in changed:
                path = source / item['path']
                if item['candidate_lf_sha256'] is None:
                    assert not path.exists()
                else:
                    assert sha(path.read_bytes()) == item['candidate_lf_sha256'], item['path']
        results.append({'trial': label, 'visible_tool_calls': len(calls), 'paired_tool_results': len(returns),
                        'records': len(rows), 'production_files_verified': len(changed),
                        'patch_applies_to_frozen_baseline': True, 'historical_log_counts_match': True})
    report = {'passed': True, 'scope': 'Evidence integrity and patch applicability only; no new model/benchmark run', 'trials': results}
    (EVIDENCE / 'verification.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8', newline='\n')
    print(json.dumps(report, ensure_ascii=False, indent=2))


ORIGINAL_LABELS = ('gpt61-sol-xhigh', 'claude-deepseek41-flash-max')
REPEAT_LABELS = tuple(f'{family}-r{n}' for family in ORIGINAL_LABELS for n in (2, 3))
IMAGE = 'sha256:57b825c56f05b13066e8d81125a03473d098550d2bd16a0d613ba64577a4be35'
VERIFIER_FILES = (
    'grade.py', 'reliability.py', 'restart_worker.py',
    'overlay/tests/events/server/triggers/test_incident_completed_run.py',
    'overlay/tests/events/server/triggers/test_early_expect_events.py',
    'overlay/tests/events/server/triggers/test_proactive_terminal_events.py',
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(path):
    return json.loads(path.read_text('utf-8-sig'))


def safe_child(root, name):
    require(isinstance(name, str) and name and '\\' not in name and ':' not in name and
            not name.startswith('/') and all(part not in {'', '.', '..'} for part in name.split('/')),
            'Unsafe artifact path: ' + str(name))
    child = (root / name).resolve()
    require(child.is_relative_to(root.resolve()), 'Artifact escapes its root: ' + name)
    return child


def normalized(data):
    return data.replace(b'\r\n', b'\n')


def parse_pytest(text, exit_code, expected):
    """Report raw counts and execution health, without assigning semantic scores."""
    text = re.sub(r'\x1b\[[0-9;]*m', '', text)
    summaries = [line for line in text.splitlines()
                 if re.search(r'\d+ (?:passed|failed|errors?|skipped|deselected|xfailed|xpassed)', line)
                 and (re.search(r'\bin \d', line) or 'interrupted' in line.lower())]
    summary = summaries[-1] if summaries else None
    counts = {('error' if key in {'error', 'errors'} else key): int(value)
              for value, key in re.findall(r'(\d+) (passed|failed|errors?|skipped|deselected|xfailed|xpassed)', summary or '')}
    failed = re.findall(r'^FAILED\s+(\S+)', text, re.M)
    errors = re.findall(r'^ERROR\s+(\S+)', text, re.M)
    infrastructure = bool(exit_code not in (0, 1) or counts.get('error', 0) or errors or
                          re.search(r'INTERNALERROR|ImportError while loading|ModuleNotFoundError|ConnectionRefusedError|'
                                    r'database is locked|WinError 10013|ECONNREFUSED|unable to open database file', text, re.I))
    complete = (not infrastructure and summary is not None and
                counts.get('passed', 0) + counts.get('failed', 0) == expected and
                not any(counts.get(key, 0) for key in ('skipped', 'xfailed', 'xpassed')) and
                len(failed) == counts.get('failed', 0) and
                ((exit_code == 0) == (counts.get('failed', 0) == 0)))
    return dict(summary=summary, counts=counts, failed_tests=failed, error_tests=errors,
                expected_tests=expected, completed_expected_checks=complete,
                execution_classification='infrastructure_or_pytest_error' if infrastructure else
                    ('completed_test_run' if complete else 'incomplete_or_unclassified'),
                semantic_failure_count=None)


def verify_historical(trial, outcome, repeat):
    require(outcome.get('formal_tb3_trial') is False, 'Historical trial scope missing')
    require(outcome.get('complete_verifier') is False, 'Historical verifier scope missing')
    parsed = {}
    for group, expected in (('behavior', 36), ('retry', 4)):
        runs = [r for r in outcome['runs'] if r['group'] == group]
        require(len(runs) == 1, 'Missing or duplicate historical group: ' + group)
        run = runs[0]
        require(run.get('log') == group + '.log', 'Historical log path mismatch')
        text = (trial / 'evaluation' / (group + '.log')).read_text('utf-8')
        actual = parse_pytest(text, run['exit_code'], expected)
        parsed[group] = actual
        for key, value in actual.items():
            if key in run:
                require(run[key] == value, 'Historical log/result mismatch: ' + group + '/' + key)
            elif repeat:
                raise ValueError('Missing repeat evaluation field: ' + key)
        require(run.get('semantic_failure_count') is None, 'Historical raw failure reported as semantic count')
    behavior = parsed['behavior']
    replay = None
    if behavior['completed_expected_checks']:
        node = 'tests/events/server/triggers/test_incident_completed_run.py::test_completed_run_incident'
        replay = node not in behavior['failed_tests']
    require(outcome.get('public_replay_passed') is replay, 'Public replay status inconsistent with exhaustive log')
    passed = behavior['counts'].get('passed', 0) - int(replay is True) if replay is not None else None
    failed = behavior['counts'].get('failed', 0) - int(replay is False) if replay is not None else None
    require(outcome.get('historical_behavior_passed') == passed, 'Historical hidden-pass count mismatch')
    require(outcome.get('historical_behavior_failed_raw') == failed, 'Historical hidden raw-failure count mismatch')
    for key, group in (('combined_behavior_summary', 'behavior'), ('retry_summary', 'retry')):
        if key in outcome:
            require(outcome[key] == parsed[group]['summary'], 'Historical summary mismatch: ' + key)
    if 'retry_counts' in outcome:
        require(outcome['retry_counts'] == parsed['retry']['counts'], 'Historical retry count mismatch')
    if 'failed_tests' in outcome:
        require(outcome['failed_tests'] == behavior['failed_tests'], 'Historical failed nodes mismatch')
    if repeat:
        hashes = outcome['historical_evaluation_lf_sha256']
        required = {'tests/events/server/triggers/' + name for name in
                    ('test_incident_completed_run.py', 'test_early_expect_events.py',
                     'test_proactive_terminal_events.py', 'incident_completed_run.json')}
        require(set(hashes) == required, 'Historical evaluator manifest mismatch')
        for name, digest in hashes.items():
            require(sha(normalized(safe_child(EVIDENCE / 'historical-evaluation/overlay', name).read_bytes())) == digest,
                    'Historical evaluator differs from attempt 1: ' + name)
    return {group: value['execution_classification'] for group, value in parsed.items()}


def verify_patch(trial):
    manifest = read_json(trial / 'candidate-files.json')
    names = [entry['path'] for entry in manifest]
    require(len(names) == len(set(names)), 'Duplicate production manifest path')
    for name in names:
        require(name.startswith('src/prefect/'), 'Nonproduction candidate path')
    with tempfile.TemporaryDirectory() as directory:
        source = Path(directory)
        baseline = {}
        archive_path = PACKAGE / 'tasks/prefect-monitor/environment/data/baseline.tar.gz'
        with tarfile.open(archive_path) as archive:
            for member in archive:
                if not member.name.startswith('src/prefect/'):
                    continue
                require(member.isfile() or member.isdir(), 'Special baseline archive member')
                path = safe_child(source, member.name.rstrip('/'))
                if member.isfile():
                    data = normalized(archive.extractfile(member).read())
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_bytes(data)
                    baseline[member.name] = sha(data)
        expected = dict(baseline)
        for entry in manifest:
            name = entry['path']
            safe_child(source, name)
            require(entry['baseline_lf_sha256'] == baseline.get(name), 'Baseline LF hash mismatch: ' + name)
            if entry['candidate_lf_sha256'] is None:
                expected.pop(name, None)
            else:
                require(re.fullmatch('[0-9a-f]{64}', entry['candidate_lf_sha256']), 'Invalid candidate LF hash')
                expected[name] = entry['candidate_lf_sha256']
        patch = (trial / 'candidate-production.patch').resolve()
        text = patch.read_text('utf-8')
        # Git apply must not alter files outside the manifest or create special files.
        for line in text.splitlines():
            require(not line.startswith(('rename ', 'copy ', 'GIT binary patch', 'Binary files ')), 'Unsupported patch form')
            require(not re.match(r'(?:new file|deleted file|old|new) mode (?!100644$|100755$)', line), 'Special patch mode')
            if line.startswith('diff --git '):
                fields = line.split()
                require(len(fields) == 4, 'Ambiguous patch path')
                for field, prefix in zip(fields[2:], ('a/', 'b/')):
                    require(field.startswith(prefix) and field[2:] in names, 'Patch path absent from manifest')
                    safe_child(source, field[2:])
            elif line.startswith(('--- ', '+++ ')):
                name = line[4:]
                require(name == '/dev/null' or (name.startswith(('a/', 'b/')) and name[2:] in names), 'Patch header mismatch')
        if text.strip():
            apply = ['git', '-c', 'core.autocrlf=false', 'apply', '--whitespace=nowarn']
            for flags in (['--check'], []):
                process = subprocess.run([*apply, *flags, str(patch)], cwd=source, capture_output=True, text=True)
                require(process.returncode == 0, 'Patch application failed: ' + process.stderr)
        else:
            require(not manifest, 'Empty patch with nonempty manifest')
        actual = {}
        for path in source.rglob('*'):
            require(not path.is_symlink(), 'Patch created a symlink')
            if path.is_file():
                actual[path.relative_to(source).as_posix()] = sha(path.read_bytes())
        require(actual == expected, 'Applied production tree does not reproduce LF manifest hashes')
    return len(manifest)


def verify_public_trial(label):
    repeat = label in REPEAT_LABELS
    trial = EVIDENCE / ('repeats/' + label if repeat else label)
    rows = [json.loads(line) for line in (trial / 'trajectory.jsonl').read_text('utf-8').splitlines()]
    require(bool(rows), 'Empty public trajectory')
    require(all(row['kind'] in {'assistant_message', 'tool_call', 'tool_result'} for row in rows), 'Nonpublic record kind')
    require([row['sequence'] for row in rows] == list(range(1, len(rows) + 1)), 'Record sequence mismatch')
    calls = Counter(row.get('call_id') for row in rows if row['kind'] == 'tool_call')
    returns = Counter(row.get('call_id') for row in rows if row['kind'] == 'tool_result')
    require(calls == returns and all(key and count == 1 for key, count in calls.items()), 'Public tool pairing mismatch')
    for row in rows:
        require(not any(key in row for key in ('payload', 'reasoning', 'thinking', 'internal_chat_message_metadata_passthrough')),
                'Private trajectory fields')
        if repeat and row['kind'] == 'tool_call':
            require(not re.search(r'collaboration|(?:^|[._\s"\'])send_message(?:_to_thread)?\b|'
                                  r'\b(?:spawn_agent|followup_task|interrupt_agent|wait_agent|list_agents)\b',
                                  str(row.get('tool')) + ' ' + str(row.get('arguments')), re.I), 'Collaboration exported')
    audit = read_json(trial / 'export-audit.json')
    require(audit['exported_records'] == len(rows), 'Audit record count mismatch')
    require(audit['record_kinds'] == dict(Counter(row['kind'] for row in rows)), 'Audit kind count mismatch')
    hashes = audit.get('file_sha256', {})
    if repeat:
        required = {'trajectory.jsonl', 'trajectory.md', 'input-task.md', 'model-summary.md',
                    'candidate-production.patch', 'candidate-files.json', 'run-config.json',
                    'evaluation/result.json', 'evaluation/behavior.log', 'evaluation/retry.log', 'infrastructure-startups.json'}
        require(required <= set(hashes), 'Repeat audit lacks required file hashes')
        require(audit.get('normalized_prompt_matches_attempt1') is True and audit.get('source_hashes_verified') is True,
                'Repeat provenance flags missing')
        # One Claude event may yield several public content-block records.
        require(type(audit['source_records']) is int and audit['source_records'] > 0, 'Invalid source record count')
    for name, digest in hashes.items():
        require(sha(safe_child(trial, name).read_bytes()) == digest, 'Audit artifact hash mismatch: ' + name)
    config = read_json(trial / 'run-config.json')
    require(config['reasoning_exported'] is False, 'Reasoning-export scope mismatch')
    require(config['source_observed_export_sha256'] == audit['source_observed_export_sha256'], 'Action provenance hash mismatch')
    if repeat:
        require(config['attempt'] == int(label[-1]), 'Repeat attempt number mismatch')
        family = label.rsplit('-r', 1)[0]
        require(normalized((trial / 'input-task.md').read_bytes()) == normalized((EVIDENCE / family / 'input-task.md').read_bytes()),
                'Repeat normalized prompt differs from attempt 1')
        for startup in read_json(trial / 'infrastructure-startups.json'):
            require(startup['counted_as_solver_attempt'] is False and startup['tool_calls'] == 0 and
                    startup['input_tokens'] == startup['output_tokens'] == 0, 'Unsubstantiated startup exclusion')
    outcome = read_json(trial / 'evaluation/result.json')
    classifications = verify_historical(trial, outcome, repeat)
    files = verify_patch(trial)
    return dict(trial=label, visible_tool_calls=len(calls), paired_tool_results=len(returns), records=len(rows),
                production_files_verified=files, patch_applies_to_frozen_baseline=True,
                historical_log_counts_match=True, historical_execution_classifications=classifications)


def verify_current(label):
    trial = EVIDENCE / ('repeats/' + label if label in REPEAT_LABELS else label)
    folder = EVIDENCE / 'unified-evaluation' / label
    execution, details = read_json(folder / 'execution.json'), read_json(folder / 'details.json')
    results = read_json(folder / 'ctrf.json')['results']
    require(execution['label'] == label and execution['driver_exit_code'] == 0, 'Current driver failed or label mismatched')
    require(execution['patch_sha256'] == sha((trial / 'candidate-production.patch').read_bytes()), 'Current candidate patch hash mismatch')
    require((folder / 'container-image.txt').read_text('utf-8').strip() == IMAGE, 'Current immutable image mismatch')
    require(read_json(folder / 'container-network.json') == 'none', 'Current container network is enabled')
    require((folder / 'container-oom.txt').read_text('utf-8').strip().lower() == 'false', 'Current container OOM recorded')
    require(execution['model_rerun'] is False and execution['formal_harbor_trial'] is False, 'Current evaluation scope mismatch')
    require(execution['details'] == details and execution['summary'] == results['summary'], 'Current execution/report mismatch')
    tests, summary = results['tests'], results['summary']
    require(len({test['name'] for test in tests}) == len(tests), 'Duplicate current CTRF test identity')
    require(all(test['status'] in {'passed', 'failed', 'skipped', 'pending', 'other'} for test in tests), 'Unknown CTRF status')
    counts = Counter(test['status'] for test in tests)
    require(summary['tests'] == len(tests) and all(summary[key] == counts[key] for key in ('passed', 'failed', 'skipped', 'pending', 'other')),
            'Current summary does not count actual CTRF tests')
    require(summary['stop'] >= summary['start'], 'Current timing order invalid')
    reward_text = (folder / 'reward.txt').read_text('utf-8').strip()
    require(reward_text in {'0', '1'}, 'Invalid current reward')
    reward = int(reward_text)
    require(execution['reward'] == reward, 'Execution/reward mismatch')
    expected_groups = {'behavior': 36, 'retry': 4, 'compatibility': 3}
    for group, expected in expected_groups.items():
        if group not in details:
            require('error' in details, 'Missing current group without recorded error')
            continue
        detail = details[group]
        require(detail['expected_tests'] == expected and type(detail['passed']) is bool, 'Current group metadata mismatch')
        if group == 'behavior':
            cases = [t for t in tests if any('.' + name + '.' in t['name'] for name in
                     ('test_incident_completed_run', 'test_early_expect_events', 'test_proactive_terminal_events'))]
        elif group == 'retry':
            cases = [t for t in tests if '.test_core_policy.' in t['name']]
        else:
            cases = [t for t in tests if '.test_basics.' in t['name']]
        inferred_passed = detail['exit_code'] == 0 and len(cases) == expected and all(t['status'] == 'passed' for t in cases)
        require(detail['passed'] is inferred_passed, 'Current group pass status/CTRF mismatch: ' + group)
    reliability = [test for test in tests if test['name'] == 'sqlite.upgrade_and_process_restarts']
    errors = [test for test in tests if test['name'] == 'verifier.integrity_or_reliability']
    require((len(errors) == 1 and errors[0]['status'] == 'failed' and not reliability) if 'error' in details else
            (len(reliability) == 1 and reliability[0]['status'] == 'passed' and not errors), 'Current reliability/details mismatch')
    inferred_reward = int('error' not in details and all(details.get(group, {}).get('passed') is True for group in expected_groups))
    require(reward == inferred_reward, 'Current reward/details inconsistency')
    if reward:
        require(len(tests) == 44 and counts['passed'] == 44, 'Passing current reward lacks 44 passing checks')
    hashes = {}
    for line in (folder / 'verifier-sha256.txt').read_text('utf-8').splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})\s+\*?(.+)', line)
        require(match is not None, 'Malformed current verifier hash line')
        digest, name = match.groups()
        require(name not in hashes, 'Duplicate current verifier hash path')
        hashes[name] = digest
    require(set(hashes) == set(VERIFIER_FILES), 'Current verifier hash manifest must contain exactly six selected files')
    for name, digest in hashes.items():
        require(sha(safe_child(PACKAGE / 'tasks/prefect-monitor/tests', name).read_bytes()) == digest,
                'Current submitted verifier SHA-256 mismatch: ' + name)
    return dict(patch_sha256=execution['patch_sha256'], image=IMAGE, reward=reward,
                tests=summary['tests'], passed=summary['passed'], failed=summary['failed'],
                complete_44_check_report=summary['tests'] == 44,
                execution_classification='recorded_verifier_error' if 'error' in details else 'completed_verifier',
                semantic_failure_count=None, verifier_files_sha256_verified=6)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--include-repeats', action='store_true', help='Verify both originals and four repeats using submitted files only.')
    parser.add_argument('--include-current', action='store_true', help='Also verify current Docker results for all six; implies --include-repeats.')
    args = parser.parse_args()
    if not (args.include_repeats or args.include_current):
        return legacy_main()
    results = []
    for label in (*ORIGINAL_LABELS, *REPEAT_LABELS):
        try:
            result = verify_public_trial(label)
            if args.include_current:
                result['current'] = verify_current(label)
            result['verified'] = True
        except (OSError, ValueError, KeyError, TypeError, tarfile.TarError) as error:
            result = dict(trial=label, verified=False, error=str(error))
        results.append(result)
    report = dict(passed=all(r['verified'] for r in results),
                  scope='Submitted evidence integrity and patch applicability; no model or benchmark rerun; raw failures are not semantic scores.',
                  include_current=args.include_current, trials=results)
    destination = EVIDENCE / 'repeats/verification-public.json'
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(0 if report['passed'] else 1)


if __name__ == '__main__':
    main()
