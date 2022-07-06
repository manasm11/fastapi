from db import database, models
from fastapi import FastAPI
from routers import article, blog_get, blog_post, user

models.Base.metadata.create_all(database.engine)

app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/hello")
def test_endpoint():
    """Check if the server is online or not."""
    return {"message": "API is live", "alive": True}
