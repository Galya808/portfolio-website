from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db, get_current_user

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.post("/")
def create_project(
    project: schemas.ProjectCreate, 
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    return crud.create_project(db, project)


@router.put("/{project_id}")
def update_project(
    project_id: int, 
    project: schemas.ProjectCreate,
    db:  Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    return crud.update_project(db, project_id, project)

@router.delete("/{project_id}")
def delete_project(
    project_id: int, 
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    return crud.delete_project(db, project_id)
    

@router.get("/")
def get_projects(db: Session = Depends(get_db)):
    return crud.get_projects(db)