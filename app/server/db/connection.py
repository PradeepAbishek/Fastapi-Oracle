from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import USER_NAME, PASSWORD, SERVER, DB_PORT, DIALECT, DATABASE_NAME


DATABASE_URL = DIALECT + "://" + USER_NAME + ":" + \
    PASSWORD + "@" + SERVER + ":" + DB_PORT + "/" + DATABASE_NAME

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
