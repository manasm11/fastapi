from typing import Dict, List, Optional

from pydantic import BaseModel

from fastapi import APIRouter, Body, Path, Query

router = APIRouter(prefix="/blog", tags=["Blog"])


class Image(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[bool]
    tags: List[str]
    metadata: Dict[str, str]
    image: Optional[Image]


@router.post("/new/{id}")
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {"id": id, "version": version, "data": blog}


@router.post("new/{id}/comment/{comment_id}")
def create_comment(
    blog: BlogModel,
    id: int,
    comment_title: int = Query(
        None, description="Description of comment title", deprecated=True
    ),
    content: str = Body(..., max_length=50, min_length=10, regex="^[a-z\s]*$"),
    v: Optional[List[str]] = Query(["1.0", "2.1", "2.2"]),
    comment_id: int = Path(None, gt=5, le=10),
):
    return {
        "blog": blog,
        "id": id,
        "comment_title": comment_title,
        "content": content,
        "v": v,
        comment_id: comment_id,
    }


def required_functionality() -> dict:
    return {"message": "Learning FastAPI"}
