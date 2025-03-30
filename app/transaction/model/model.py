from app.db.base import Base
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.user.model.model import UserCreateModel
    from app.category.model.model import CatrgoryModel


class TransactionModel(Base):
    __tablename__ = "transaction"
    amount:Mapped[float]
    type:Mapped[str]
    date: Mapped[str]
    description:Mapped[str]
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        index=True
    )
    user: Mapped["UserCreateModel"] = relationship(back_populates="transactions")
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categry.id"),
        nullable=True
    )
    category: Mapped["CatrgoryModel"] = relationship(back_populates="transactions")