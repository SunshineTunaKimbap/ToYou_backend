from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class DB_props:
    instance = None
    def __init__(self):
        DATABASE_URL = "sqlite:///./sqlite_test.db"

        self.engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
        self.SessionLocal = sessionmaker(bind=self.engine, autocommit=False, autoflush=False)
        self.ModelBase = declarative_base()
        DB_props.instance = self

    def get_instance():
        if DB_props.instance == None:
            db = DB_props()
        return DB_props.instance

# Get database
def get_db():
    db = DB_props.get_instance().SessionLocal()
    try:
        DB_props.get_instance().ModelBase.metadata.create_all(bind=DB_props.get_instance().engine)
        yield db
    finally:
        db.close()

MODEL_BASE = DB_props.get_instance().ModelBase