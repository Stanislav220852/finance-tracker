from app.db.base import Base
from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped,relationship

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.transaction.model.model import TransactionModel
    from app.goal.model.model import GoalModel

class UserCreateModel(SQLAlchemyBaseUserTable,Base):
    __tablename__ = "users"
    
   
    transactions: Mapped[list["TransactionModel"]] = relationship(back_populates="user")

    goals: Mapped[list["GoalModel"]] = relationship(back_populates="user")