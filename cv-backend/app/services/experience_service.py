from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import schemas
from app.repositories import experience_repository


def create_experience(db: Session, experience: schemas.ExperienceCreate):
    if experience.company_name is not None and not experience.company_name.strip():
        raise HTTPException(status_code=400, detail="Company name cannot be empty")

    if experience.end_date and experience.start_date > experience.end_date:
        raise HTTPException(status_code=400, detail="Start date cannot be after end date")

    return experience_repository.create_experience(db, experience)


def get_experience(db: Session):
    return experience_repository.get_experience(db)


def delete_experience(db: Session, exp_id: int):
    deleted = experience_repository.delete_experience(db, exp_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Experience not found")

    return {"message": "Experience deleted"}
