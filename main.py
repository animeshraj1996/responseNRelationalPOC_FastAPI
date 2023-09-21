from fastapi import FastAPI
from models.author import Author
from models.book import Book
from database import engine
from sqlalchemy.orm import Session
from util.response_utility import create_api_response

app = FastAPI()


@app.post("/authors/", response_model=Author)
def create_author(author: Author):
    with Session(engine) as session:
        session.add(author)
        session.commit()
        session.refresh(author)
        return author


@app.post("/books/", response_model=Book)
def create_book(book: Book):
    with Session(engine) as session:
        session.add(book)
        session.commit()
        session.refresh(book)
        return book


@app.get("/books/{book_id}/author")
def get_author_of_book(book_id: int):
    with Session(engine) as session:
        book = session.query(Book).filter(Book.id == book_id).first()
        if not book:
            return create_api_response(False, [])
        return create_api_response(True, {"author": book.author, "book": book})
