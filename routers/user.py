from sqlalchemy.orm import Session

from db import db_user
from db.database import get_db
from fastapi import APIRouter, Depends, status
from schemas import UserBase, UserDisplay

router = APIRouter(prefix="/user", tags=["User"])

# Create User
@router.post("/", response_model=UserDisplay, status_code=status.HTTP_201_CREATED)
def create_user(user: UserBase, db: Session = Depends(get_db)):
    new_user = db_user.create_user(db, user)
    return new_user


# Read User

# Update User

# Delete User
