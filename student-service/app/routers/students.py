from ..course_client import get_courses_from_course_service
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Student
from ..schemas import StudentCreate, StudentResponse
from ..security import get_current_user, oauth2_scheme

router = APIRouter(prefix="/students", tags=["Students"])

@router.get("/test-auth")
def test_auth(user: str = Depends(get_current_user)):
    return {"message": "JWT authentication successful", "user": user}

@router.post("/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db),
                    user: str = Depends(get_current_user)):
    existing_student = db.query(Student).filter(Student.email == student.email).first()
    if existing_student:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_student = Student(
        name=student.name, age=student.age,
        course=student.course, email=student.email
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@router.get("/", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return db.query(Student).all()

@router.get("/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db),
                 user: str = Depends(get_current_user)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.put("/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student_data: StudentCreate,
                    db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    student.name = student_data.name
    student.age = student_data.age
    student.course = student_data.course
    student.email = student_data.email
    db.commit()
    db.refresh(student)
    return student

@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db),
                    user: str = Depends(get_current_user)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return {"message": "Student deleted successfully"}

@router.get("/{student_id}/courses")
def get_student_with_courses(
    student_id: int,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    courses = get_courses_from_course_service(token)

    return {
        "student": student.name,
        "available_courses": courses
    }