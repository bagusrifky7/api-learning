# import libraries
import uvicorn
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing_extensions import Optional
from random import randrange
from sqlalchemy.orm import Session
from database import engine
import models


# create endpoint
app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Supabase is connected"
    }
    
if __name__=="__main__":
    uvicorn.run("main:app", port=9700, host="0.0.0.0", reload=True)