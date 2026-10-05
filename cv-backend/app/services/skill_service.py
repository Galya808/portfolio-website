from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import schemas
from app.repositories import skill_repository


def create_skill(db: Session, skill: schemas.SkillCreate):
    if not skill.name.strip():
        raise HTTPException(status_code=400, detail="Skill name is required")

    return skill_repository.create_skill(db, skill)


def get_skills(db: Session):
    return skill_repository.get_skills(db)


def update_skill(db: Session, skill_id: int, skill: schemas.SkillUpdate):
    db_skill = skill_repository.get_skill(db, skill_id)
    if db_skill is None:
        raise HTTPException(status_code=404, detail="Skill not found")

    if skill.name is not None and not skill.name.strip():
        raise HTTPException(status_code=400, detail="Skill name is required")

    return skill_repository.update_skill(db, db_skill, skill)
