from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Course
from ..schemas import CourseCreate, CourseResponse
from ..security import get_current_user

router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)

# CREATE COURSE
@router.post("/", response_model=CourseResponse)
def create_course(
    course: CourseCreate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    new_course = Course(
        name=course.name,
        duration_years=course.duration_years,
        department=course.department
    )
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course

# GET ALL COURSES
@router.get("/", response_model=list[CourseResponse])
def get_courses(
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    courses = db.query(Course).all()
    return courses

# GET COURSE BY ID
@router.get("/{course_id}", response_model=CourseResponse)
def get_course(
    course_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course