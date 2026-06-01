from fastapi import FastAPI
from app.database import engine, Base # SQLAlchemy database engine and declarative base
from app import models 
from app.routers import projects, education, experience, skills, auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() # creates application

origins = [
    "https://gala-portfolio-website.vercel.app/#about"
]

Base.metadata.create_all(bind=engine) # creates all tables that do not exist yet

app.include_router(projects.router)
app.include_router(education.router)
app.include_router(experience.router)
app.include_router(skills.router)
app.include_router(auth.router)

# connects to the frontend server
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/") # registers a simple GET request
def root():
    return {"message": "CV Backend is running"}