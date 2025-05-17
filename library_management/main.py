from fastapi import FastAPI
from typing import List
from model import Book
from schema import BookCreate, BookUpdate
from service import (
    get_all_books,
    get_book_by_id,
    add_book,
    update_book,
    delete_book
)

app = FastAPI(
    title="Library Management API",
    version="1.0.0",
    description="Manage your library's books without a database."
)

@app.get("/books", response_model=List[Book])
def list_books():
    return get_all_books()

@app.get("/books/{book_id}", response_model=Book)
def retrieve_book(book_id: int):
    return get_book_by_id(book_id)

@app.post("/books", response_model=Book, status_code=201)
def create_book(book: BookCreate):
    return add_book(book)

@app.put("/books/{book_id}", response_model=Book)
def modify_book(book_id: int, book: BookUpdate):
    return update_book(book_id, book)

@app.delete("/books/{book_id}", status_code=204)
def remove_book(book_id: int):
    delete_book(book_id)
    return None
