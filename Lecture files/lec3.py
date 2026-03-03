from fastapi import FastAPI, HTTPException,status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://restfox.dev"],  # Allows all origins; change to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],  # Allows GET, POST, OPTIONS, etc.
    allow_headers=["*"],  # Allows all headers
)

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

class UpdateBook(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

book_collection: list[dict] = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publisher": "Charles Scribner's Sons",
        "published_date": "1925-04-10",
        "page_count": 218,
        "language": "English"
    },
    {
        "id": 2,
        "title": "1984",
        "author": "George Orwell",
        "publisher": "Secker & Warburg",
        "published_date": "1949-06-08",
        "page_count": 328,
        "language": "English"
    },
    {
        "id": 3,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publisher": "J.B. Lippincott & Co.",
        "published_date": "1960-07-11",
        "page_count": 281,
        "language": "English"
    },
    {
        "id": 4,
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "publisher": "Little, Brown and Company",
        "published_date": "1951-07-16",
        "page_count": 277,
        "language": "English"
    },
    {
        "id": 5,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "publisher": "T. Egerton",
        "published_date": "1813-01-28",
        "page_count": 279,
        "language": "English"
    },
    {
        "id": 6,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "publisher": "George Allen & Unwin",
        "published_date": "1937-09-21",
        "page_count": 310,
        "language": "English"
    },
    {
        "id": 7,
        "title": "Fahrenheit 451",
        "author": "Ray Bradbury",
        "publisher": "Ballantine Books",
        "published_date": "1953-10-19",
        "page_count": 194,
        "language": "English"
    },
    {
        "id": 8,
        "title": "Moby Dick",
        "author": "Herman Melville",
        "publisher": "Harper & Brothers",
        "published_date": "1851-10-18",
        "page_count": 635,
        "language": "English"
    },
    {
        "id": 9,
        "title": "War and Peace",
        "author": "Leo Tolstoy",
        "publisher": "The Russian Messenger",
        "published_date": "1869-01-01",
        "page_count": 1225,
        "language": "Russian"
    },
    {
        "id": 10,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "publisher": "HarperTorch",
        "published_date": "1988-01-01",
        "page_count": 208,
        "language": "Portuguese"
    }
]


@app.get('/books')
async def get_all_books():
    return book_collection


@app.get('/books/name/{book_name}')
async def get_all_books(book_name: str):
    """
    parameters: book_id == name of the book without spaces (since url)

    Output: Returns book object if it exists. Otherwise sends error
    """
    # match = [book for book in book_collection if "".join(book.model_dump()["title"].split(" ")) == book_id]
    match = [book for book in book_collection if "".join(book["title"].split(" ")).lower() == book_name.lower()]
    if match:
        return match
    else: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = 'Book not Found')
  

@app.post('/books')
async def create_book(book:Book):
    new_book = book.model_dump()
    if new_book in book_collection:
       raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = 'Book already exists')
    else:
        book_collection.append(book.model_dump())
        return (f'Book: {book.title} has been added')

@app.delete('/book/{book_id}')
async def delete_book(book_id:int):
    for book in book_collection:
        if book["id"] == book_id:
            book_collection.remove(book)
            return book
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'Book not found in list' )

@app.patch('/book/{book_id}')
async def update_book(book_id:int, book_upd:UpdateBook):
    for book in book_collection:
        if book["id"] == book_id:
            book["title"] = book_upd.title
            book["author"] = book_upd.author
            book["publisher"] = book_upd.publisher
            book["published_date"] = book_upd.published_date
            book["page_count"] = book_upd.page_count
            book["language"] = book_upd.language
            return {"Message": "Book Updated", "New Book": book}
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'Book not found in list' )  
    