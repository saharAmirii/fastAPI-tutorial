from fastapi import FastAPI, status, HTTPException
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    print("Application startup")
    
    yield  

    print("Application shutdown")
   
app=FastAPI(lifespan=lifespan)

expenses=[]
id_counter=1

@app.post("/expenses", status_code=status.HTTP_201_CREATED)
def create_expense(description: str, amount:float):
    global id_counter
    new_id= id_counter
    id_counter+=1
    expense_obj = {"id": new_id, "description": description, "amount": amount}
    expenses.append(expense_obj)
    return expense_obj


@app.get("/expenses")
def get_all_expenses():
    return expenses

@app.get("/expenses/{id}")
def get_expense(id : int):
    flg = False
    for item in expenses:
        if item["id"] == id:
            flg = True
            return item
    if not flg:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Expense not Found")
    
@app.put("/expenses/{id}")
def edit_expense(id:int, description:str, amount:float):
    for item in expenses:
        if item["id"] == id:
            item["amount"] = amount
            item["description"] = description
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Expense not Found")


@app.delete("/expenses/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_expense(id:int):
    for item in expenses:
        if item["id"] == id:
            expenses.remove(item)
            return {"message" : "the expense deleted successfully"}
    raise HTTPException(status_code=404, detail="Expense not found")    
