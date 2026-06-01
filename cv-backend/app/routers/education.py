from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db

router = APIRouter(prefix="/education", tags=["Education"])

@router.post("/")
def create_education(education: schemas.EducationCreate, db: Session = Depends(get_db)):
    return crud.create_education(db, education)

@router.get("/")
def get_education(db: Session = Depends(get_db)):
    return crud.get_education(db)
