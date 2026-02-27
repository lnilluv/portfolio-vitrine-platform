from pathlib import Path
import unittest


class ComposeLimitsTest(unittest.TestCase):
    def test_always_on_services_define_limits(self) -> None:
        base = Path("docker-compose.base.yml").read_text(encoding="utf-8")
        demos = Path("docker-compose.demos.yml").read_text(encoding="utf-8")
        projects = Path("docker-compose.projects.yml").read_text(encoding="utf-8")

        for token in ("proxy", "portfolio-api", "portfolio-web"):
            self.assertIn(token, base)
        for token in ("showcase-streamlit", "nlp-spam-api"):
            self.assertIn(token, demos)
        for token in ("brainsight", "getaround", "fraudstream"):
            self.assertIn(token, projects)

        self.assertIn("mem_limit", base)
        self.assertIn("cpus", base)
        self.assertIn("mem_limit", demos)
        self.assertIn("cpus", demos)
        self.assertIn("mem_limit", projects)
        self.assertIn("cpus", projects)
        self.assertTrue(Path("docs/ops/resource-budget.md").exists())


if __name__ == "__main__":
    unittest.main()
