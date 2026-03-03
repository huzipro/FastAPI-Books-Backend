from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.schemas import UserSignUpModel
from src.auth.service import create_user

auth_router = APIRouter()

@auth_router.post('/signup')
async def create_user_account(user_info: UserSignUpModel, session: AsyncSession):
    pass