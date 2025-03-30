from typing import TYPE_CHECKING
from app.db.base import Base
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey

if TYPE_CHECKING:
    from app.user.model.model import UserCreateModel


class GoalModel(Base):
    __tablename__ = "goal"
    target_amount:Mapped[float]
    current_amount:Mapped[float]
    deadline:Mapped[str]
    
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )
    user: Mapped["UserCreateModel"] = relationship(back_populates="goals")