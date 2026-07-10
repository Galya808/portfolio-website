from sqlalchemy.orm import Session
from app import models, schemas


def create_skill(db: Session, skill: schemas.SkillCreate):
    db_skill = models.Skill(**skill.model_dump())
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill


def get_skills(db: Session):
    return db.query(models.Skill).all()
