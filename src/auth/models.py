from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String, DateTime, func
from src.books.base import Base
import uuid
from datetime import datetime


class User(Base):
    __tablename__ = 'users'
    uid: Mapped[uuid.UUID] = mapped_column(UUID (as_uuid=True), primary_key = True, default = uuid.uuid4)
    username: Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    first_name: Mapped[str] = mapped_column(String(30), nullable=False)
    last_name: Mapped[str] =  mapped_column(String(30), nullable=False)
    is_verified: Mapped[bool] = mapped_column(default=False)
    password_hash: Mapped[str] = mapped_column(deferred=True)
    created_at: Mapped[str] = mapped_column(DateTime(timezone=True), default = func.now())
    updated_at: Mapped[str] = mapped_column(DateTime(timezone=True), default = func.now(), onupdate = func.now())

    def __repr__ (self):
        return {"user": self.username,
                "email": self.email,
                }