from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class UserSignUpModel(BaseModel):
    username : str = Field(max_length = 10)
    email:str = Field(max_length = 255)
    first_name: str =  Field(max_length=30, min_len= 2)
    last_name: str = Field(max_length=30, min_len= 2)
    password: str

class UserReturnModel(BaseModel):
    model_config = ConfigDict(from_attributes = True)
    username : str = Field(max_length = 10)
    email:str = Field(max_length = 255)
    first_name: str = Field(min_length = 8)
    last_name: Optional[str] = None
    password: Optional[str] =  None