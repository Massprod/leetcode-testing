from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy_utils import database_exists, create_database

DB_URL = 'postgresql+psycopg2://postgres:2552@localhost:5432/leetbase'

engine = create_engine(DB_URL)

LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()


def get_session():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()
