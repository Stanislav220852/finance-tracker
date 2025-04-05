from pydantic import BaseModel,EmailStr,Field
from typing import Annotated

class UserSchem(BaseModel):
    name:Annotated[...,str]
    email:EmailStr
    hashed_password:Annotated[...,str]




class UserStatus(UserSchem):
    is_active:bool = Field(default=True)
    is_premium: bool = Field(default=False)
    