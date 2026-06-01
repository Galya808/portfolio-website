from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db

router = APIRouter(prefix="/skills", tags=["Skills"])

@router.post("/")
def create_skill(skill: schemas.SkillCreate, db: Session = Depends(get_db)):
    return crud.create_skill(db, skill)

@router.get("/")
def get_skills(db: Session = Depends(get_db)):
    return crud.get_skills(db)
