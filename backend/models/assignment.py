
from sqlalchemy import Column, Integer, String
from database.db import Base

class Assignment(Base):
    __tablename__ = "assignments"
    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String)
    deadline = Column(String)
    priority = Column(Integer)
