from fastapi import FastAPI, Path
from enum import Enum
from typing import Optional
from pydantic import BaseModel
app = FastAPI()  #creating an instance of the FastAPI class

#creating the first endpoint
# @app.get("/hello/{name}")
# async def hello(name):
#     return f"Welcome to a new tutorial {name}"

class Available_Cuisines(str, Enum):
     indian= "indian"
     american= "american"
     italian= "italian"

food_items = {
    "indian": ["idli", "dosa"],
    "american": ["wings", "fries"],
    "italian": ["pizza", "pasta"],
}

@app.get("/get_cuisines/{cuisine}")
async def get_cuisines(cuisine: Available_Cuisines):
    return f"Eat loads of {food_items.get(cuisine)}"

#one advantage of fastapi over flask is that we do not have to write any validation code. Fastapi has inbuilt input validation
#second advantage of fastapi over flask is inbuilt documentation (redoc and doc)
#fast performance time almost at par with a node/express server
#faster development with lesser bugs

students = {
    1: {
        "name":"Shourjo",
        "email":"shourjo@yahoo.com",
        "age": 23
    },
    2: {
        "name":"Yash",
        "email":"yash@yahoo.com",
        "age": 29
    },
    3: {
        "name":"Shashank",
        "email":"ss@yahoo.com",
        "age": 24
    }
}

class Student(BaseModel):
    name: str
    email:str
    age:int

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    email:Optional[str] = None
    age:Optional[int] = None
    
#path params
@app.get("/get_students/{id}")
async def get_students(id: int = Path( description="This is the id of the student you want to view", gt=0)):
    return students[id]

#query params
@app.get("/get_students_byname")
async def get_students_byname(*, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}

#query params and path params
@app.get("/get_students_byname2/{id}")
async def get_students_byname2(*, id: int,name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}

#post method
@app.post("/create_student/{id}")
async def create_student(id: int, student: Student):
    if id in students:
       return {"Error":"Student already exists"}  
    students[id] = student
    return students[id]

#put method

@app.put("/update_student/{id}")
async def update_student(id: int, student: UpdateStudent):
    if id not in students:
       return {"Error":"Student does not exist"}  
   
    if student.name != None:
        students[id]["name"] = student.name 
    if student.email != None:
        students[id]["email"] = student.email 
    if student.age != None:
        students[id]["age"] = student.age 
                
    return students[id]

#delete method

@app.delete("/delete_student/{id}")
async def delete_student(id: int):
    if id not in students:
       return {"Error":"Student does not exist"}  
    del students[id]
    return {"Success":"Student deleted successfully`"} 
                
