from app.strategies.project_sort_strategy import (
    SortProjectsByTitleAscending,
    SortProjectsByTitleDescending,
    ProjectTitleAdapter,
)
from types import SimpleNamespace


def test_sort_projects_by_title_ascending():
    # Arrange
    projects = [
        {"title": "Zoo"},
        {"title": "alpha"},
        {"title": "Blog"}
    ]
    strategy = SortProjectsByTitleAscending()

    # Act
    result = strategy.sort(projects)

    # Assert
    assert [project["title"] for project in result] == [
        "alpha",
        "Blog",
        "Zoo"
    ]
    assert len(result) == 3


def test_sort_projects_by_title_descending():
    # Arrange
    projects = [
        {"title": "Zoo"},
        {"title": "alpha"},
        {"title": "Blog"}
    ]
    strategy = SortProjectsByTitleDescending()

    # Act
    result = strategy.sort(projects)

    # Assert
    assert [project["title"] for project in result] == [
        "Zoo",
        "Blog",
        "alpha"
    ]
    assert len(result) == 3


def test_sort_projects_with_object_attributes():
    # Arrange
    projects = [
        SimpleNamespace(title="Zoo"),
        SimpleNamespace(title="alpha"),
        SimpleNamespace(title="Blog"),
    ]

    strategy = SortProjectsByTitleAscending()

    # Act
    result = strategy.sort(projects)

    # Assert
    assert [project.title for project in result] == [
        "alpha",
        "Blog",
        "Zoo",
    ]


def test_project_title_adapter_with_dict():
    # Arrange
    project = {
        "title": "Portfolio"
    }

    # Act
    adapter = ProjectTitleAdapter(project)

    # Assert
    assert adapter.title == "Portfolio"


def test_project_title_adapter_with_object():
    # Arrange
    project = SimpleNamespace(title="Portfolio")

    # Act
    adapter = ProjectTitleAdapter(project)

    # Assert
    assert adapter.title == "Portfolio"