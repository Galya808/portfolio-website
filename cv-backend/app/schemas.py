from pydantic import BaseModel
from datetime import datetime, date


class ProjectBase(BaseModel):
    title: str
    description: str | None = None
    github_url: str | None = None
    live_url: str | None = None
    technologies: str | None = None
    image_url: str | None = None

class ProjectCreate(ProjectBase):
    pass

class ProjectResponse(ProjectBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class SkillBase(BaseModel):
    name: str
    category: str | None = None
    proficiency_level: int | None = None

class SkillCreate(SkillBase):
    pass

class SkillResponse(SkillBase):
    id: int

    class Config:
        orm_mode = True


class ExperienceBase(BaseModel):
    company_name: str 
    position: str | None = None
    description: str | None = None
    start_date: date
    end_date: date
    is_current: bool | None = None

class ExperienceCreate(ExperienceBase):
    pass

class ExperienceResponse(ExperienceBase):
    id: int

    class Config:
        orm_mode = True


class EducationBase(BaseModel):
    institution: str
    degree: str | None = None
    field_of_study: str | None = None
    start_year: int
    end_year: int | None = None

class EducationCreate(EducationBase):
    pass

class EducationResponse(EducationBase):
    id: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int 
    username: str
    email: str

    class Config:
        orm_mode = True