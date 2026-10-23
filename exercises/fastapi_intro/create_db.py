from database import Category, Expense, engine
from sqlmodel import SQLModel, Session, select


def create_tables():
    SQLModel.metadata.create_all(engine)

def seed_data():
    with Session(engine) as session:
        category = Category(name="food")
        expense = Expense(amount=10.2, category=category)
        session.add(category)
        session.add(expense)
        session.commit()
        session.refresh(category)
        session.refresh(expense)

def query_categories():
    with Session(engine) as session:
        statement = select(Category)
        results = session.exec(statement)
        print(results.all())

def query_category_with_expenses(category_name: str):
    with Session(engine) as session:
        statement = select(Category).where(Category.name == category_name)
        result = session.exec(statement).first()
        if result:
            print(category_name, result.expenses)

if __name__ == "__main__":
    create_tables()
    # seed_data()
    # query_categories()
    query_category_with_expenses("food")