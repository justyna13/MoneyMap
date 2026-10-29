from sqlmodel import SQLModel, Session
from database import engine
from models import Budget, User, Category, BudgetPlan, Expense
from datetime import date

def create_tables():
    SQLModel.metadata.create_all(engine)

def seed_data():
    with Session(engine) as session:
        user = User(email="test@example.com", hashed_password="hashedpassword")
        category = Category(name="Food")
        budget = Budget(year=2024, month=6)

        session.add(user)
        session.add(category)
        session.add(budget)
        session.flush()

        budget_plan = BudgetPlan(budget_id=budget.id, category_id=category.id, planned_amount=500.0)
        expense = Expense(budget_id=budget.id, category_id=category.id, amount=100.0, date=date(2024, 6, 1), description="Groceries")

        budget.users.append(user)

        session.add(budget_plan)
        session.add(expense)
        session.commit()
        session.refresh(user)
        session.refresh(category)
        session.refresh(budget)
        session.refresh(budget_plan)
        session.refresh(expense)


if __name__ == "__main__":
    create_tables()
    seed_data()