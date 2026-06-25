from pydantic import BaseModel, EmailStr

# ==========================================
# STUDENT SCHEMAS
# ==========================================

class Student(BaseModel):
    name: str
    age: int
    email: EmailStr  # Ensures emails follow standard user@domain.com formatting
    country: str
    id_number: int

# ==========================================
# TEACHER SCHEMAS
# ==========================================

class Teacher(BaseModel):
    name: str
    email: EmailStr
    department: str
    office_room: str
    employee_id: int

# ==========================================
# COURSE SCHEMAS
# ==========================================

class Course(BaseModel):
    course_code: str
    title: str
    credits: int
    semester: str
    teacher_id: int
