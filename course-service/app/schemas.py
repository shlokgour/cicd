from pydantic import BaseModel, ConfigDict

class CourseCreate(BaseModel):
    name: str
    duration_years: int
    department: str

class CourseResponse(CourseCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)
    