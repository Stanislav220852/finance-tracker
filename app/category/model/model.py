from app.db.base import Base
from sqlalchemy.orm import Mapped,relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.transaction.model.model import TransactionModel


class CatrgoryModel(Base):
    __tablename__ = "categry"
    name:Mapped[str]

    transactions: Mapped[list["TransactionModel"]] = relationship(
        back_populates="category",
        passive_deletes=True
    )