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
