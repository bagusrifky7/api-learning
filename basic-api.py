from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing_extensions import Optional

class Post(BaseModel):
    title: str
    content: str
    published: bool = False
    rating: Optional[int] = None

# create in memoy
my_store = [{"title": "title of post one", "content": "content of pose 1" }]

app = FastAPI()

@app.get("/")
def root():
    return {
        "Status": "OK"
    }

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/createposts")
def create_posts(payload: Post):
    print(payload)
    return {"state": payload}
