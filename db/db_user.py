from sqlalchemy.orm import Session

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
    # Handle any exceptions
    return user


def update_user(db: Session, request: UserRequest, id: int):
    users = db.query(DbUser).filter(DbUser.id == id)
    # Handle any exceptions
    users.update(
        {
            DbUser.email: request.email,
            DbUser.username: request.username,
            DbUser.password: Hash.bcrypt(request.password),
        }
    )
    db.commit()
    user = users.first()
    db.refresh(user)
    return user


def delete_user(db: Session, id: int):
    user = db.query(DbUser).get(id)
    # Handle any exceptions
    db.delete(user)
    db.commit()
    return {"message": f"User with id {id} deleted"}
