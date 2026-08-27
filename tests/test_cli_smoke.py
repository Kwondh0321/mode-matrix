import subprocess
import sys
import unittest
from pathlib import Path


class CliSmokeTest(unittest.TestCase):
    def test_help_exits_successfully(self):
        script = Path(__file__).resolve().parents[1] / "mode_matrix.py"
        result = subprocess.run(
            [sys.executable, str(script), "--help"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("usage:", result.stdout.lower())


if __name__ == "__main__":
    unittest.main()
