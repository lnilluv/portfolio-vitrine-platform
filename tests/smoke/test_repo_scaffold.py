from pathlib import Path
import unittest


class RepoScaffoldTest(unittest.TestCase):
    def test_platform_scaffold_exists(self) -> None:
        self.assertTrue(Path("docker-compose.base.yml").exists())


if __name__ == "__main__":
    unittest.main()
