from sqlalchemy.orm import Session
from app import models, schemas
from typing import Protocol


class ProjectRepository(Protocol):
    def create_project(self, project: schemas.ProjectCreate):
        ...

    def get_projects(self):
        ...

    def delete_project(self, project_id: int) -> bool:
        ...


class InMemoryProjectRepository:
    def __init__(self):
        self.projects = {}
        self.next_id = 1
    
    def create_project(self, project: schemas.ProjectCreate):
        project_data = project.model_dump()
        project_data["id"] = self.next_id

        self.projects[self.next_id] = project_data
        self.next_id += 1

        return project_data

    def get_projects(self):
        return list(self.projects.values())
    
    def delete_project(self, project_id: int) -> bool:
        project = self.projects.pop(project_id, None)
        return project is not None
    
    
class SQLAlchemyProjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_project(self, project: schemas.ProjectCreate):
        db_project = models.Project(**project.model_dump())
        self.db.add(db_project)
        self.db.commit()
        self.db.refresh(db_project)
        return db_project
    
    def get_projects(self):
        return self.db.query(models.Project).all()
    
    def delete_project(self, project_id: int) -> bool:
        project = (
            self.db.query(models.Project)
            .filter(models.Project.id == project_id)
            .first()
        )

        if project is None:
            return False
        
        self.db.delete(project)
        self.db.commit()

        return True
    
