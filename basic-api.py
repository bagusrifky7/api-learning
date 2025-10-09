from fastapi import FastAPI, Response, status
from fastapi.params import Body
from pydantic import BaseModel
from typing_extensions import Optional
from random import randrange

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

# functio  for finding posts
def find_post(id):
    for p in my_post:
        if p["id"] == id:
            return p

app = FastAPI()

@app.get("/")
def root():
    return {
        "Status": "OK"
    }

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
    if not my_post:
        # we want the status code in 404
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Post with this id {id} is not found"}

    post = find_post(id)
    return post

# get latest post
@app.get("/posts/latest")
def get_latest_post():
    if not my_post:
        return {"latest_post": "Post not available"}

    latest = my_post[-1]
    return {"latest_post": latest}
