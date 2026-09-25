from fastapi import FastAPI
from .database import Base, engine
from .routers.students import router as student_router
from .routers import auth

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Microservice",
    description="Student Management Microservice using FastAPI and SQLite",
    version="1.0.0"
)

app.include_router(student_router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Student Microservice is running"}