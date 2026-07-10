from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import schemas
from app.repositories import project_repository


def create_project(db: Session, project: schemas.ProjectCreate):
    if not project.title.strip():
        raise HTTPException(status_code=400, detail="Project title is required")

    return project_repository.create_project(db, project)


def get_projects(db: Session):
    return project_repository.get_projects(db)


def delete_project(db: Session, project_id: int):
    deleted = project_repository.delete_project(db, project_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Project not found")

    return {"message": "Project deleted"}
