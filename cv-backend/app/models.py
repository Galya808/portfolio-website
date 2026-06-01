from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, Date
from datetime import datetime
from app.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    github_url = Column(String, nullable=True)
    live_url = Column(String, nullable=True)
    technologies = Column(String, nullable=True)
    image_url = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String)
    proficiency_level = Column(Integer)

class Experience(Base):
    __tablename__ = "experiences"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, nullable=True)
    position = Column(String)
    description = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    is_current = Column(Boolean, default=False)

class Education(Base):
    __tablename__ = "education"

    id = Column(Integer, primary_key=True, index=True)
    institution = Column(String, nullable=False)
    degree = Column(String)
    field_of_study = Column(String)
    start_year = Column(Integer)
    end_year = Column(Integer)
    