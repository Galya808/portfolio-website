from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas
from app.dependencies import get_db, get_current_user
from app.services import project_service

router = APIRouter(prefix="/projects", tags=["Projects"])
# accepts HTTP request

@router.post("/")
def create_project(
    project: schemas.ProjectCreate, 
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    return project_service.create_project(db, project)


@router.delete("/{project_id}")
def delete_project(
    project_id: int, 
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    return project_service.delete_project(db, project_id)
    

@router.get("/")
def get_projects(db: Session = Depends(get_db)):
    return project_service.get_projects(db)