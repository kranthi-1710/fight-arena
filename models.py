from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    character = Column(String, nullable=False)
    rating = Column(Integer, default=1000)
    created_at = Column(DateTime, default=datetime.utcnow)
