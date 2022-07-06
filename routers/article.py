from typing import List

from sqlalchemy.orm import Session

import exceptions
from auth.oauth2 import get_current_user, oauth2_schema
from db import db_article
from db.database import get_db
from fastapi import APIRouter, Depends, status
from schemas import ArticleRequest, ArticleResponse, UserRequest

router = APIRouter(
    prefix="/article",
    tags=["Article"],
)


@router.post("/", response_model=ArticleResponse, status_code=status.HTTP_201_CREATED)
def create_article(request: ArticleRequest, db: Session = Depends(get_db)):
    return db_article.create_article(db, request)


@router.get("/{article_id}", response_model=ArticleResponse)
def get_one_article(
    article_id: int,
    db: Session = Depends(get_db),
    current_user: UserRequest = Depends(get_current_user),
):
    article = db_article.get_one_article(db, article_id)
    if article.user_id != current_user.id:
        raise exceptions.Forbidden()
    return article


@router.post("/{article_id}/update", response_model=ArticleResponse)
def update_article(
    article_id: int, request: ArticleRequest, db: Session = Depends(get_db)
):
    return db_article.update_article(db, article_id, request)


@router.get("/{article_id}/delete")
def delete_article(article_id, db: Session = Depends(get_db)):
    return db_article.delete_article(db, article_id)
