from sqlalchemy.orm import Session
from app import models, schemas


def create_education(db: Session, education: schemas.EducationCreate):
    db_education = models.Education(**education.model_dump())
    db.add(db_education)
    db.commit()
    db.refresh(db_education)
    return db_education


def get_education(db: Session):
    return db.query(models.Education).all()
