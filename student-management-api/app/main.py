from fastapi import FastAPI
from app.database import engine, Base
from app.routers import students

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(students.router)


@app.get("/")
def home():
    return {"message": "Student API"}