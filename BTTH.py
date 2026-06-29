from fastapi import FastAPI
app = FastAPI()
courses = [
    {
        "id": 1,
        "code": "PY101",
        "name": "Python Basic",
        "level": "beginner",
        "price": 1500000
    },
    {
        "id": 2,
        "code": "FA101",
        "name": "FastAPI Basic",
        "level": "beginner",
        "price": 2000000
    }
]

@app.get("/health")
def check_the_system():
    return {
        "message": "API is running"
    }
@app.get("/courses")
def get_courses():
    return courses

@app.get("/courses/{course_id}")
def find_the_course(course_id: int):
    for course in courses:
        if course["id"] == course_id:
            return course
    return {
        "message": f"Không tìm thấy id là {course_id}"
    }
    