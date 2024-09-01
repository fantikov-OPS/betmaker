import pytest
from httpx import AsyncClient
from app.main import app
from app.models import Base
from app.database import engine

@pytest.fixture(scope="module")
async def test_client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.fixture(scope="module")
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.mark.asyncio
async def test_create_bet(test_client: AsyncClient, init_db):
    response = await test_client.post("/bet", json={"event_id": "1", "amount": 100.00})
    assert response.status_code == 200
    assert response.json()["event_id"] == "1"

@pytest.mark.asyncio
async def test_read_bets(test_client: AsyncClient, init_db):
    await test_client.post("/bet", json={"event_id": "1", "amount": 100.00})
    response = await test_client.get("/bets")
    assert response.status_code == 200
    assert len(response.json()) == 1
