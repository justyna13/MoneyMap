from sqlmodel import create_engine, Session
from models import Budget, Category, Expense, User, BudgetPlan, BudgetUserLink

engine = create_engine("sqlite:///moneymap.db")

def get_session():
    with Session(engine) as session:
        yield session   