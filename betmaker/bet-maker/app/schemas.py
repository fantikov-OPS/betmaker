from pydantic import BaseModel
from typing import Optional
import enum

class StatusEnum(str, enum.Enum):
    PENDING = "pending"
    WIN = "win"
    LOSE = "lose"

class BetBase(BaseModel):
    event_id: str
    amount: float

class BetCreate(BetBase):
    pass

class Bet(BetBase):
    id: int
    status: StatusEnum

    class Config:
        orm_mode = True
