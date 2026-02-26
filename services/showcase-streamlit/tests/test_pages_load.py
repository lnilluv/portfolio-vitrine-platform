from pathlib import Path
import unittest


class ShowcasePagesTest(unittest.TestCase):
    def test_showcase_has_multiple_pages(self) -> None:
        pages_dir = Path("services/showcase-streamlit/pages")
        self.assertTrue(pages_dir.exists())
        self.assertGreaterEqual(len(list(pages_dir.glob("*.py"))), 3)


if __name__ == "__main__":
    unittest.main()
