from typing import List, Optional
from model import Book
from schema import BookCreate, BookUpdate
from fastapi import HTTPException

_books: List[Book] = []
_book_id_counter = 1

def get_all_books() -> List[Book]:
    return _books

def get_book_by_id(book_id: int) -> Book:
    for book in _books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

def add_book(book_data: BookCreate) -> Book:
    global _book_id_counter
    new_book = Book(id=_book_id_counter, **book_data.dict())
    _books.append(new_book)
    _book_id_counter += 1
    return new_book

def update_book(book_id: int, updates: BookUpdate) -> Book:
    book = get_book_by_id(book_id)
    updated_fields = updates.dict(exclude_unset=True)
    updated_book = book.copy(update=updated_fields)
    
    for i, b in enumerate(_books):
        if b.id == book_id:
            _books[i] = updated_book
            return updated_book

    raise HTTPException(status_code=404, detail="Book not found")  # Should never be reached

def delete_book(book_id: int) -> None:
    for i, book in enumerate(_books):
        if book.id == book_id:
            del _books[i]
            return
    raise HTTPException(status_code=404, detail="Book not found")
