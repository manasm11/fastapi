from sqlalchemy.orm import Session

from db.models import DbArticle
from schemas import ArticleRequest


def create_article(db: Session, request: ArticleRequest):
    article = DbArticle(
        title=request.title,
        content=request.content,
        published=request.published,
        user_id=request.creator_id,
    )
    db.add(article)
    db.commit()
    db.refresh(article)
    return article


def get_all_articles(db: Session):
    all_articles = db.query(DbArticle).all()
    return all_articles


def get_one_article(db: Session, id: int):
    article = db.query(DbArticle).get(id)
    return article


def update_article(db: Session, id: int, request: ArticleRequest):
    articles = db.query(DbArticle).filter(DbArticle.id == id)
    articles.update(
        {
            DbArticle.title: request.title,
            DbArticle.content: request.content,
            DbArticle.published: request.published,
            DbArticle.user_id: request.creator_id,
        }
    )
    db.commit()
    article = articles.first()
    db.refresh(article)
    return article


def delete_article(db: Session, id: int):
    article = db.query(DbArticle).get(id)
    db.delete(article)
    db.commit()
    return {"message": f"Article with id {id} deleted"}
