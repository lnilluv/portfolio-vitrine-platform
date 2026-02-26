from pathlib import Path
import unittest


class ComposeProfilesTest(unittest.TestCase):
    def test_compose_profile_files_exist(self) -> None:
        self.assertTrue(Path("docker-compose.demos.yml").exists())
        self.assertTrue(Path("docker-compose.heavy.yml").exists())


if __name__ == "__main__":
    unittest.main()
