from os import stat
from typing import Union

from fastapi import Request, status
from fastapi.responses import JSONResponse


class UserNotFound(Exception):
    def __init__(self, id_or_username: Union[str, int] = None):
        if type(id_or_username) == int:
            self.message = f"User with id {id} not found"
        elif type(id_or_username) == str:
            self.message = f"User with username {id_or_username} not found"
        else:
            self.message = f"User not found"


def user_not_found(request: Request, exc: UserNotFound):
    return JSONResponse({"detail": exc.message}, status_code=status.HTTP_404_NOT_FOUND)


class ArticleNotFound(Exception):
    def __init__(self, id: int = 0):
        if id:
            self.message = f"Article with id {id} not found"
        else:
            self.message = f"Article not found"


def article_not_found(request: Request, exc: ArticleNotFound):
    return JSONResponse({"detail": exc.message}, status_code=status.HTTP_404_NOT_FOUND)


class IncorrectPassword(Exception):
    def __init__(self):
        self.message = f"Incorrect password"


def incorrect_password(request: Request, exc: IncorrectPassword):
    return JSONResponse(
        {"detail": exc.message}, status_code=status.HTTP_401_UNAUTHORIZED
    )


class Unauthorized(Exception):
    def __init__(self):
        self.message = f"Could not validate credentials"


def unauthorized(request: Request, exc: Unauthorized):
    return JSONResponse(
        {"detail": exc.message}, status_code=status.HTTP_401_UNAUTHORIZED
    )


class Forbidden(Exception):
    def __init__(self):
        self.message = f"You are not authorized to access this resource"


def forbidden(request: Request, exc: Forbidden):
    return JSONResponse({"detail": exc.message}, status_code=status.HTTP_403_FORBIDDEN)
