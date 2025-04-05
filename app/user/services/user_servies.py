from app.user.model.user_model import UserModel
from app.db.engine import new_session

class UserServices:
    @classmethod
    async def add_user(cls,):
        async with new_session() as session:
            