from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

import uuid

from src.auth.models import User
from src.auth.schemas import UserSignUpModel
from src.auth.utils import verify_pw_hash, generate_pw_hash

class authService:

    async def get_users(self, session:AsyncSession):
        try:
            statement = select(User).order_by(User.username.desc())
            users_orm = await session.execute(statement)
            return users_orm.scalars().all()
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail = str(e))
        
    
    async def get_user_by_id(self, user_uid:uuid.UUID, session:AsyncSession ):
        try:
            user_orm =  await session.get(User, user_uid)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail = str(e))
        
        if not user_orm:
                raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'No user found with uid: {user_uid}' )
        return user_orm
    
        
    async def get_user_by_email(self, email:str, session:AsyncSession ):
        try:
            statement = select(User).where(User.email == email)
            user_orm = await session.execute(statement)
            user = user_orm.scalar_one_or_none()
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail = str(e))
        
        if not user:
                raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'No user found with wmail: {email}' )
        return user
    
    #Quiet helper function to just return none or user. 
    async def find_user_by_email(self, email:str, session:AsyncSession ):
         return await session.scalar(select(User).where(User.email == email))
         
        
    async def user_exists (self, email:str, session:AsyncSession):
        user = await self.find_user_by_email(email, session)
        return True if user is not None else False
        
    async def create_user(self, user_data: UserSignUpModel, session:AsyncSession):


        user_dict = user_data.model_dump()
        user_dict['password'] = generate_pw_hash(user_dict['password'])

        user_orm = User(**user_dict)
        session.add(user_orm)
        
        try:
            await session.commit()
            await session.refresh(user_orm)
       
        except Exception as e:
            await session.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail = str(e))
        
        return user_orm

    async def delete_user(self, user_uid: uuid.UUID, session:AsyncSession):

        user_orm = await session.get(User, user_uid)
             
        if not user_orm:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = 'No user found with this ')
        try:
            await session.delete(user_orm)
        except Exception as e:
            await session.rollback()
        return {"message": "User has been deleted",
                "detail": user_uid}
             



    