import uvicorn
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing_extensions import Optional
from random import randrange
from sqlalchemy.orm import Session
from database import engine, get_db
import models

# updating database
print("Syncing database schema with Supabase...")
models.Base.metadata.create_all(bind=engine) # importing Base that inherit by many table from models
print("Database is up to date")

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

# create post for get
my_post = [
    {"title": "title of post one", "content": "content of post 1", "id": "1"},
    {"title": "title of post two", "content": "content of post 2", "id": "2"}
    ]


# function for finding posts
def find_post(id):
    for p in my_post:
        if p["id"] == id:
            return p

# function for getting post index
def get_post_index(id):
    for i, p in enumerate(my_post):
        if p['id'] == id:
            return i

# create api endpoint
app = FastAPI()

@app.get("/")
def root():
    return {
        "Status": "OK"
    }

# for create and updating model
@app.get("/create_db")
def db_stuff(db: Session = Depends(get_db)):
    posts = db.query()

@app.get("/posts")
def get_posts():
    return {"data": my_post}

@app.post("/createposts")
def create_posts(state_post: Post):
    # convert into dictionary
    post_dict = state_post.dict()
    post_dict["id"] = randrange(1, 100000)
    my_post.append(post_dict)  
    return {"data": state_post}

# findinng post with specific id
@app.get("/posts/{id}")
def get_post(id, response: Response):

    post = find_post(id)
    if not post: # if the id is not found
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with this id {id} is not found")
    
    return {"post_detail": post}

# get latest post
@app.get("/posts/latest")
def get_latest_post():
    if not my_post:
        return {"latest_post": "Post not available"}

    latest = my_post[-1]
    return {"latest_post": latest}

# delete post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id):
    # get post index (because is a list)
    index = get_post_index(id)
    if index == None: # if index not found
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with this id {id} is not found")
    
    # deleting the post
    my_post.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# update post
@app.put("/posts/{id}") 
def update_post(id, post: Post):
    # get post index
    index = get_post_index(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with this id {id} is not found")

    post_dict = post.dict()
    post_dict["id"] = id
    my_post[index] = post_dict

    return {"data": post_dict}

# running the api
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9500, reload=True)