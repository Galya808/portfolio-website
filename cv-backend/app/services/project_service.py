from app import schemas
from app.repositories.project_repository import ProjectRepository
from app.strategies.project_sort_strategy import (
    SortProjectsByTitleAscending,
    ProjectSortStrategy
)


class ProjectNotFoundError(Exception):
    pass


class ProjectValidationError(Exception):
    pass


class ProjectService:
    def __init__(
            self, 
            repo: ProjectRepository,
            sort_strategy: ProjectSortStrategy | None = None
    ):
        self.repo = repo
        self.sort_strategy = (
            sort_strategy or SortProjectsByTitleAscending()
        )

    def create_project(self, project: schemas.ProjectCreate):
        if not project.title.strip():
            raise ProjectValidationError(
                "Project title is required"
            )
        
        return self.repo.create_project(project)

    def get_projects(self):
        projects = self.repo.get_projects()
        
        return self.sort_strategy.sort(projects)

    def delete_project(self, project_id: int) -> None:
        deleted = self.repo.delete_project(project_id)
        
        if not deleted:
            raise ProjectNotFoundError(f"Project with id {project_id} not found")