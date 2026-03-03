from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.books.schemas import BookModel, ReturnBookModel, UpdateBookModel,CreateBookModel
from src.books.service import bookService
from src.db.main import get_session
import uuid

book_router = APIRouter()
book_service = bookService()

@book_router.get('/', response_model = list[ReturnBookModel] )
async def get_all_books(session:AsyncSession = Depends(get_session)):
    books = await book_service.get_all_books(session)
    return books


@book_router.get('/{uid}', response_model = ReturnBookModel)
async def get_book_by_uid(uid: uuid.UUID, session:AsyncSession = Depends(get_session)):
    book = await book_service.get_book(uid, session)
    return book


@book_router.post('/', response_model = ReturnBookModel)
async def create_book(book:CreateBookModel, session:AsyncSession = Depends(get_session)):
    create_book = await book_service.create_book(book, session)
    return create_book
   

@book_router.delete('/{book_id}', response_model = ReturnBookModel)
async def delete_book(uid : uuid.UUID, session:AsyncSession = Depends(get_session)):
    del_book = await book_service.delete_book(uid, session)
    return del_book
   

@book_router.patch('/{uid}', response_model = ReturnBookModel)
async def update_book(uid: uuid.UUID , book_upd: UpdateBookModel, session:AsyncSession = Depends(get_session)):
    updated_book = await book_service.update_book(uid, book_upd, session)
    return updated_book