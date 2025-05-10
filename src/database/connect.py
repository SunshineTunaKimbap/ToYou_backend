from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class DB_props:
    def __init__(self):
        DATABASE_URL = "sqlite:///./sqlite_test.db"

        engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
        SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
        ModelBase = declarative_base()
        ModelBase.metadata.create_all(bind=engine)

# Get database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()