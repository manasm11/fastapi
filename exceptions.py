from os import stat

from fastapi import Request, status
from fastapi.responses import JSONResponse


class UserNotFoundException(Exception):
    def __init__(self, id: int = 0):
        if id:
            self.message = f"User with id {id} not found"
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
