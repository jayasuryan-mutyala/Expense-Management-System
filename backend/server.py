from fastapi import FastAPI,HTTPException
from datetime import date
from backend import db_helper 
from typing import List
from pydantic import BaseModel,field_validator


class Expense(BaseModel):
    # expense_date: date 
    amount: float
    category: str
    notes: str

    @field_validator("amount")
    @classmethod
    def amount_must_be_positive(cls,value):
        if value < 0:
            raise ValueError("Amount must be greater than or equal to zero")
        return value

    @field_validator("category")
    @classmethod
    def normalize_category(cls,value):
        return value.strip().title()

class DateRange(BaseModel):
    start_date: date 
    end_date: date

class MonthlyExpense(BaseModel):
    month: str
    total_expense: float

class CategoryExpense(BaseModel):
    category: str
    total_expense: float

class Category(BaseModel):
    category: str

app = FastAPI()

def server_error(message: str):
    raise HTTPException(
        status_code=500,
        detail={
            "error":"SERVER_ERROR",
            "message":message
        }
    )

# response model specifies the schema format
# we will only get the necessary fields we specified in BaseClass
@app.get("/expenses/{expense_date}",response_model=List[Expense])
def get_expenses(expense_date: date):
    expenses = db_helper.fetch_expenses_for_date(expense_date)
    if expenses is None:
       server_error(message="Failed to retrieve expenses from the database.")
    return expenses 

# Take serious note of the Python typehints because it can define how we send inputs from postman 

@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date,expenses: List[Expense]):
    try:
        db_helper.delete_expense(expense_date)

        for expense in expenses:
            db_helper.insert_expense(expense_date,
                                    expense.amount,
                                    expense.category,
                                    expense.notes)
        return {"message":"Expenses updated successfully"}
    
    except Exception as e:
        server_error(str(e))
    

@app.post("/analytics/")
def get_analytics(date_range: DateRange):
    data = db_helper.fetch_expense_summary(date_range.start_date,
                                    date_range.end_date)
    
    if data is None:
        return server_error(message="Failed to retrieve expense summary from the data")
    
    total = sum([row['total'] for row in data])

    breakdown = {}

    for row in data:
        percentage = (row['total']/total)*100 if total != 0 else 0
        breakdown[row['category']] = {
            "total":row['total'],
            "percentage":percentage
        }

    return breakdown

@app.get("/monthly_expense",response_model=List[MonthlyExpense])
def get_month_wise_expenses():
    data = db_helper.fetch_total_monthly_expense()

    if not data:
        raise HTTPException(
            status_code=404,
            detail={"error":"No monthly expense data found"}
        )
    
    return data 

@app.get("/categories/",response_model=List[Category])
def get_categories():
    data = db_helper.fetch_categories()

    if not data:
        raise HTTPException(status_code=404,
                            detail={"error":"No categories found"})
    return data


@app.get("/category_expense/{category}",response_model=List[CategoryExpense])
def get_category_wise_expenses(category: str):
    category = category.strip().title()
    data = db_helper.fetch_expense_by_category(category)

    if not data:
        raise HTTPException(status_code=404,
                            detail=f"No expenses found for category: {category}")
    return data

@app.get("/category_expense",response_model=List[CategoryExpense])
def get_total_expense_by_categories():
    data = db_helper.fetch_total_expense_by_category()
    if not data:
        raise HTTPException(status_code=404,
                            details="Unable to fetch expenses by category")
    return data



# note we are running from the project root 
# so we can run it like this 
# uvicorn backend.server:app --reload


