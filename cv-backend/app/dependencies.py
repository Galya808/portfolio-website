from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from typing import Literal

from app.config import SECRET_KEY, ALGORITHM
from app.database import SessionLocal
from app.repositories.project_repository import (
    SQLAlchemyProjectRepository
)
from app.services.project_service import ProjectService
from app.strategies.project_sort_strategy import (
    SortProjectsByTitleAscending,
    SortProjectsByTitleDescending,
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

# This code allows FastAPI to automatically provide database sessions
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def get_project_service(
        db: Session=Depends(get_db)
) -> ProjectService:
    repo = SQLAlchemyProjectRepository(db)
    return ProjectService(repo)


def get_sorted_project_service(
        sort_order: Literal["asc", "desc"] = "asc",
        db: Session = Depends(get_db),
) -> ProjectService:
    if sort_order == "desc":
        strategy = SortProjectsByTitleDescending()
    else:
        strategy = SortProjectsByTitleAscending()

    repo = SQLAlchemyProjectRepository(db)

    return ProjectService(repo, strategy)


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
