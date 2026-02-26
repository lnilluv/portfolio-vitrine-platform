import json
from pathlib import Path
import unittest


class ProjectsSchemaTest(unittest.TestCase):
    def test_runtime_mode_is_supported(self) -> None:
        data = json.loads(Path("data/projects/projects.json").read_text(encoding="utf-8"))
        allowed = {"live-interactive", "artifacts-interactive", "static-case-study"}
        for row in data:
            self.assertIn(row["runtime_mode"], allowed)
            self.assertIsInstance(row.get("skills"), list)


if __name__ == "__main__":
    unittest.main()
