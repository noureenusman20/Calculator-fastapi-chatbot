from pydantic import BaseModel
from typing import Literal,Union

class Calculator(BaseModel):
    num1: float
    num2: float
    operation: Literal["+", "-", "*", "/"]
    result: Union[float, str] = None
