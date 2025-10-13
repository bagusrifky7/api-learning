# import libraries
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

from pydantic.types import conint

# post title and content
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

# class for create post
class PostCreate(PostBase):
    pass 

# class for record user when logging out
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


# class for creating post
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True


# classs when the posting is out
class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode: True

# class for creating user
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# class for login user
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# class for access token
class Token(BaseModel):
    access_token: str
    token_type: str

# class for token data
class TokenData(BaseModel):
    id: Optional[str] = None


# class for vote
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)


