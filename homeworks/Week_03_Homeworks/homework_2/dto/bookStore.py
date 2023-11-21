from pydantic import BaseModel, field_validator
from typing import List
from .bookItem import BookItem

class BookStore(BaseModel):
    name_of_bookstore:str
    book_shelve:List[BookItem]

    @field_validator("book_shelve")
    @classmethod    
    def check_book_shelve(cls, book_shelve: List[BookItem]):
        assert all(isinstance(book, BookItem) for book in book_shelve), "Item inside the Book Shelve is not a book, please store only books here."
        return book_shelve