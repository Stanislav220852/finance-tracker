from enum import Enum

class TransactionType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"
    TRANSFER = "transfer"

class BudgetPeriod(str, Enum):
    DAY = "day"
    WEEK = "week"
    MONTH = "month"

class DebtType(str, Enum):
    DEBT = "debt"  # Мне должны
    LOAN = "loan"  # Я должен
