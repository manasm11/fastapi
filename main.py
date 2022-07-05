from fastapi import FastAPI
from routers import blog_get, blog_post

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/hello")
def test_endpoint():
    """Check if the server is online or not."""
    return {"message": "API is live", "alive": True}
