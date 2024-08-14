from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        'name' : 'shiva',
        'age': 19,
        'city': 'surat'
    },
    2: {
        'name' : 'keyur',
        'age': 19,
        'city': 'surat'
    }
}

class Student(BaseModel):
    name: str
    age: int
    city: str
    
class UpdateStudent(BaseModel):
    name: Optional[str]
    age: Optional[int]
    city: Optional[str]

@app.get('/')
def index():
    return students

@app.get('/get_student/{student_id}')
def get_student(student_id: int = Path(description="Enter ID of Student : ")):
    return students[student_id]

@app.get('/get-by-name/{studnet_id}')
def get_name(student_id: int,name: Optional[str] = None):
    for i in students:
        if students[i]['name'] == name:
            return students[i]
    return {"Date": 'Not Found'}

@app.post('/create-student/{student_id}')
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"error": "student exists."}

    students[student_id] = student
    return students[student_id]

@app.put('/update-student/{student_id}')
def update_student(student_id: int,student: UpdateStudent):
    if student_id not in students:
        return {"error": "Data not Found."}
    
    if student.name != None:
        students[student_id]['name'] = student.name
    
    if student.age != None:
        students[student_id]['age'] = student.age
    
    if student.city != None:
        students[student_id]['city'] = student.city
        
    return students[student_id]

@app.delete('/delete_student/{student_id}')
def delete_student(student_id: int):
    if student_id not in students:
        return {"data": "not exitst"}
    
    del students[student_id]
    return {"message": "deleted."}