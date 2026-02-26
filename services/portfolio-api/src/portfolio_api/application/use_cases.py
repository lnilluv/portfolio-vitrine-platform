from dataclasses import asdict
from typing import List, Dict, Any

from portfolio_api.application.ports import ProjectRepositoryPort


class ListProjectsUseCase:
    def __init__(self, repository: ProjectRepositoryPort) -> None:
        self._repository = repository

    def execute(self) -> List[Dict[str, Any]]:
        return [asdict(project) for project in self._repository.list_projects()]
