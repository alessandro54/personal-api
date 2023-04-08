
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.engine.url import URL
import os

db_config = {
    "host": os.environ.get('DB_HOST', 'localhost'),
    "port": int(os.environ.get('DB_PORT', 3306)),
    "database": os.environ.get('DB_NAME', 'db'),
    "username": os.environ.get('DB_USER', 'root'),
    "password": os.environ.get('DB_PASSWORD', None),
    'drivername': 'mysql+mysqlconnector',
    'query': {'charset': 'utf8mb4'}
}

SQLALCHEMY_DATABASE_URL = URL(**db_config)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
