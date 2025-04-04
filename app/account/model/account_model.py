from app.db.base import Base
from pydantic import EmailStr
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey,String, Enum as SQLEnum
from datetime import date,datetime
from typing import TYPE_CHECKING
from app.enum.enum import TransactionType
from app.enum.enum import DebtType
from app.enum.enum import BudgetPeriod

if TYPE_CHECKING:
    from app.account.model.account_model import AccountModel
    from app.category.model.category_model import CategoryModel
    from app.transaction.model.transaction_model import TransactionModel
    from app.budget.model.budget_model import BudgetModel
    from app.debt.model.debt_model import DeptModel
    from app.user.model.user_model import UserModel

class AccountModel(Base):
    name: Mapped[str] = mapped_column(String(100))
    currency: Mapped[str] = mapped_column(String(3))  # RUB, USD, EUR
    balance: Mapped[float] = mapped_column(default=0.0)
    is_archived: Mapped[bool] = mapped_column(default=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("usermodels.id"))