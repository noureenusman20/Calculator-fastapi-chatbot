from sqlalchemy import Column, Integer, String, Float
from database import Base

class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True)
    num1 = Column(Float, nullable=False)
    num2 = Column(Float, nullable=False)
    operation = Column(String, nullable=False)
    result = Column(String, nullable=False)
