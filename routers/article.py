from typing import List

from sqlalchemy.orm import Session

from db import db_article
from db.database import get_db
from fastapi import APIRouter, Depends, status
from schemas import ArticleRequest, ArticleResponse

router = APIRouter(
    prefix="/article",
    tags=["Article"],
)


@router.post("/", response_model=ArticleResponse, status_code=status.HTTP_201_CREATED)
def create_article(request: ArticleRequest, db: Session = Depends(get_db)):
    return db_article.create_article(db, request)


@router.get("/", response_model=List[ArticleResponse])
def get_all_articles(db: Session = Depends(get_db)):
    return db_article.get_all_articles()


@router.get("/{article_id}", response_model=ArticleResponse)
def get_one_article(article_id: int, db: Session = Depends(get_db)):
    return db_article.get_one_article(db, article_id)


@router.post("/{article_id}/update", response_model=ArticleResponse)
def update_article(
    article_id: int, request: ArticleRequest, db: Session = Depends(get_db)
):
    return db_article.update_article(db, article_id, request)


@router.get("/{article_id}/delete")
def delete_article(article_id, db: Session = Depends(get_db)):
    return db_article.delete_article(db, article_id)
