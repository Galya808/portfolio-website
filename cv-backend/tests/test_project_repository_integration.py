import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import models, schemas
from app.database import Base
from app.repositories.project_repository import SQLAlchemyProjectRepository


@pytest.fixture
def db_session():
    # Setup
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

    testing_session = sessionmaker(bind=engine)
    session = testing_session()

    try: 
        yield session
    finally:
        # Teardown
        session.close()
        Base.metadata.drop_all(engine)
        engine.dispose()


def test_create_project_persists_in_database(db_session):
    # Arrange
    repo = SQLAlchemyProjectRepository(db_session)
    project = schemas.ProjectCreate(
        title="Portfolio", 
        description="Personal Website",
    )

    # Act
    created_project = repo.create_project(project)
    stored_project = db_session.query(models.Project).one()

    # Assert
    assert stored_project.id == created_project.id
    assert stored_project.title == "Portfolio"
    assert stored_project.description == "Personal Website"


def test_get_projects_from_database(db_session):
    # Arrange
    repo = SQLAlchemyProjectRepository(db_session)
    repo.create_project(
        schemas.ProjectCreate(title="Portfolio")
    )
    repo.create_project(
        schemas.ProjectCreate(title="Website")
    )

    # Act
    projects = repo.get_projects()

    # Assert
    assert len(projects) == 2
    assert {project.title for project in projects} == {
        "Portfolio",
        "Website",
    }
