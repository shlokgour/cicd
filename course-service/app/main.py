from fastapi import FastAPI
from .database import Base, engine
from .routers.courses import router as course_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Course Microservice",
    description="Course Management Microservice using FastAPI and SQLite",
    version="1.0.0"
)

app.include_router(course_router)

@app.get("/")
def root():
    return {"message": "Course Microservice is running"}