from app.db.base import Base
from pydantic import EmailStr
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey,String, Enum as SQLEnum
from datetime import date,datetime
from typing import TYPE_CHECKING
from app.enum.enum import TransactionType
from app.enum.enum import DebtType

if TYPE_CHECKING:
    from app.account.model.account_model import AccountModel
    from app.category.model.category_model import CategoryModel
    from app.transaction.model.transaction_model import TransactionModel
    from app.budget.model.budget_model import BudgetModel
    from app.debt.model.debt_model import DeptModel
    from app.user.model.user_model import UserModel

class DeptModel(Base):
    amount: Mapped[float]
    type: Mapped[DebtType] = mapped_column(SQLEnum(DebtType))
    counterparty: Mapped[str] = mapped_column(String(100))
    due_date: Mapped[date]
    is_repaid: Mapped[bool] = mapped_column(default=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("usermodels.id"))
    account_id: Mapped[int] = mapped_column(ForeignKey("accountmodels.id"), nullable=True)

    user: Mapped["UserModel"] = relationship(back_populates="debts")
    account: Mapped["AccountModel"] = relationship()
    transactions: Mapped[list["TransactionModel"]] = relationship(back_populates="debt")