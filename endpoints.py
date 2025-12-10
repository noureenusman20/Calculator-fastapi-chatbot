from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Calculation
from schemas import Calculator

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()
 
@router.post("/calculate")
def calculate(data: Calculator, db: Session = Depends(get_db)):
    if data.operation == "+":
        data.result = data.num1 + data.num2
    elif data.operation == "-":
        data.result = data.num1 - data.num2
    elif data.operation == "*":
        data.result = data.num1 * data.num2
    elif data.operation == "/":
        if data.num2 == 0:
            data.result = "Cannot divide by zero"
        else:
            data.result = data.num1 / data.num2
    else:
        data.result = "Invalid operator"

    # Save to database
    record = Calculation(
        num1=data.num1,
        num2=data.num2,
        operation=data.operation,
        result=str(data.result)
    )
    db.add(record)
    db.commit()
    db.refresh(record)

    
    return {
        "message": "Saved!",
        "data": {
            "num1": data.num1,
            "num2": data.num2,
            "operation": data.operation,
            "result": data.result
        },
        "id": record.id
    }
