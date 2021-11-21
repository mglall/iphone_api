from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from model import Todo

# app object
app = FastAPI()

from database import (
     fetch_one_iphone,
     fetch_all_iphones,
     create_iphone,
     fetch_one_iphone_by_model,
 )

origins = ['http://localhost:5055']

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins, 
    allow_credentials = True,
    allow_methods=["*"], 
    allow_headers=["*"],
)




# get all

@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_iphones()
    return response



# get by model 

@app.get("/api/todo/{model}")
async def get_todo_by_model(model):
    response = await fetch_one_iphone_by_model(model)
    if response: 
         
        return response
    raise HTTPException(404, f"there is no TODO item with this title{model}")

# get by model,capacity,colors

@app.get("/api/todo/{model}/{capacity}/{colors}",response_model=Todo)
async def get_todo_by_mcc(model, capacity, colors):
    response = await fetch_one_iphone(model, capacity, colors)
    if response: 
        return response
    raise HTTPException(404, f"there is no TODO item with this title{model,capacity,colors}")

# post

@app.post("/api/todo", response_model=Todo)
async def post_todo(todo:Todo):
    response = await create_iphone(todo.dict())
    if response:
        return response
    raise HTTPException(400, "something went wrong / Bad request")


