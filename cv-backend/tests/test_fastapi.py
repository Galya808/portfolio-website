import pytest

from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.routers import projects
from app.repositories.project_repository import InMemoryProjectRepository
from app.services.project_service import ProjectService
from app.dependencies import (
    get_sorted_project_service,
    get_project_service,
    get_current_user,
)
from app.schemas import ProjectCreate

api_app = FastAPI()
api_app.include_router(projects.router, prefix="/api")


@pytest.fixture
def client_and_service():
    # Setup
    repo = InMemoryProjectRepository()
    service = ProjectService(repo)

    api_app.dependency_overrides[get_sorted_project_service] = lambda: service
    api_app.dependency_overrides[get_project_service] = lambda: service
    api_app.dependency_overrides[get_current_user] = lambda: "test-user"

    with TestClient(api_app) as client:
        yield client, service
    
    # Teardown
    api_app.dependency_overrides.clear()


def test_get_projects_returns_empty_list(client_and_service):
    # Arrange
    client, _ = client_and_service

    # Act
    response = client.get('/api/projects/')

    # Assert
    assert response.status_code == 200
    assert response.json() == []


def test_get_projects_returns_projects_as_json(client_and_service):
    # Arrange
    client, service = client_and_service
    service.create_project(ProjectCreate(title='Zoo'))
    service.create_project(ProjectCreate(title='alpha'))

    # Act
    response = client.get('/api/projects/')
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert len(body) == 2
    assert [project['title'] for project in body] == [
        'alpha',
        'Zoo',
    ]


def test_create_project_without_title_returns_422(client_and_service):
    # Arrange
    client, service = client_and_service

    # Act
    response = client.post("/api/projects/", json={})

    # Assert
    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == ["body", "title"]
    assert service.get_projects() == []


def test_create_project_with_blank_title_returns_400(client_and_service):
    # Arrange
    client, service = client_and_service

    # Act
    response = client.post("/api/projects/", json={"title": "   "})

    # Assert
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Project title is required"
    }
    assert service.get_projects() == []


def test_create_project_without_token_returns_401(client_and_service):
    # Arrange
    client, service = client_and_service
    api_app.dependency_overrides.pop(get_current_user)

    # Act 
    response = client.post("/api/projects/", json={"title": "Not authenticated"})

    # Assert
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Not authenticated",
    }
    assert service.get_projects() == []


def test_create_project_returns_and_stores_project(client_and_service):
    # Arrange
    client, service = client_and_service
    payload = {
        "title": "Portfolio",
        "description": "Personal Website"
    }

    # Act
    response = client.post("/api/projects/", json=payload)
    body = response.json()
    stored_projects = service.get_projects()

    # Assert
    assert response.status_code == 201

    # checking if the API moved the object correctly
    assert body["id"] == 1
    assert body["title"] == "Portfolio"
    assert body["description"] == "Personal Website"

    # checking if the object is in the repository
    assert len(stored_projects) == 1
    assert stored_projects[0]["id"] == body["id"]


def test_delete_missing_project_returns_404(client_and_service):
    # Arrange
    client, _ = client_and_service

    # Act
    response = client.delete("/api/projects/999")

    # Assert
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Project with id 999 not found",
    }


def test_delete_existing_project_returns_200_and_removes_project(client_and_service):
    # Arrange
    client, service = client_and_service
    created_project = service.create_project(
        ProjectCreate(title="Portfolio")
    )

    # Act
    response = client.delete(f"/api/projects/{created_project['id']}")

    # Assert HTTP contract
    assert response.status_code == 200
    assert response.json() == {
        "message": "Project deleted",
    }

    # Assert side effect
    assert service.get_projects() == []


def test_delete_project_without_token_returns_401_and_does_not_remove_project(client_and_service):
    # Arrange
    client, service = client_and_service
    created_project = service.create_project(
        ProjectCreate(title="Portfolio")
    )
    api_app.dependency_overrides.pop(get_current_user)

    # Act
    response = client.delete(f"/api/projects/{created_project["id"]}")

    # Assert
    assert response.status_code == 401

    assert response.json() == {
        "detail": "Not authenticated",
    }
    assert service.get_projects() == [created_project]


def test_delete_project_with_string_instead_of_id_returns_422(client_and_service):
    # Arrange
    client, service = client_and_service
    created_project = service.create_project(
        ProjectCreate(title="Portfolio")
    )
    
    # Act
    response = client.delete(f"/api/projects/{created_project["title"]}")

    # Assert
    assert response.status_code == 422
    
    assert response.json()["detail"][0]["loc"] == ["path", "project_id"]
    assert service.get_projects() == [created_project]
