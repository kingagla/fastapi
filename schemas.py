from typing import List

from pydantic import BaseModel


class Article(BaseModel):
    title: str
    content: str
    published: bool

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article] = []

    class config:
        # użycie tego pozwala na konwertowanie między typami (z klasy db_user do tej klasy)
        from_attributes = True


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int


# user inside ArticleDisplay
class User(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True


class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User

    class Config:
        from_attributes = True
