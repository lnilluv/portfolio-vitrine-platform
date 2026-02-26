from pathlib import Path
import unittest


class RunbooksExistTest(unittest.TestCase):
    def test_runbooks_present(self) -> None:
        self.assertTrue(Path("docs/ops/deploy-runbook.md").exists())
        self.assertTrue(Path("docs/ops/rollback-runbook.md").exists())


if __name__ == "__main__":
    unittest.main()
