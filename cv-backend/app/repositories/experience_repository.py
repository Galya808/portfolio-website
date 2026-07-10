from sqlalchemy.orm import Session
from app import models, schemas


def create_experience(db: Session, experience: schemas.ExperienceCreate):
    db_experience = models.Experience(**experience.model_dump())
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

    if not exp:
        return False

    db.delete(exp)
    db.commit()
    return True
