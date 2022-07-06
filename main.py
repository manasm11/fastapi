import exceptions
from auth import authentication
from db import database, models
from fastapi import FastAPI
from routers import article, blog_get, blog_post, product, user

models.Base.metadata.create_all(database.engine)

app = FastAPI()


#######################################################
###                    ROUTES                       ###
#######################################################
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(product.router)


@app.get("/hello")
def test_endpoint():
    """Check if the server is online or not."""
    return {"message": "API is live", "alive": True}


#######################################################
###              EXCEPTION HANDLERS                 ###
#######################################################
app.add_exception_handler(
    exceptions.UserNotFoundException, exceptions.user_not_found_handler
)
app.add_exception_handler(
    exceptions.ArticleNotFoundException, exceptions.article_not_found_handler
)
app.add_exception_handler(
    exceptions.IncorrectPasswordException, exceptions.incorrect_password_handler
)
app.add_exception_handler(
    exceptions.UnauthorizedException, exceptions.unauthorized_handler
)
app.add_exception_handler(exceptions.ForbiddenException, exceptions.forbidden_handler)
