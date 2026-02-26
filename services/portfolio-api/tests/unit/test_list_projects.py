import unittest

from portfolio_api.application.use_cases import ListProjectsUseCase
from portfolio_api.adapters.repositories.in_memory_repo import InMemoryProjectRepository


class ListProjectsUseCaseTest(unittest.TestCase):
    def test_list_projects_returns_entries(self) -> None:
        repo = InMemoryProjectRepository()
        use_case = ListProjectsUseCase(repo)
        projects = use_case.execute()

        self.assertIsInstance(projects, list)
        self.assertGreaterEqual(len(projects), 8)


if __name__ == "__main__":
    unittest.main()
