from pathlib import Path
import unittest


class ProjectsCacheHeaderTest(unittest.TestCase):
    def test_projects_endpoint_sets_cache_control_header(self) -> None:
        server_code = Path(
            "services/portfolio-api/src/portfolio_api/adapters/http/server.py"
        ).read_text(encoding="utf-8")
        self.assertIn("Cache-Control", server_code)
        self.assertIn("max-age=120", server_code)


if __name__ == "__main__":
    unittest.main()
