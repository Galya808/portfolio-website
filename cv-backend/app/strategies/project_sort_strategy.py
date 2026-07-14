from typing import Protocol


class ProjectSortStrategy(Protocol):
    def sort(self, projects: list[dict]):
        ...


class SortProjectsByTitleAscending:
    def sort(self, projects: list[dict]):
        return sorted(
            projects, 
            key=lambda project: ProjectTitleAdapter(project).title.lower(),
        )


class SortProjectsByTitleDescending:
    def sort(self, projects: list[dict]):
        return sorted(
            projects,
            key=lambda project: ProjectTitleAdapter(project).title.lower(),
            reverse=True,
        )


class ProjectTitleAdapter:
    def __init__(self, project):
        self.project = project
    
    @property
    def title(self) -> str:
        if isinstance(self.project, dict):
            return self.project["title"]

        return self.project.title