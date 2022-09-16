from fastapi import HTTPException, Path, FastAPI
from internal.db.db import Database
from internal.models.models import PostAuthor
from internal.driver.driver import connect_DB

import psycopg2

app = FastAPI()

DB = Database()

conn = connect_DB()

DB.connect_to_db(conn)


@app.get("/books")
async def list_books():
    try:
        books = DB.get_all_books()
        return books
    except Exception as err:
        print(err)
        raise HTTPException(
            status_code=500, detail="error occured with the DB")


@app.get("/books/{id}")
async def get_book(id: int = Path(None, description="id of the book you want to view", gt=0)):
    try:
        book = DB.get_book(id)
        return book
    except Exception as err:
        if err == psycopg2.InternalError():
            raise HTTPException(
                status_code=500, detail="error occured with the DB")
        raise HTTPException(status_code=404, detail="book is not found")


@app.post("/authors")
async def create_author(author: PostAuthor):
    try:
        a = DB.new_author(author)
        return a
    except Exception as err:
        print(err)
        raise HTTPException(
            status_code=500, detail="error occured with the DB")


@app.get("/authors")
async def get_all_authors():
    try:
        authors = DB.list_authors()
        return authors
    except:
        raise HTTPException(
            status_code=500, detail="error occured with the DB")


@app.get("/authors/{id}")
async def get_authors(id: int = Path(None, description="id of the author you want to view", gt=0)):
    try:
        author = DB.get_author(id)
        return author
    except Exception as err:
        if err == psycopg2.InternalError:
            raise HTTPException(
                status_code=500, detail="error occured with the DB")
        print(err)
        raise HTTPException(status_code=404, detail="author is not found")
