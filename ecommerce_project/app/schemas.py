from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True  

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class Product(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    stock_quantity: int

    class Config:
        from_attributes = True  

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock_quantity: int

class Order(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
    total_price: float  
    created_at: datetime

    class Config:
        from_attributes = True  
class OrderCreate(BaseModel):
    product_id: int
    quantity: int
    
class PaymentIntentRequest(BaseModel):
    amount:int