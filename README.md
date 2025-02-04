# E-commerce API with FastAPI
-This is an e-commerce API built with FastAPI. It includes user registration, authentication, product management, order management, and payment processing using Stripe.

## Features

- User registration and authentication
- Product management (create, read)
- Order management (create, read)
- Payment processing with Stripe


## Requirements

- Python 3.8+
- FastAPI
- SQLAlchemy
- Stripe

## Setup

### 1. Clone the repository

```sh
git clone https://github.com/KHUSHIJAISWAL11/ecommerce-api.git
cd ecommerce-api

```
### 2 Create a virtual environment
```bash
python -m veve venv
-source venv/bin/activate
```
### 3 setup env variable
-DATABASE_URL=sqlite:///./test.db
-STRIPE_SECRET_KEY=your_stripe_secret_key
-STRIPE_PUBLISHABLE_KEY=your_stripe_publishable_key
### 4 run the application
```bash
uvicorn app.main:app --reload

```
### 5 Endpoints
```bash
http://127.0.0.1:8000.
```
## User Registration
-URL:/register
-Method:POST
-Request Body:
```bash
{
    "username": "testuser",
    "password": "testpassword"
}
```
-Response
```bash
{
    "id": 1,
    "username": "testuser"
}
```
## User Login
-URL:/token/
-Method:/POST
-Request Body:
```bash
{
    "username": "testuser",
    "password": "testpassword"
}
```
## Create Product
-URL: /products/
-Method: POST
-Request Body:
```bash
{
    "name": "Product 1",
    "description": "Description of product 1",
    "price": 100.0,
    "stock_quantity": 10
}
```
-Response
```bash
{
    "id": 1,
    "name": "Product 1",
    "description": "Description of product 1",
    "price": 100.0,
    "stock_quantity": 10
}
```
## Get Products
-URL: /products/
-Method: GET
-Response:
```bash
[
    {
        "id": 1,
        "name": "Product 1",
        "description": "Description of product 1",
        "price": 100.0,
        "stock_quantity": 10
    }
]
```
## Create Order
-URL: /orders/
-Method: POST
-Request Body:
```bash
{
    "product_id": 1,
    "quantity": 2
}
```
-Response
```bash
{
    "id": 1,
    "user_id": 1,
    "product_id": 1,
    "quantity": 2,
    "total_price": 200.0,
    "created_at": "2023-01-01T00:00:00"
}
```
## Get Order
-URL: /orders/
-Method: GET
-Response:
```bash
[
    {
        "id": 1,
        "user_id": 1,
        "product_id": 1,
        "quantity": 2,
        "total_price": 200.0,
        "created_at": "2023-01-01T00:00:00"
    }
]
```
## Create Payment Intent
-URL: /create-payment-intent/
-Method: POST
-Request Body:
```bash
{
    "amount": 2000  # Amount in cents (e.g., $20.00)
}
```
-Response
```bash
{
    "client_secret": "your_client_secret"
}
```









