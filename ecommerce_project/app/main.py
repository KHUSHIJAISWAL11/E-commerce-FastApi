from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import List
from jose import JWTError, jwt
import environ
from . import models, schemas, crud, auth
from .database import SessionLocal, engine
import stripe

env = environ.Env()
# Reading the .env file
environ.Env.read_env()

app = FastAPI()

stripe.api_key = env("STRIPE_SECRET_KEY")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/register/", response_model=schemas.User)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):

    hashed_password = auth.get_password_hash(user.password)
    user.password = hashed_password
    return crud.create_user(db=db, user=user)


@app.post("/token/")
def login_for_access_token(form_data: schemas.UserLogin, db: Session = Depends(get_db)):
    user = auth.authenticate_user(
        db, username=form_data.username, password=form_data.password
    )
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)


@app.get("/products/", response_model=List[schemas.Product])
def get_products(db: Session = Depends(get_db)):
    return crud.get_products(db=db)


@app.post("/orders/", response_model=schemas.Order)
def create_order(
    order: schemas.OrderCreate,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme),
):
    user = auth.get_current_user(token, db)
    return crud.create_order(db=db, order=order, user_id=user.id)


@app.get("/orders/", response_model=List[schemas.Order])
def get_orders(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    user = auth.get_current_user(token, db)
    return crud.get_orders_by_user(db=db, user_id=user.id)


@app.post("/create-payment-intent/")
async def create_payment_intent(request: Request):
    data = await request.json()
    try:
        intent = stripe.PaymentIntent.create(
            amount=data["amount"],
            currency="usd",
            payment_method_types=["card"],
        )
        return {"client_secret": intent["client_secret"]}
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))


@app.get("/")
def read_root():
    return {"message": "E-commerce API is working!"}
