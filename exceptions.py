from os import stat
from typing import Union

from fastapi import Request, status
from fastapi.responses import JSONResponse


class UserNotFoundException(Exception):
    def __init__(self, id_or_username: Union[str, int] = None):
        if type(id_or_username) == int:
            self.message = f"User with id {id} not found"
        elif type(id_or_username) == str:
            self.message = f"User with username {id_or_username} not found"
        else:
            self.message = f"User not found"


def user_not_found_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse({"detail": exc.message}, status_code=status.HTTP_404_NOT_FOUND)


class ArticleNotFoundException(Exception):
    def __init__(self, id: int = 0):
        if id:
            self.message = f"Article with id {id} not found"
        else:
            self.message = f"Article not found"


def article_not_found_handler(request: Request, exc: ArticleNotFoundException):
    return JSONResponse({"detail": exc.message}, status_code=status.HTTP_404_NOT_FOUND)


class IncorrectPasswordException(Exception):
    def __init__(self):
        self.message = f"Incorrect password"


def incorrect_password_handler(request: Request, exc: IncorrectPasswordException):
    return JSONResponse(
        {"detail": exc.message}, status_code=status.HTTP_401_UNAUTHORIZED
    )


class UnauthorizedException(Exception):
    def __init__(self):
        self.message = f"Could not validate credentials"


def unauthorized_handler(request: Request, exc: UnauthorizedException):
    return JSONResponse(
        {"detail": exc.message}, status_code=status.HTTP_401_UNAUTHORIZED
    )


class ForbiddenException(Exception):
    def __init__(self):
        self.message = f"You are not authorized to access this resource"


def forbidden_handler(request: Request, exc: ForbiddenException):
    return JSONResponse({"detail": exc.message}, status_code=status.HTTP_403_FORBIDDEN)
