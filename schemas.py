from pydantic import BaseModel, EmailStr

# STUDENT 

class Student(BaseModel):
    name: str
    age: int
    email: EmailStr 
    country: str
    id_number: int


# TEACHER 

class Teacher(BaseModel):
    name: str
    email: EmailStr
    department: str
    office_room: str
    employee_id: int

# COURSE 

class Course(BaseModel):
    course_code: str
    title: str
    credits: int
    semester: str
    teacher_id: int
