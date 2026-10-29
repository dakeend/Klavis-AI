"""Synthetic tests of submitted-only optional verifier; never run publication."""
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('public_verifier', ROOT / 'verify_trajectories.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


class PublicVerifierTests(unittest.TestCase):
    def test_complete_all_pass_and_zero_pass_public_failure(self):
        passed = v.parse_pytest('36 passed in 2.00s', 0, 36)
        self.assertTrue(passed['completed_expected_checks'])
        nodes = ['tests/events/server/triggers/test_incident_completed_run.py::test_completed_run_incident'] + [f'test_{i}' for i in range(35)]
        failed = v.parse_pytest('\n'.join('FAILED ' + n + ' - AssertionError' for n in nodes) + '\n36 failed in 2.00s', 1, 36)
        self.assertTrue(failed['completed_expected_checks'])
        self.assertEqual(failed['counts'].get('passed', 0), 0)
        self.assertIsNone(failed['semantic_failure_count'])

    def test_errors_and_incomplete_reports_are_unscored(self):
        for text, code in [('4 errors in 1.00s', 1), ('ModuleNotFoundError: x', 2), ('no tests ran in 1.00s', 5)]:
            actual = v.parse_pytest(text, code, 36)
            self.assertFalse(actual['completed_expected_checks'])
            self.assertEqual(actual['execution_classification'], 'infrastructure_or_pytest_error')
            self.assertIsNone(actual['semantic_failure_count'])

    def test_current_integrity_and_tamper_rejections(self):
        with tempfile.TemporaryDirectory(dir=ROOT, prefix='synthetic-public-') as temp:
            package = Path(temp)
            evidence = package / 'reports/trajectories'
            label = v.ORIGINAL_LABELS[0]
            trial, folder = evidence / label, evidence / 'unified-evaluation' / label
            trial.mkdir(parents=True)
            folder.mkdir(parents=True)
            (trial / 'candidate-production.patch').write_bytes(b'')
            def save(name, data):
                (folder / name).write_text(json.dumps(data), encoding='utf-8')
            tests = [dict(name=f'x.test_early_expect_events.test_{i}', status='passed') for i in range(36)]
            tests += [dict(name=f'x.test_core_policy.test_{i}', status='passed') for i in range(4)]
            tests += [dict(name=f'x.test_basics.test_{i}', status='passed') for i in range(3)]
            tests += [dict(name='sqlite.upgrade_and_process_restarts', status='passed')]
            summary = dict(tests=44, passed=44, failed=0, skipped=0, pending=0, other=0, start=1, stop=2)
            details = {name: dict(expected_tests=count, exit_code=0, passed=True) for name, count in
                       [('behavior', 36), ('retry', 4), ('compatibility', 3)]}
            execution = dict(label=label, patch_sha256=v.sha(b''), driver_exit_code=0,
                             model_rerun=False, formal_harbor_trial=False, reward=1, summary=summary, details=details)
            save('execution.json', execution)
            save('details.json', details)
            save('ctrf.json', dict(results=dict(summary=summary, tests=tests)))
            save('container-network.json', 'none')
            (folder / 'container-oom.txt').write_text('false')
            (folder / 'container-image.txt').write_text(v.IMAGE)
            (folder / 'reward.txt').write_text('1')
            hashes = []
            for name in v.VERIFIER_FILES:
                path = package / 'tasks/prefect-monitor/tests' / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(name.encode())
                hashes.append(v.sha(path.read_bytes()) + '  ' + name)
            (folder / 'verifier-sha256.txt').write_text('\n'.join(hashes))
            with patch.object(v, 'PACKAGE', package), patch.object(v, 'EVIDENCE', evidence):
                self.assertEqual(v.verify_current(label)['reward'], 1)
                for name, invalid, valid in [('container-image.txt', 'wrong-image', v.IMAGE),
                                             ('reward.txt', '0', '1'), ('container-oom.txt', 'true', 'false')]:
                    (folder / name).write_text(invalid)
                    with self.assertRaises(ValueError):
                        v.verify_current(label)
                    (folder / name).write_text(valid)
                execution['patch_sha256'] = '0' * 64
                save('execution.json', execution)
                with self.assertRaises(ValueError):
                    v.verify_current(label)

    def test_unsafe_path_rejected(self):
        for name in ['../escape', '/absolute', 'src/prefect/../escape', 'C:/absolute', 'src\\escape']:
            with self.assertRaises(ValueError):
                v.safe_child(ROOT, name)


if __name__ == '__main__':
    unittest.main()
