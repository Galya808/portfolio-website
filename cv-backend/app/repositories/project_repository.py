from sqlalchemy.orm import Session
from app import models, schemas


def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(**project.model_dump())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def get_projects(db: Session):
    return db.query(models.Project).all()


def delete_project(db: Session, project_id: int):
    project = db.query(models.Project).filter(
        models.Project.id == project_id
    ).first()

    if not project:
        return False

    db.delete(project)
    db.commit()
    return True
