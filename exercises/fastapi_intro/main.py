from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel

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
def list_categories(pagination: dict = Depends(common_pagination)):
    return pagination

@app.get("/expenses")
def list_expenses(pagination: dict = Depends(common_pagination)):
    return pagination

class Expense(BaseModel):
    name: str
    amount: float


@app.post("/expenses")
def create_expense(expense: Expense):
    return expense