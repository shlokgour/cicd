from sqlalchemy import Column, Integer, String
from .database import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    duration_years = Column(Integer, nullable=False)
    department = Column(String, nullable=False)
    