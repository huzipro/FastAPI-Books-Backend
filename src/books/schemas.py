from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional
import uuid

class BookModel(BaseModel):
    model_config = ConfigDict(from_attributes = True)
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: datetime
    page_count: int
    language: str
    created_at: datetime
    published_at: datetime
    isbn:str 

    

class UpdateBookModel(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    publisher: Optional[str] = None
    published_date: Optional[str] = None
    page_count: Optional[int] = None
    language: Optional[str] = None
    isbn:Optional[str] = None


class CreateBookModel(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: datetime
    page_count: int
    language: str
    isbn: str

class ReturnBookModel(BaseModel):
    model_config = ConfigDict(from_attributes = True)
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: datetime
    page_count: int
    language: str
    created_at: datetime
    isbn: str
    published_at: Optional[datetime] = None
