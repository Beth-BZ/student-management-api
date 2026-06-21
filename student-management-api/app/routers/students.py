from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import app.crud as crud
from app.dependencies import get_db
from app.schemas import StudentCreate, StudentResponse

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.post("/", response_model=StudentResponse)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    return crud.create_student(db, student)


@router.get("/", response_model=list[StudentResponse])
def get_students(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return crud.get_students(db, skip, limit)


@router.get("/search", response_model=list[StudentResponse])
def search_students(
    name: str,
    db: Session = Depends(get_db)
):
    return crud.search_students(db, name)


@router.get("/{student_id}", response_model=StudentResponse)
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = crud.get_student_by_id(db, student_id)

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


@router.put("/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    updated_student = crud.update_student(
        db,
        student_id,
        student
    )

    if not updated_student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return updated_student


@router.delete("/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    deleted_student = crud.delete_student(
        db,
        student_id
    )

    if not deleted_student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {"message": "Student deleted successfully"}