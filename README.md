# Student Management API

A FastAPI-based backend application for managing students using a clean modular architecture (CRUD operations, SQLAlchemy ORM, and Pydantic validation).  
This project follows FastAPI bigger applications structure for scalability and maintainability.

---

## Features

- Create new students
- Retrieve all students (with pagination)
- Search students by name
- Get student by ID
- Update student information
- Delete student
- SQLite database integration
- Automatic API documentation with FastAPI

---

## Project Structure

student-management-api/
│
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   ├── dependencies.py
│   ├── utils.py
│   ├── response.py
│   └── routers/
│       └── students.py
│
├── students.db
├── requirements.txt
└── README.md

---

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
- SQLite

---

## Installation

### Clone repository
git clone https://github.com/Beth-BZ/student-management-api.git
cd student-management-api

### Create virtual environment
python -m venv venv

Activate (Windows)
venv\Scripts\activate

### Install dependencies
pip install -r requirements.txt

---

## Run Application

uvicorn app.main:app --reload

---

## API Documentation

Swagger UI:
http://127.0.0.1:8000/docs

ReDoc:
http://127.0.0.1:8000/redoc

---

## API Endpoints

POST /students
GET /students
GET /students/search
GET /students/{id}
PUT /students/{id}
DELETE /students/{id}

---

## Example Request Body

{
  "name": "John Doe",
  "email": "john@example.com"
}

---

## Author

Bethlehem Belete

---

## Future Improvements

- Add authentication (JWT)
- Use PostgreSQL instead of SQLite
- Add Docker support
- Add unit testing
- Improve logging system
