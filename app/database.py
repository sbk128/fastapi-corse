from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

# SQLALCHEMY_DATABASE_URL = 'postgresql://<localhost>:<password>@<ip-address--or--hostname>/<database_name>'

# Below commented code is for establishing connections with database w/o sqlalchemy

# while True:
#     try:
#         conn = psycopg2.connect(host="localhost", database="fastapi", 
#                                 user="postgres", password="prathamesh",
#                                 cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was established!!!")
#         break
#     except Exception as error:
#         print("Failed to connect to Database")
#         print("Error: ", error)
#         time.sleep(2)

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()