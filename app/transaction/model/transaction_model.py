from app.db.base import Base
from pydantic import EmailStr
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey,String, Enum as SQLEnum
from datetime import date,datetime
from typing import TYPE_CHECKING
from app.enum.enum import TransactionType


if TYPE_CHECKING:
    from app.account.model.account_model import AccountModel
    from app.category.model.category_model import CategoryModel
    from app.transaction.model.transaction_model import TransactionModel
    from app.budget.model.budget_model import BudgetModel
    from app.debt.model.debt_model import DeptModel
    from app.user.model.user_model import UserModel



class TransactionModel(Base):
    amount: Mapped[float]
    type: Mapped[TransactionType] = mapped_column(SQLEnum(TransactionType))
    date: Mapped[datetime] = mapped_column(default=date.today())
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("usermodels.id"))
    account_id: Mapped[int] = mapped_column(ForeignKey("accountmodels.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("categorymodels.id"), nullable=True)
    debt_id: Mapped[int] = mapped_column(ForeignKey("debtmodels.id"), nullable=True)

    user: Mapped["UserModel"] = relationship(back_populates="transactions")
    account: Mapped["AccountModel"] = relationship(back_populates="transactions")
    category: Mapped["CategoryModel"] = relationship(back_populates="transactions")
    debt: Mapped["DeptModel"] = relationship(back_populates="transactions")