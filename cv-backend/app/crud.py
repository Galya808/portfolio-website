from sqlalchemy.orm import Session
from app import models, schemas

# This is the part where the API actually talks to the database

def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(**project.dict())
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

    if project:
        db.delete(project)
        db.commit()

    return {"message": "Project deleted"}



def create_skill(db: Session, skill: schemas.SkillCreate):
    db_skill = models.Skill(**skill.dict())
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill

def get_skills(db: Session):
    return db.query(models.Skill).all()



def create_experience(db: Session, experience: schemas.ExperienceCreate):
    db_experience = models.Experience(**experience.dict())
    db.add(db_experience)
    db.commit()
    db.refresh(db_experience)
    return db_experience

def get_experience(db: Session):
    return db.query(models.Experience).all()

def delete_experience(db: Session, exp_id: int):
    exp = db.query(models.Experience).filter(
        models.Experience.id == exp_id
    ).first()

    if exp:
        db.delete(exp)
        db.commit()

    return {"message": "Experience deleted"}



def create_education(db: Session, education: schemas.EducationCreate):
    db_education = models.Education(**education.dict())
    db.add(db_education)
    db.commit()
    db.refresh(db_education)
    return db_education

def get_education(db: Session):
    return db.query(models.Education).all()



def create_user(db: Session, user: schemas.UserCreate, hashed_password: str):
    db_user = models.User(
        username=user.username, 
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()