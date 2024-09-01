from sqlalchemy import Column, Float, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class StatusEnum(str, enum.Enum):
    PENDING = "pending"
    WIN = "win"
    LOSE = "lose"

class Bet(Base):
    __tablename__ = "bets"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(String, index=True)
    amount = Column(Float, nullable=False)
    status = Column(Enum(StatusEnum), default=StatusEnum.PENDING)
