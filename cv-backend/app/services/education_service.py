from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import schemas
from app.repositories import education_repository


def create_education(db: Session, education: schemas.EducationCreate):
    if not education.institution.strip():
        raise HTTPException(status_code=400, detail="Institution is required")

    if education.end_year and education.start_year > education.end_year:
        raise HTTPException(status_code=400, detail="Start year cannot be after end year")

    return education_repository.create_education(db, education)


def get_education(db: Session):
    return education_repository.get_education(db)
