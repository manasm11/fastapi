from enum import Enum
from typing import Optional

from fastapi import APIRouter, Depends, Response, status

from .blog_post import required_functionality

router = APIRouter(tags=["Blog"], prefix="/blog")


@router.get("/all", response_description="List of all blogs")
def all_blogs(req: dict = Depends(required_functionality)):
    """Retrieve all blogs."""
    return {"message": "All blogs", "req": req}


@router.get("/{id}")
def blog_with_id(id: int, response: Response):
    """Retrieve a specific blog using id."""
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Blog with ID {id} NOT FOUND"}
    return {"message": f"Blog with ID {id}"}


class BlogType(str, Enum):
    travel = "travel"
    howto = "howto"
    philosophy = "philosophy"


@router.get("/type/{type}")
def blogs_of_certain_type(type: BlogType):
    """Retrieve blogs of a certain category"""
    return {"message": f"All blogs of category {type}"}


@router.get("/{id}/comment/{comment_id}", tags=["Comment"])
def get_comment(
    id: int, comment_id: int, valid: bool = True, username: Optional[str] = ""
):
    """
    Retrieve comment of a blog
    - **id** mandatory blog id
    - **comment_id** mandatory comment id
    - **valid** optional valid boolean
    - **username** optional username
    """
    return {
        "message": f"blog_id {id}, comment_id {comment_id}, valid {valid} username {username}"
    }
