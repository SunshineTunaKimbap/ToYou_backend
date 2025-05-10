from sqlalchemy import Column, Integer, String
from .connect import DB_props

# Example model
class Letter(DB_props.get_instance().ModelBase):
    __tablename__ = "letter"
    id = Column(Integer, primary_key=True, index=True)
    name_sender = Column(String)
    name_receiver = Column(String)
    abbr_sender = Column(String, index=True)
    abbr_receiver = Column(String, index=True)
    content = Column(String)
    content_secret = Column(String)
    pin = Column(String)
    design_id = Column(Integer)
