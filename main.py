import utils
from fastapi import Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from fastapi import HTTPException
from fastapi import FastAPI, HTTPException
from database import engine, SessionLocal, Base
from schemas import StudentCreate, StudentResponse
import crud


app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
   return utils.success_response(
    "Student created successfully"
   
)

@app.post("/students", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):

    new_student = crud.create_student(db, student)

    return new_student


from typing import List

@app.get("/students", response_model=List[StudentResponse])
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):

    students = crud.get_students(db, skip=skip, limit=limit)

    return students

@app.get("/students/search", response_model=List[StudentResponse])
def search_student(name: str, db: Session = Depends(get_db)):

    students = crud.search_students(db, name)

    return utils.success_response(
        "Students search completed",
        students
    )

@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int):

    db = SessionLocal()

    student = crud.get_student_by_id(db, student_id)

    db.close()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return utils.success_response(
        "Student retrieved successfully",
        {
            "id": student.id,
            "name": student.name,
            "email": student.email
        }
    )

@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student: StudentCreate):

    db = SessionLocal()

    updated_student = crud.update_student(db, student_id, student)

    db.close()

    if not updated_student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return utils.success_response(
        "Student updated successfully",
        {
            "id": updated_student.id,
            "name": updated_student.name,
            "email": updated_student.email
        }
    )


@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    db = SessionLocal()

    deleted_student = crud.delete_student(db, student_id)

    db.close()

    if not deleted_student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return utils.success_response(
        "Student deleted successfully",
        {
            "id": deleted_student.id,
            "name": deleted_student.name,
            "email": deleted_student.email
        }
    )