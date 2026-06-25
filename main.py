from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr
from typing import List, Dict, Any

import database as db

app = FastAPI(title="School Registration API")



# @app.on_event("startup")
def startup_event():
    db.create_table()



def row_to_dict(row) -> Dict[str, Any]:
    return dict(row) if row else {}



class Student(BaseModel):
    name: str
    age: int
    email: EmailStr 
    country: str
    id_number: int

class Teacher(BaseModel):
    name: str
    email: EmailStr
    department: str
    office_room: str
    employee_id: int

class Course(BaseModel):
    course_code: str
    title: str
    credit: int
    semester: str
    teacher_id: int




@app.get("/")
def home():
    return {"message": "Welcome to my first server"}




@app.post("/students/", status_code=status.HTTP_201_CREATED)
def register_student(student: Student):
    try:
        db.add_student(student.name, student.age, student.email, student.country, student.id_number)
        return {"message": "Student registered successfully", "student": student}
    except Exception:
        raise HTTPException(status_code=400, detail="Could not register student. ID or email already exists.")

@app.get("/students/")
def list_students():
    rows = db.get_students()
    return [row_to_dict(r) for r in rows]

@app.get("/students/{id_number}")
def get_student_by_id(id_number: int):
    student = db.get_student_by_id(id_number)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return row_to_dict(student)

@app.put("/students/{id_number}")
def update_student_data(id_number: int, student: Student):
    existing = db.get_student_by_id(id_number)
    if not existing:
        raise HTTPException(status_code=404, detail="Student not found")
    db.update_student(id_number, student.name, student.age, student.email, student.country)
    return {"message": "Student updated successfully", "student": student}

@app.delete("/students/{id_number}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student_record(id_number: int):
    existing = db.get_student_by_id(id_number)
    if not existing:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete_student(id_number)
    return None


@app.post("/teachers/", status_code=status.HTTP_201_CREATED)
def register_teacher(teacher: Teacher):
    try:
        db.add_teacher(teacher.name, teacher.email, teacher.department, teacher.office_room, teacher.employee_id)
        return {"message": "Teacher registered successfully", "teacher": teacher}
    except Exception:
        raise HTTPException(status_code=400, detail="Could not register teacher. ID or email already exists.")

@app.get("/teachers/")
def list_teachers():
    rows = db.get_teachers()
    return [row_to_dict(r) for r in rows]

@app.get("/teachers/{employee_id}")
def get_teacher_by_id(employee_id: int):
    teacher = db.get_teacher_by_id(employee_id)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return row_to_dict(teacher)

@app.put("/teachers/{employee_id}")
def update_teacher_data(employee_id: int, teacher: Teacher):
    existing = db.get_teacher_by_id(employee_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Teacher not found")
    db.update_teacher(employee_id, teacher.name, teacher.email, teacher.department, teacher.office_room)
    return {"message": "Teacher updated successfully", "teacher": teacher}

@app.delete("/teachers/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_teacher_record(employee_id: int):
    existing = db.get_teacher_by_id(employee_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Teacher not found")
    db.delete_teacher(employee_id)
    return None




@app.post("/courses/", status_code=status.HTTP_201_CREATED)
def register_course(course: Course):
    try:
        db.add_course(course.course_code, course.title, course.credits, course.semester, course.teacher_id)
        return {"message": "Course registered successfully", "course": course}
    except Exception:
        raise HTTPException(status_code=400, detail="Could not register course. Verify course code unique constraint.")

@app.get("/courses/")
def list_courses():
    rows = db.get_courses()
    return [row_to_dict(r) for r in rows]

@app.get("/courses/{course_code}")
def get_course_by_code(course_code: str):
    course = db.get_course_by_code(course_code)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return row_to_dict(course)

@app.put("/courses/{course_code}")
def update_course_data(course_code: str, course: Course):
    existing = db.get_course_by_code(course_code)
    if not existing:
        raise HTTPException(status_code=404, detail="Course not found")
    db.update_course(course_code, course.title, course.credits, course.semester, course.teacher_id)
    return {"message": "Course updated successfully", "course": course}

@app.delete("/courses/{course_code}", status_code=status.HTTP_204_NO_CONTENT)
def delete_course_record(course_code: str):
    existing = db.get_course_by_code(course_code)
    if not existing:
        raise HTTPException(status_code=404, detail="Course not found")
    db.delete_course(course_code)
    return None


















































# from fastapi import FastAPI
# from pydantic import BaseModel #how to validate
# from database import create_table, add_student, get_student

# app=FastAPI()

# create_table=()

# class Student(BaseModel):
#     name:str #type hint
#     age: int
#     email: str
#     country:str
#     id_number:int

# students=[]

# @app.get("/")

# def home ():
#     return{"message: Welcome to my firstserver "}

# @app.get("/students")
# def list_students():
#     return students

# @app.post("/students")
# def register_student(student:Student):
#     students.append(student)
#     return {"message":"Student reistered", "student":student}



# @app.post("/students")
# def register_student(student:Student):
#     add_student(student.name, student.age,student.email, student.country, student.id_number)
#     return {"message": "Student registered successfully", "student": student}





































# # from fastapi import FastAPI
# # app=FastAPI()
# # @app.get("/")
# # def home():
# #     return {"message":"Welcome to my first server"}
# # @app.get("students")
# # def list_student():
# #     students=[]
# #     return students
