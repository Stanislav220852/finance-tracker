from pydantic import BaseModel, EmailStr,Field


class UserRead(BaseModel):
    id:int


class UserCreate(BaseModel):
    name:str = Field(min_length=3,max_length=20)
    email:EmailStr
    password:str = Field(min_length=3,max_length=8)

class UserDefoult(UserCreate):
    is_active: bool = Field(default=False)
    is_superuser: bool = Field(default= False)
    is_verified: bool = Field(default=False)
    

class UserUpdate(BaseModel):
    name:str = Field(min_length=3,max_length=20)
    email:EmailStr
    password:str = Field(min_length=3,max_length=8)