import subprocess
import unittest


class HexagonalBoundariesTest(unittest.TestCase):
    def test_checker_passes(self) -> None:
        result = subprocess.run(
            ["python3", "tools/architecture/check_hexagonal_boundaries.py"],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
