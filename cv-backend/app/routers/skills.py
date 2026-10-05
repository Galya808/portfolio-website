from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas
from app.dependencies import get_db, get_current_user
from app.services import skill_service

router = APIRouter(prefix="/skills", tags=["Skills"])

@router.post("/")
def create_skill(
    skill: schemas.SkillCreate, 
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    return skill_service.create_skill(db, skill)

@router.get("/")
def get_skills(db: Session = Depends(get_db)):
    return skill_service.get_skills(db)


@router.patch("/{skill_id}")
def update_skill(
    skill_id: int,
    skill: schemas.SkillUpdate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user),
):
    return skill_service.update_skill(db, skill_id, skill)
