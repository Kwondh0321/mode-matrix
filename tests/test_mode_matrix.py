import os
import tempfile
import unittest
from pathlib import Path
from mode_matrix import modes

class Tests(unittest.TestCase):
    def test_regular_file_mode(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp, "x")
            path.write_text("x")
            os.chmod(path, 0o600)
            self.assertEqual(modes(tmp)["-rw-------"], 1)

if __name__ == "__main__":
    unittest.main()
