from sqlalchemy.orm import Session

import exceptions
from auth import oauth2
from db.database import get_db
from db.hash import Hash
from db.models import DbUser
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags=["Auth"])


@router.post("/token")
def get_token(
    request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user: DbUser = db.query(DbUser).filter(DbUser.username == request.username).first()
    if not user:
        raise exceptions.UserNotFoundException()
    if not Hash.verify(user.password, request.password):
        raise exceptions.IncorrectPasswordException()
    access_token = oauth2.create_access_token(data={"kft": user.username})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": user.id,
        "username": user.username,
    }
