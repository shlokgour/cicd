from pydantic import BaseModel, ConfigDict

class StudentCreate(BaseModel):
    name: str
    age: int
    course: str
    email: str

class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    course: str
    email: str
    model_config = ConfigDict(from_attributes=True)
    