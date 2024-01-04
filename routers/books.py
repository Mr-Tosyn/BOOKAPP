from fastapi import APIRouter
from schemas.book_schema import Book

books_router = APIRouter()

books = [
    Book(**{"title":"Harry Potter and the Philosopher's Stone", "author":"J. K. Rowlings"}),
    Book(**{"title":"Harry Potter and the Chambers of Secrets", "author":"Caleb Doxsey"})
    ]

@books_router.get("/")  
def get_books():
    return books 

@books_router.get("/{author}")
def get_books(author: str):
    for i in  books:
        if i.author == author:
            return i
    return {"error": "Author not found"}
    