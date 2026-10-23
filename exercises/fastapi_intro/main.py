from fastapi import FastAPI, HTTPException, Depends
from database import Category, Expense, get_session
from sqlmodel import Session, select

app = FastAPI()

def common_pagination(skip: int = 0, limit: int = 10):
    return { "skip": skip, "limit": limit }

@app.get("/")
def read_root() -> dict[str, str]:
    return { "message": "Hello" }

@app.get("/categories/{category_name}")
def get_category_details(category_name: str) -> dict[str, str]:
    if category_name not in ["jedzenie", "transport", "rozrywka"]:
        raise HTTPException(status_code=404, detail="Category not found")
    return { "category": category_name }

@app.get("/categories")
def list_categories(session: Session = Depends(get_session)):
    statement = select(Category)
    results = session.exec(statement)
    return results.all()

@app.get("/expenses")
def list_expenses(session: Session = Depends(get_session)):
    statement = select(Expense)
    results = session.exec(statement)
    return results.all()


@app.post("/expenses")
def create_expense(expense: Expense, session: Session = Depends(get_session)):
    session.add(expense)
    session.commit()
    session.refresh(expense)
    return expense


