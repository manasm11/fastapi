from typing import Optional

from pydantic import BaseModel

from fastapi import APIRouter

router = APIRouter(prefix="/blog", tags=["Blog"])


class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[bool]


@router.post("/new")
def create_blog(blog: BlogModel):
    return {"data": blog}
