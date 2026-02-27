from pathlib import Path
import unittest


class ProxyFileProviderTest(unittest.TestCase):
    def test_proxy_uses_file_provider_config(self) -> None:
        compose = Path("docker-compose.base.yml").read_text(encoding="utf-8")
        self.assertIn("--providers.file.filename=/etc/traefik/dynamic.yml", compose)
        self.assertTrue(Path("services/proxy/dynamic.yml").exists())


if __name__ == "__main__":
    unittest.main()
