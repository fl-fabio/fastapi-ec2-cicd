from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="FastAPI EC2 CI/CD Demo",
    description="API dimostrativa per pipeline CI/CD con Docker, GitHub Actions ed EC2",
    version="1.0.0"
)

courses = [
    {
        "id": 1,
        "title": "Fondamenti di Python",
        "level": "base",
        "hours": 20
    },
    {
        "id": 2,
        "title": "Introduzione a FastAPI",
        "level": "intermedio",
        "hours": 12
    },
    {
        "id": 3,
        "title": "Docker per applicazioni backend",
        "level": "intermedio",
        "hours": 16
    },
    {
        "id": 4,
        "title": "CI/CD con GitHub Actions",
        "level": "avanzato",
        "hours": 18
    },
    {
        "id": 5,
        "title": "Test Python",
        "level": "avanzato",
        "hours": 10
    }
]


@app.get("/")
def root():
    return {
        "message": "Applicazione FastAPI in esecuzione su EC2",
        "status": "ok"
    }


@app.get("/courses")
def get_courses():
    return {
        "count": len(courses),
        "data": courses
    }


@app.get("/courses/{course_id}")
def get_course_by_id(course_id: int):
    for course in courses:
        if course["id"] == course_id:
            return course

    raise HTTPException(
        status_code=404,
        detail="Corso non trovato"
    )


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }