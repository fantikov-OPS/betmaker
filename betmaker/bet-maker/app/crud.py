from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas

async def create_bet(db: AsyncSession, bet: schemas.BetCreate):
    db_bet = models.Bet(**bet.dict())
    db.add(db_bet)
    await db.commit()
    await db.refresh(db_bet)
    return db_bet

async def get_bets(db: AsyncSession):
    result = await db.execute(select(models.Bet))
    return result.scalars().all()
