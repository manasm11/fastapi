import exceptions
from auth import authentication
from db import database, models
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import article, blog_get, blog_post, file, product, user

models.Base.metadata.create_all(database.engine)

app = FastAPI()


#######################################################
###                    ROUTES                       ###
#######################################################
app.include_router(file.router)
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(product.router)

app.mount("/files", StaticFiles(directory="files"), name="files")


@app.get("/hello")
def test_endpoint():
    """Check if the server is online or not."""
    return {"message": "API is live", "alive": True}


#######################################################
###              EXCEPTION HANDLERS                 ###
#######################################################
app.add_exception_handler(exceptions.UserNotFound, exceptions.user_not_found)
app.add_exception_handler(exceptions.ArticleNotFound, exceptions.article_not_found)
app.add_exception_handler(exceptions.IncorrectPassword, exceptions.incorrect_password)
app.add_exception_handler(exceptions.Unauthorized, exceptions.unauthorized)
app.add_exception_handler(exceptions.Forbidden, exceptions.forbidden)
