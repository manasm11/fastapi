from typing import List

from pydantic import BaseModel


#######################################################
###                    REQUESTS                     ###
#######################################################
class UserRequest(BaseModel):
    username: str
    email: str
    password: str


class ArticleRequest(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int


class ProductRequest(BaseModel):
    title: str
    description: str
    price: float


#######################################################
###                    RESPONSES                    ###
#######################################################
class _ArticleInUserResponse(BaseModel):
    title: str
    content: str
    published: bool

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    username: str
    email: str
    items: List[_ArticleInUserResponse]

    class Config:
        orm_mode = True


class _UserInArticleResponse(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


class ArticleResponse(BaseModel):
    title: str
    content: str
    published: bool
    user: _UserInArticleResponse

    class Config:
        orm_mode = True
