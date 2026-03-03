from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy import text
from src.config import Config
from src.books.models import Book
from src.books.base import Base
from typing import AsyncGenerator

async_engine = create_async_engine(
    url = Config.DATABASE_URL,
    echo = True)

async_session = async_sessionmaker(
    bind = async_engine, 
    class_ = AsyncSession,
    expire_on_commit = False
)

async def init_db():
    async with async_engine.begin() as conn:  #Context manager will automatically handle errors and closes. 
        await conn.run_sync(Base.metadata.create_all)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency that provides an async session for each request.
    Automatically closes the session after the request is finished.
    """
    async with async_session() as session:
        yield session
    
    
