from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base

class Post(Base):
    __tablename__ = "posts" # table name

    id = Column(Integer, primary_key=True, nullable=False) # post id
    title = Column(String, nullable=False) # post title
    content = Column(String, nullable=False) # post content
    published = Column(Boolean, server_default=True, nullable=False) # published or not
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()')) # post created at
    owner_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False) # users id in users table

    owner = relationship("User") # tied to User class

class User(Base):
    __tablename__ = "users" # table name

    id = Column(Integer, primary_key=True, nullable=False) # user id
    email = Column(String, nullable=False, unique=True) # user email
    password = Column(String, nullable=False) # user password
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()')) # user created date

class Vote(Base):
    __tablename__ = "votes"

    user_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), primary_key=True, nullable=False) # foreign key from users table as primary key
    post_id = Column(Integer, ForeignKey(
        "posts.id", ondelete="CASCADE"), primary_key=True, nullable=False) # foreign key from post tabele as primary key






