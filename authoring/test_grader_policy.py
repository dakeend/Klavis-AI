"""Author-side regression tests for the verifier's fail-closed boundary."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

GRADER = Path(__file__).parents[1] / "tasks/prefect-monitor/tests/grade.py"


class PolicyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("grade", GRADER)
        cls.grade = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.grade)

    def test_normal_production_patch(self):
        self.grade.validate_patch(b"diff --git a/src/prefect/server/a.py b/src/prefect/server/a.py\n--- a/src/prefect/server/a.py\n+++ b/src/prefect/server/a.py\n@@ -1 +1 @@\n-x\n+y\n")

    def test_readonly_source_keeps_executable_helpers(self):
        self.assertEqual(self.grade.immutable_mode(0o100755), 0o755)
        self.assertEqual(self.grade.immutable_mode(0o100644), 0o644)
        self.assertEqual(self.grade.immutable_mode(0o100777), 0o755)

    def test_forbidden_patch_headers(self):
        for path in ["tests/conftest.py", "../escape", "/etc/passwd", "src/prefect/../../etc/a", "src/prefect/a\\b.py"]:
            with self.subTest(path=path), self.assertRaises(ValueError):
                self.grade.validate_patch(f"diff --git a/{path} b/{path}\n--- a/{path}\n+++ b/{path}\n@@ -1 +1 @@\n-x\n+y\n".encode())

    def test_symlink_or_rename_or_binary_rejected(self):
        for header in ["new file mode 120000", "rename to tests/conftest.py", "GIT binary patch"]:
            with self.subTest(header=header), self.assertRaises(ValueError):
                self.grade.validate_patch(("diff --git a/src/prefect/a.py b/src/prefect/a.py\n" + header + "\n").encode())

    def test_no_tests_or_partial_report_cannot_pass(self):
        for count in [0, 1, 39, 41]:
            with tempfile.TemporaryDirectory() as d:
                p = Path(d) / "report.xml"
                p.write_text(f'<testsuites><testsuite tests="{count}" errors="0" failures="0" skipped="0"/></testsuites>')
                self.assertFalse(self.grade.report_passed(p, 0, 40))

    def test_failure_skip_crash_and_missing_report_cannot_pass(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "report.xml"
            self.assertFalse(self.grade.report_passed(p, 0, 40))
            for field in ["errors", "failures", "skipped"]:
                p.write_text(f'<testsuites><testsuite tests="40" errors="0" failures="0" skipped="0"><testcase><{field[:-1]}/></testcase></testsuite></testsuites>')
                self.assertFalse(self.grade.report_passed(p, 0, 40))
            cases = ''.join('<testcase name="t%d"/>' % n for n in range(40))
            p.write_text('<testsuites><testsuite tests="40" errors="0" failures="0" skipped="0">' + cases + '</testsuite></testsuites>')
            self.assertFalse(self.grade.report_passed(p, 1, 40))
            self.assertTrue(self.grade.report_passed(p, 0, 40))


if __name__ == "__main__":
    unittest.main()
