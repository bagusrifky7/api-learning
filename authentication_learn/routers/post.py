import models, schemas
from database import get_db
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing_extensions import List, Optional
from sqlalchemy import func



# create router
router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)


# router endpoint
@router.get("/", response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    posts = db.query(
        models.Post, 
    )
    
## NOT FINISH
