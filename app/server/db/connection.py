from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import USER_NAME, PASSWORD, SERVER, DB_PORT, DIALECT, DATABASE_NAME, SQL_DRIVER


DATABASE_URL = DIALECT + '+' + SQL_DRIVER  + "://" + USER_NAME + ":" + \
    PASSWORD + "@" + SERVER + ":" + str(DB_PORT) + "/?service_name=" + DATABASE_NAME

engine = create_engine(DATABASE_URL, convert_unicode=False, pool_recycle=10,pool_size=50,echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
