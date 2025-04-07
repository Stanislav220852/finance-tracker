from annotated_types import MinLen,MaxLen
from pydantic import BaseModel,EmailStr,Field
from typing import Annotated


class UserSchem(BaseModel):
    name:Annotated[...,str,MinLen(3),MaxLen(30)]
    email:EmailStr
    hashed_password:Annotated[...,str]




class UserStatus(UserSchem):
    is_active:bool = Field(default=True)
    is_premium: bool = Field(default=False)
    