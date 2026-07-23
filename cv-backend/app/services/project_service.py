import logging
from app import schemas
from app.repositories.project_repository import ProjectRepository
from app.strategies.project_sort_strategy import (
    SortProjectsByTitleAscending,
    ProjectSortStrategy
)


logger = logging.getLogger(__name__)

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
        normalized_title = project.title.strip()
        if not normalized_title:
            raise ProjectValidationError(
                "Project title is required"
            )

        normalized_project = project.model_copy(
            update={"title": normalized_title}
        )
        created_project = self.repo.create_project(normalized_project)

        logger.info(
            "Project created project_id=%s",
            created_project["id"],
        )

        return created_project

    def get_projects(self):
        projects = self.repo.get_projects()
        sorted_projects = self.sort_strategy.sort(projects)

        logger.info(
            "Projects listed count=%s",
            len(sorted_projects),
        )
        
        return sorted_projects

    def delete_project(self, project_id: int) -> None:
        deleted = self.repo.delete_project(project_id)
        
        if not deleted:
            logger.warning(
                "Project deletion failed: project not found project_id=%s",
                project_id
            )
            raise ProjectNotFoundError(
                f"Project with id {project_id} not found"
            )

        logger.info(
            "Project deleted project_id=%s",
            project_id
        )