from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import schemas
from app.auth import create_access_token, hash_password, verify_password
from app.repositories import user_repository


def register_user(db: Session, user: schemas.UserCreate):
    existing_user = user_repository.get_user_by_username(db, user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed = hash_password(user.password)
    return user_repository.create_user(db, user, hashed)


def login_user(db: Session, username: str, password: str):
    db_user = user_repository.get_user_by_username(db, username)

    if not db_user or not verify_password(password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="invalid credentials")

    token = create_access_token({"sub": db_user.username})
    return {"access_token": token, "token_type": "bearer"}
