from datetime import datetime
from pydantic import BaseModel


class PostAuthor(BaseModel):
    first_name: str
    last_name: str


class Author:
    id: int
    first_name: str
    last_name: str
    created_at: datetime


class Book:
    id: int
    title: str
    author_id: int
    publication: str
    created_at: datetime


class Response:
    book_id: int
    book_title: str
    publication: str
    author_id: int
    author_first_name: str
    author_last_name: str
