from unittest.mock import Mock

from sqlalchemy.orm import Session

from app import schemas
from app import models
from app.repositories.project_repository import SQLAlchemyProjectRepository

def test_create_project_saves_refreshes_project():
    # Arrange
    db = Mock(spec=Session)
    repo = SQLAlchemyProjectRepository(db)
    project = schemas.ProjectCreate(
        title="Portfolio",
        description="My website",
    )

    # Act
    created_project = repo.create_project(project)

    # Assert state
    assert created_project.title == "Portfolio"
    assert created_project.description == "My website"
    
    # Assert interaction
    db.add.assert_called_once_with(created_project)
    db.commit.assert_called_once_with()
    db.refresh.assert_called_once_with(created_project)


def test_delete_existing_project_deletes_and_commits():
    # Arrange
    db = Mock(spec=Session)
    query = Mock()
    filtered_query = Mock()
    existing_project = models.Project(id=1, title="Portfolio")

    db.query.return_value = query
    query.filter.return_value = filtered_query
    filtered_query.first.return_value = existing_project

    repo = SQLAlchemyProjectRepository(db)

    # Act
    result = repo.delete_project(1)

    # Assert
    assert result is True
    db.query.assert_called_once_with(models.Project)
    query.filter.assert_called_once()
    filtered_query.first.assert_called_once_with()
    db.delete.assert_called_once_with(existing_project)
    db.commit.assert_called_once_with()


def test_delete_missing_project_does_not_delete_or_commit():
    # Arrange
    db = Mock(spec=Session)
    query = Mock()
    filtered_query = Mock()

    db.query.return_value = query
    query.filter.return_value = filtered_query
    filtered_query.first.return_value = None

    repo = SQLAlchemyProjectRepository(db)

    # Act
    result = repo.delete_project(999)

    # Assert
    assert result is False

    db.query.assert_called_once_with(models.Project)
    query.filter.assert_called_once()
    filtered_query.first.assert_called_once_with()

    db.delete.assert_not_called()
    db.commit.assert_not_called()