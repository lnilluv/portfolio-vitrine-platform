from pathlib import Path
import unittest


class DeployWorkflowRoutesTest(unittest.TestCase):
    def test_deploy_workflow_recreates_proxy_and_checks_public_routes(self) -> None:
        workflow = Path(
            ".github/workflows/deploy-production.yml"
        ).read_text(encoding="utf-8")
        self.assertIn("--force-recreate proxy", workflow)
        self.assertIn(
            "curl -skf --resolve nilluv.com:443:127.0.0.1 https://nilluv.com",
            workflow,
        )
        self.assertIn(
            "curl -skf --resolve api.nilluv.com:443:127.0.0.1 https://api.nilluv.com/healthz",
            workflow,
        )


if __name__ == "__main__":
    unittest.main()
