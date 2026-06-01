from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db, get_current_user

router = APIRouter(prefix="/experience", tags=["Experience"])

@router.post("/")
def create_experience(experience: schemas.ExperienceCreate, db: Session = Depends(get_db)):
    return crud.create_experience(db, experience)

@router.get("/")
def get_experience(db: Session = Depends(get_db)):
    return crud.get_experience(db)

@router.delete("/{exp_id}")
def delete_experience(
    exp_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    return crud.delete_experience(db, exp_id)