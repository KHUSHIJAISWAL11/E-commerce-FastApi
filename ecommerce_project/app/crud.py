from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import  HTTPException, status
from datetime import datetime
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(models.User).filter(models.User.username == username).first()
    if user and user.password == password:
        return user
    return None

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()

def create_order(db: Session, order: schemas.OrderCreate, user_id: int):
    product = db.query(models.Product).filter(models.Product.id == order.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    total_price = product.price * order.quantity
    db_order = models.Order(
        user_id=user_id,
        product_id=order.product_id,
        quantity=order.quantity,
        total_price=total_price,
        created_at=datetime.utcnow()
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_orders_by_user(db: Session, user_id: int):
    orders = db.query(models.Order).filter(models.Order.user_id == user_id).all()
    for order in orders:
        if order.total_price is None:
            product = db.query(models.Product).filter(models.Product.id == order.product_id).first()
            order.total_price = product.price * order.quantity
            db.commit()
    return orders