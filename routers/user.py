from typing import List

from sqlalchemy.orm import Session

from auth.oauth2 import get_current_user
from db import db_user
from db.database import get_db
from fastapi import APIRouter, Depends, status
from schemas import UserRequest, UserResponse

router = APIRouter(prefix="/user", tags=["User"])

# Create User
@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(request: UserRequest, db: Session = Depends(get_db)):
    new_user = db_user.create_user(db, request)
    return new_user


# Read All Users
@router.get("/", response_model=List[UserResponse])
def get_all_users(
    db: Session = Depends(get_db),
    current_user: UserRequest = Depends(get_current_user),
):
    return db_user.get_all_users(db)


# Read One User
@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: UserRequest = Depends(get_current_user),
):
    user = db_user.get_user(db, user_id)
    return user


# Update User
@router.post("/{user_id}/update", response_model=UserResponse)
def update_user(
    user_id: int,
    request: UserRequest,
    db: Session = Depends(get_db),
    current_user: UserRequest = Depends(get_current_user),
):
    return db_user.update_user(db, request, user_id)


# Delete User
@router.get("/{user_id}/delete")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: UserRequest = Depends(get_current_user),
):
    return db_user.delete_user(db, user_id)
