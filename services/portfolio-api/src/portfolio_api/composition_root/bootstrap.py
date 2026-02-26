from portfolio_api.adapters.repositories.in_memory_repo import InMemoryProjectRepository
from portfolio_api.application.use_cases import ListProjectsUseCase


def build_list_projects_use_case() -> ListProjectsUseCase:
    return ListProjectsUseCase(InMemoryProjectRepository())
