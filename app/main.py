from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from models import Budget, User, Category

app = FastAPI()

@app.get("/budgets")
def list_budgets(session: Session = Depends(get_session)):
    statement = select(Budget)
    results = session.exec(statement)
    return results.all()

@app.post("/budgets")
def create_budget(budget: Budget, session: Session = Depends(get_session)):
    session.add(budget)
    session.commit()
    session.refresh(budget)
    return budget

@app.post("/budgets/{budget_id}/users/{user_id}")
def append_user_to_budget(budget_id: int, user_id: int, session: Session = Depends(get_session)):
    budget = session.get(Budget, budget_id)
    if not budget:
        raise HTTPException(status_code=404, detail="Budget not found")

    user = session.get(User, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user in budget.users:
        raise HTTPException(status_code=400, detail=f"User {user_id} is already associated with Budget {budget_id}")

    budget.users.append(user)
    session.commit()
    session.refresh(budget)
    session.refresh(user)
    return {"message": f"User {user_id} appended to Budget {budget_id}"}

@app.get("/categories")
def list_categories(session: Session = Depends(get_session)):
    statement = select(Category)
    results = session.exec(statement)
    return results.all()

@app.get("/categories/{category_id}")
def get_category(category_id: int, session: Session = Depends(get_session)):
    category = session.get(Category, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@app.post("/categories")
def create_category(category: Category, session: Session = Depends(get_session)):
    session.add(category)
    session.commit()
    session.refresh(category)
    return category

@app.put("/categories/{category_id}")
def update_category(category_id: int, updated_category: Category, session: Session = Depends(get_session)):
    category = session.get(Category, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    category.name = updated_category.name
    category.parent_id = updated_category.parent_id

    session.add(category)
    session.commit()
    session.refresh(category)
    return category

@app.delete("/categories/{category_id}")
def delete_category(category_id: int, session: Session = Depends(get_session)):
    category = session.get(Category, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    session.delete(category)
    session.commit()
    return {"message": f"Category {category_id} deleted"}