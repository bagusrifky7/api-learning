# import libraries
import models, schemas, utils
from fastapi import FastAPI, HTTPException, status, Depends, Response
from sqlalchemy.orm import Session
from .database import get_db

app = FastAPI()

@app.post("/user", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # hash the password
    hashed_password = utils.hash(user.password)
    
    # updating the pasword in schemas
    user.password = hashed_password
    
    # create user
    new_user = models.User(email=user.email, password=user.password)
    
    # put the data into the database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    # return response based on specified response model
    return new_user

@app.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    # query to filter user by id
    user = db.query(models.User).filter(models.User.id == id).first()
   
    # if not user 
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with {id} does not exist")
    
    return user
