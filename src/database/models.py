from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .connect import DB_props

class ReceiverGroup(DB_props.get_instance().ModelBase):
    __tablename__ = "receiver_group"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

class Letter(DB_props.get_instance().ModelBase):
    __tablename__ = "letter"
    id = Column(Integer, primary_key=True, index=True)
    name_sender = Column(String)
    name_receiver = Column(String)
    abbr_sender = Column(String, index=True)
    abbr_receiver = Column(String, index=True)
    group_receiver_id = Column(Integer, ForeignKey("receiver_group.id"))
    design_id = Column(Integer)
    content = Column(String)
    content_secret = Column(String)
    pin = Column(String)

    group_receiver = relationship("ReceiverGroup")
