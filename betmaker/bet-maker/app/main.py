from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, models, schemas, database
from typing import List
import httpx

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/bet", response_model=schemas.Bet)
async def create_bet(bet: schemas.BetCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_bet(db, bet)

@app.get("/bets", response_model=List[schemas.Bet])
async def read_bets(db: AsyncSession = Depends(get_db)):
    return await crud.get_bets(db)

@app.get("/events")
async def get_events():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{LINE_PROVIDER_URL}/events")
    response.raise_for_status()
    return response.json()

@app.put("/events/{event_id}")
async def update_event(event_id: str, status: str):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{LINE_PROVIDER_URL}/events/{event_id}", json={"status": status})
    response.raise_for_status()
    return response.json()
