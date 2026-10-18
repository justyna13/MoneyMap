from sqlmodel import SQLModel, create_engine, Session, Field, select

class Category(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str

class Expense(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    amount: float
    category_id: int = Field(foreign_key="category.id")


engine = create_engine("sqlite:///database.db")



def create_tables():
    SQLModel.metadata.create_all(engine)

def seed_data():
    with Session(engine) as session:
        category = Category(name="food")
        session.add(category)
        session.commit()
        session.refresh(category)

def query_categories():
    with Session(engine) as session:
        statement = select(Category)
        results = session.exec(statement)
        print(results.all())

if __name__ == "__main__":
    create_tables()
    seed_data()
    query_categories()