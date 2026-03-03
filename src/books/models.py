from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String, DateTime, Integer,Date,func
from datetime import datetime, date
from src.books.base import Base
import uuid


class Book(Base): 

    __tablename__ = "books"
    uid: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid = True), primary_key=True, default = uuid.uuid4) 
    title:Mapped[str] = mapped_column(String(100), nullable= False)
    author: Mapped[str] = mapped_column(String(100), nullable= False)
    publisher: Mapped[str] =  mapped_column(String(100), nullable= False)
    published_date: Mapped[date] = mapped_column(Date, nullable= False)
    page_count: Mapped[int] = mapped_column(Integer, nullable= False)
    language: Mapped[str] = mapped_column(String(20), nullable= False)
    isbn: Mapped[str] = mapped_column(String(40), nullable = False, unique = True, index=True )
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default = func.now(), nullable = False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default = func.now(), onupdate = func.now(),nullable = False)

    def __repr__ (self):
        return f"Book name: {self.title}, Author name: {self.author}"