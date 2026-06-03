from fastapi import FastAPI
from app.database import engine, Base # SQLAlchemy database engine and declarative base
from app import models 
from app.routers import projects, education, experience, skills, auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(docs_url=None, redoc_url=None) # creates application

origins = [
    "https://galymzhan.xyz",
    "https://www.galymzhan.xyz"
]

Base.metadata.create_all(bind=engine) # creates all tables that do not exist yet

app.include_router(projects.router, prefix='/api')
app.include_router(education.router, prefix='/api')
app.include_router(experience.router, prefix='/api')
app.include_router(skills.router, prefix='/api')
app.include_router(auth.router, prefix='/api')

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