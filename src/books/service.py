from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy import select, desc
from .schemas import CreateBookModel, ReturnBookModel, UpdateBookModel
from .models import Book
import uuid


class bookService:
     
    """
    Business logic layer for Book entity operations.
    Handles database interactions using SQLAlchemy AsyncSession.
    """
     
    async def get_all_books(self, session:AsyncSession) -> list[Book]:

        """
        Retrieves all books from the database ordered by creation date (desc).
        """

        statement = select(Book).order_by(desc(Book.created_at)) #returns all books from table Book (model maps to table) ordered descending by book.createdat 
        result = await session.execute(statement)
        if not result: 
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'No books found')
        return result.scalars().all()
    
    async def get_book(self, book_uid: uuid.UUID, session:AsyncSession) -> Book:
        
        """
        Retrieves a single book by its unique ID.
        Raises 422 if UID format is invalid, 404 if book not found.
        Returns book as dict
        """
        book_orm_obj = await session.get(Book, book_uid)

        if not book_orm_obj:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'Not found')
        
        return book_orm_obj
        

    async def create_book(self, book_data:CreateBookModel, session:AsyncSession):
        
        """
        Creates a new book record and persists it to the database.
        """

        create_book_orm = Book(**book_data.model_dump()) # Convert to ORM object.
        session.add(create_book_orm)
        await session.commit()
        await session.refresh(create_book_orm)
        return (create_book_orm)


    async def update_book(self, book_uid:uuid.UUID ,book_data:UpdateBookModel, session:AsyncSession):
        """
        Updates an existing book's fields. Only provided fields are updated.
        """
        
        update_book_orm = await session.get(Book, book_uid)

        if not update_book_orm:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail='No book with the uid provided was found')
        
        updates = book_data.model_dump(exclude_unset = True)

        for k,v in updates.items():
            setattr(update_book_orm, k, v)

        await session.commit()
        await session.refresh(update_book_orm)
        return update_book_orm    

       
    async def delete_book(self, book_id:uuid.UUID , session:AsyncSession):
        
        """
        Deletes a book from the database.
        """
       
        try:
            uid = uuid.UUID(book_id)
        except:
            raise HTTPException(status_code = status.HTTP_422_UNPROCESSABLE_CONTENT, detail = 'UID invalid')
        
        delete_book_orm = await session.get(Book, uid)

        if not delete_book_orm:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'No book with the uid provided was found')
        try:
            await session.delete(delete_book_orm)
            await session.commit()
            return 'Book Deleted'
        except Exception as e: 
            await session.rollback()
            raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete book")

    async def create_multiple_books(self, book_data:list[CreateBookModel], session:AsyncSession):
        try:
            for book in book_data:
                book_orm = Book(**book.model_dump)
                session.add(book_orm)
            await session.commit()
            return f'Successfully added {len(book_data)} books'
        except Exception as e:
            await session.rollback()
            raise HTTPException(status_code=status.HTTP, detail = {"message": "Error while creation.", "Error": str(e)})

