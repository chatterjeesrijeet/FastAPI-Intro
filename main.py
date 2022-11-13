from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title : str
    content : str
    published : bool = True
    rating : Optional[int] = None

my_posts = [
    {
        "id" : 1,
        "title" : "This is title for post 1",
        "content": "This is content for post 1"
    },
    {
        "id" : 2,
        "title" : "This is title for post 2",
        "content": "This is content for post 2"
    }
]

def find_post(id):
    for ele in my_posts:
        if ele["id"] == id:
            return ele
    return None

def find_index_post(id):
    for idx,ele in enumerate(my_posts):
        if ele["id"] == id:
            return idx
    return -1

@app.get("/"):
def hello():
    return {"message" :"This is my forst app"}

@app.get("/posts")
def get_posts():
    return {"data":my_posts}
    pass




