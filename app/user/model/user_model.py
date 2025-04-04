from app.db.base import Base
from pydantic import EmailStr
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey,String, Enum as SQLEnum
from datetime import date,datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.account.model.account_model import AccountModel
    from app.category.model.category_model import CategoryModel
    from app.transaction.model.transaction_model import TransactionModel
    from app.budget.model.budget_model import BudgetModel
    from app.debt.model.debt_model import DeptModel


class UserModel(Base):
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(1024))
    is_active: Mapped[bool] = mapped_column(default=True)
    is_premium: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime]


    transactions: Mapped[list["TransactionModel"]] = relationship(back_populates="user")
    accounts: Mapped[list["AccountModel"]] = relationship(back_populates="user")
    categories: Mapped[list["CategoryModel"]] = relationship(back_populates="user")
    budgets: Mapped[list["BudgetModel"]] = relationship(back_populates="user")
    debts: Mapped[list["DeptModel"]] = relationship(back_populates="user")