from typing import List

from sqlalchemy.orm import Session

from db import db_user
from db.database import get_db
from fastapi import APIRouter, Depends, Path, Response, status
from schemas import UserBase, UserDisplay

router = APIRouter(prefix="/user", tags=["User"])

# Create User
@router.post("/", response_model=UserDisplay, status_code=status.HTTP_201_CREATED)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    new_user = db_user.create_user(db, request)
    return new_user


# Read All Users
@router.get("/", response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)


# Read One User
@router.get("/{user_id}", response_model=UserDisplay)
def get_one_user(user_id: int, db: Session = Depends(get_db)):
    user = db_user.get_one_user(db, user_id)
    return user


# Update User
@router.post("/{user_id}/update", response_model=UserDisplay)
def update_user(user_id: int, request: UserBase, db: Session = Depends(get_db)):
    return db_user.update_user(db, request, user_id)


# Delete User
@router.get("/{user_id}/delete")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return db_user.delete_user(db, user_id)
