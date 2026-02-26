from typing import Protocol, List

from portfolio_api.domain.models import ProjectCard


class ProjectRepositoryPort(Protocol):
    def list_projects(self) -> List[ProjectCard]:
        ...
