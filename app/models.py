from sqlmodel import SQLModel, Field, Relationship
from datetime import date

class BudgetUserLink(SQLModel, table=True):
    budget_id: int | None = Field(default=None, foreign_key="budget.id", primary_key=True)
    user_id: int | None = Field(default=None, foreign_key="user.id", primary_key=True)

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: str
    hashed_password: str
    budgets: list["Budget"] = Relationship(back_populates="users", link_model=BudgetUserLink)

class Category(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    parent_id: int | None = Field(default=None, foreign_key="category.id")

class Budget(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    users: list["User"] = Relationship(back_populates="budgets", link_model=BudgetUserLink)
    year: int
    month: int

class BudgetPlan(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    budget_id: int = Field(foreign_key="budget.id")
    category_id: int = Field(foreign_key="category.id")
    planned_amount: float

class Expense(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    budget_id: int = Field(foreign_key="budget.id")
    category_id: int = Field(foreign_key="category.id")
    amount: float
    date: date
    description: str | None = None
