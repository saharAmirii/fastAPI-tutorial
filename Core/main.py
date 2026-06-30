from fastapi import FastAPI, HTTPException, status, Query, Path, Form, UploadFile, File
from fastapi.responses import JSONResponse
import random
from typing import List
from contextlib import asynccontextmanager
from dataclasses import dataclass

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    print("Application startup")
    
    yield  

    print("Application shutdown")
   
app = FastAPI(lifespan=lifespan)


name_list = [
    {"name" : "ali", "id" : 1},
    {"name" : "maryam", "id" : 2},
    {"name" : "sara", "id" : 3},
    {"name" : "reza", "id" : 4},
    {"name" : "akbar", "id" : 5},
    {"name" : "hasan", "id" : 6},
    {"name" : "nazi", "id" : 7},
    {"name" : "hasan", "id" : 8},
    {"name" : "hasan", "id" : 9},
    {"name" : "hasan", "id" : 10},
    {"name" : "hasan", "id" : 11},
]


@dataclass
class Student():
    name : str
    age : int
    

@app.get("/names/{name_id}")
def retrieve_name_datail(name_id:int=Path(description="item id enter kon", alias="name_id")):
    for item in name_list:
        if item["id"] == name_id:
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Object Not Found!")



@app.get("/")
def roote():
    return JSONResponse(content={"message":"hello world!"}, status_code=status.HTTP_202_ACCEPTED)




@app.get("/names")
def retrieve_name_list(q:str | None = Query(description="enter a name to know if the user is here",example="sahar", alias="search", max_length=30, default=None)):
    if q:
       result = [item for item in name_list if item["name"] == q]
        
        
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="We do not have this specific user in our DB"
        )
    return result


@app.post("/names", status_code=status.HTTP_201_CREATED)
def create_user(name: str = Form()):
    name_obj = {"id": random.randint(12,100), "name" : name}
    name_list.append(name_obj)
    return name_obj

@app.get("/names/show")
def show_all():
    for item in name_list:
        return item
    
@app.post("/uploadfile/")
async def upload_file(file: UploadFile):
    content = await file.read()
    return {"filename": file.filename, "content_type": file.content_type, "file_size": len(content)}


@app.post("/upload-multiple/")
def upload_multiple(files: List[UploadFile]):
    return [
        {"filename": file.filename, "content_type": file.content_type} 
        for file in files
    ]