"""Verify published exploratory evidence without re-running models or trusting reports as new trials."""
from collections import Counter
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


def main():
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


if __name__ == '__main__':
    main()
