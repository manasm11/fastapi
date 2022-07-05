from typing import Optional
from fastapi import FastAPI, Response
from enum import Enum


app = FastAPI()


@app.get("/hello")
def test_endpoint():
    """Check if the server is online or not."""
    return {"message": "API is live", "alive": True}


@app.get("/blog/all", tags=["Blog"], response_description="List of all blogs")
def all_blogs():
    """Retrieve all blogs."""
    return {"message": "All blogs"}


@app.get("/blog/{id}", tags=["Blog"])
def blog_with_id(id: int, response: Response):
    """Retrieve a specific blog using id."""
    if id > 5:
        response.status_code = 404
        return {"error": f"Blog with ID {id} NOT FOUND"}
    return {"message": f"Blog with ID {id}"}


class BlogType(str, Enum):
    travel = "travel"
    howto = "howto"
    philosophy = "philosophy"


@app.get("/blog/type/{type}", tags=["Blog"])
def blogs_of_certain_type(type: BlogType):
    """Retrieve blogs of a certain category"""
    return {"message": f"All blogs of category {type}"}


@app.get("blog/{id}/comment/{comment_id}", tags=["Blog", "Comment"])
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
