from app.models import Student


def create_student(db, student):

    new_student = Student(
        name=student.name,
        email=student.email
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


def get_student_by_id(db, student_id: int):
    return db.query(Student).filter(
        Student.id == student_id
    ).first()


def update_student(db, student_id, student_data):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        return None

    student.name = student_data.name
    student.email = student_data.email

    db.commit()
    db.refresh(student)

    return student


def delete_student(db, student_id):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        return None

    db.delete(student)
    db.commit()

    return student
def get_students(db, skip: int = 0, limit: int = 10):

    return db.query(Student).offset(skip).limit(limit).all()

def search_students(db, name: str):

    return db.query(Student).filter(
        Student.name.contains(name)
    ).all()