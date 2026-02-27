from pathlib import Path
import unittest


class ComposeProfilesTest(unittest.TestCase):
    def test_compose_profile_files_exist(self) -> None:
        self.assertTrue(Path("docker-compose.demos.yml").exists())
        self.assertTrue(Path("docker-compose.heavy.yml").exists())
        self.assertTrue(Path("docker-compose.projects.yml").exists())

    def test_heavy_profile_overrides_real_project_services(self) -> None:
        heavy = Path("docker-compose.heavy.yml").read_text(encoding="utf-8")
        self.assertIn("profiles: [\"heavy\"]", heavy)
        for token in ("brainsight", "getaround", "fraudstream"):
            self.assertIn(token + ":", heavy)
        self.assertNotIn("placeholder", heavy)


if __name__ == "__main__":
    unittest.main()
