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


def get_skill(db: Session, skill_id: int):
    return db.query(models.Skill).filter(models.Skill.id == skill_id).first()


def update_skill(
    db: Session,
    db_skill: models.Skill,
    skill: schemas.SkillUpdate,
):
    for field, value in skill.model_dump(exclude_unset=True).items():
        setattr(db_skill, field, value)

    db.commit()
    db.refresh(db_skill)
    return db_skill
