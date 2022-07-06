from sqlalchemy.orm import Session

import exceptions
from db.hash import Hash
from db.models import DbUser
from schemas import UserRequest


def create_user(db: Session, request: UserRequest):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_users(db: Session):
    return db.query(DbUser).all()


def get_one_user(db: Session, id: int):
    user = db.query(DbUser).get(id)
    if not user:
        raise exceptions.UserNotFound(id)
    return user


def update_user(db: Session, request: UserRequest, id: int):
    users = db.query(DbUser).filter(DbUser.id == id)
    user = users.first()
    if not user:
        raise exceptions.UserNotFound(id)
    users.update(
        {
            DbUser.email: request.email,
            DbUser.username: request.username,
            DbUser.password: Hash.bcrypt(request.password),
        }
    )
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, id: int):
    user = db.query(DbUser).get(id)
    if not user:
        raise exceptions.UserNotFound(id)
    db.delete(user)
    db.commit()
    return {"message": f"User with id {id} deleted"}


def get_user_by_username(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise exceptions.UserNotFound(username)
    return user
