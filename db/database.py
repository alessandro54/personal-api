from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from pathlib import Path
import logging
import os
import re

try:
    models_path = str(Path(__file__).resolve().parents[1] / 'app/models')
    models = {model_file.split('.')[0]: getattr(__import__(f'app.models.{model_file.split(".")[0]}', fromlist=[model_file.split(".")[0]]), model_file.split(
    '.')[0].capitalize()) for model_file in os.listdir(models_path) if model_file.endswith('.py') and not model_file.startswith('__init__')}
except AttributeError as e:
    model_name = re.findall(r"'(.*?)'", str(e))[1]
    logging.critical(f'please create the {model_name} class inside the {model_name.lower()}.py model file')

finally:

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
