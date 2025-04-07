from fastapi import APIRouter
from app.user.services.user_servies import UserServices
from app.user.schema.user_schema import UserSchem

user_router = APIRouter(
    prefix="user",
    tags=["user"]
)



@user_router.post("/")
async def add_user(schem:UserSchem):
    return await UserServices.add_user(schem=schem)


