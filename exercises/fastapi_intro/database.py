from sqlmodel import Relationship, SQLModel, Field, create_engine, Session


class Category(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    expenses: list["Expense"] = Relationship(back_populates="category")

class Expense(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    amount: float
    category_id: int = Field(foreign_key="category.id")
    category: Category = Relationship(back_populates="expenses")
    date: str | None = None


engine = create_engine("sqlite:///database.db")

def get_session():
    with Session(engine) as session:
        yield session