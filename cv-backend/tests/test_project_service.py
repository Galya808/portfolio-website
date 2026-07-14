import pytest
from app import schemas
from app.repositories.project_repository import (
    InMemoryProjectRepository,
)
from app.services.project_service import (
    ProjectNotFoundError, 
    ProjectService,
    ProjectValidationError
)
from app.strategies.project_sort_strategy import SortProjectsByTitleDescending


def test_create_project():
    # Arrange
    repo = InMemoryProjectRepository()
    service = ProjectService(repo)

    project = schemas.ProjectCreate(
        title="Portfolio",
        description="My portfolio website"
    )

    # Act
    created_project = service.create_project(project)

    # Assert
    assert created_project["id"] == 1
    assert created_project["title"] == "Portfolio"
    assert created_project["description"] == "My portfolio website"
    assert 1 in repo.projects

def test_get_projects():
    # Arrange
    repo = InMemoryProjectRepository()
    service = ProjectService(repo)

    first_project = schemas.ProjectCreate(
        title="Portfolio"
    )

    second_project = schemas.ProjectCreate(
        title="Newspaper"
    )

    service.create_project(first_project)
    service.create_project(second_project)

    # Act
    projects = service.get_projects()

    # Assert
    assert len(projects) == 2
    assert projects[0]["title"] == "Newspaper"
    assert projects[1]["title"] == "Portfolio"

def test_cannot_create_project_without_title():
    # Arrange
    repo = InMemoryProjectRepository()
    service = ProjectService(repo)

    project = schemas.ProjectCreate(
        title="     ",
    )

    # Act + Assert
    with pytest.raises(
        ProjectValidationError,
        match="Project title is required",
    ):
        service.create_project(project)
    
    assert repo.get_projects() == []


def test_delete_existing_project():
    # Arrange
    repo = InMemoryProjectRepository()
    repo.projects[1] = {"title": "Portfolio"}

    # Act
    service = ProjectService(repo)
    service.delete_project(1)

    # Assert
    assert 1 not in repo.projects


def test_delete_not_existing_project():
    # Arrange
    repo = InMemoryProjectRepository()
    service = ProjectService(repo)

    # Act + Assert 
    with pytest.raises(ProjectNotFoundError):
        service.delete_project(999)


def test_get_projects_with_descending_sort_strategy():
    # Arrange
    repo = InMemoryProjectRepository()
    service = ProjectService(
        repo, 
        SortProjectsByTitleDescending(),
    )

    service.create_project(schemas.ProjectCreate(title="alpha"))
    service.create_project(schemas.ProjectCreate(title="Zoo"))
    service.create_project(schemas.ProjectCreate(title="Blog"))

    # Act
    projects = service.get_projects()

    # Assert
    assert [project["title"] for project in projects] == [
        "Zoo",
        "Blog",
        "alpha"
    ]