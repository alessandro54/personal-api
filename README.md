# Welcome to my personal API

This is a simple API that I use to store my personal data. It is a work in progress and I will be adding more features as I go along.

## How to use

### Install with Docker

1. Clone the repository
2. Run `docker-compose up -d`
3. Go to `localhost:8000` to see the API

### Install without Docker

1. Clone the repository
2. Run `pip install -r requirements.txt` with Python 3.11
3. Run `uvicorn main:app --reload`
4. Go to `localhost:8000` to see the API

## Migrations

To create a migration, run `alembic revision --autogenerate -m "message"`.

To apply a migration, run `alembic upgrade head`.
