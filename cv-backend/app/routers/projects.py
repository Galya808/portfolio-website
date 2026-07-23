from fastapi import APIRouter, Depends, HTTPException, status

from app import schemas
from app.dependencies import (
    get_current_user,
    get_project_service,
    get_sorted_project_service,
)
from app.services import project_service
from app.services.project_service import ProjectService


router = APIRouter(prefix="/projects", tags=["Projects"])
# accepts HTTP request


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_project(
    project: schemas.ProjectCreate, 
    service: ProjectService = Depends(get_project_service),
    user: str = Depends(get_current_user)
):
    try:
        return service.create_project(project)
    except project_service.ProjectValidationError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        ) from error
    

@router.get("/")
def get_projects(
    service: ProjectService = Depends(get_sorted_project_service)
):
    return service.get_projects()


@router.delete("/{project_id}")
def delete_project(
    project_id: int, 
    service: ProjectService = Depends(get_project_service),
    user: str = Depends(get_current_user)
):
    try:
        service.delete_project(project_id)
        return {"message": "Project deleted"}
    except project_service.ProjectNotFoundError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        ) from error