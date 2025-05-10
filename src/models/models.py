from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./sqlite_test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
ModelBase = declarative_base()

# Example model
class Letter(ModelBase):
    __tablename__ = "letter"
    id = Column(Integer, primary_key=True, index=True)
    name_sender = Column(String)
    abbr_sender = Column(String, index=True)
    abbr_receiver = Column(String, index=True)
    content = Column(String)
    content_secret = Column(String)
    pin = Column(String)
    design_id = Column(Integer)
