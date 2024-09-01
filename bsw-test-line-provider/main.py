from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

events = {}

class Event(BaseModel):
    id: str
    odds: float
    deadline: str
    status: str

@app.post("/events", response_model=Event)
async def create_event(event: Event):
    if event.id in events:
        raise HTTPException(status_code=400, detail="Event already exists")
    events[event.id] = event
    return event

@app.put("/events/{event_id}")
async def update_event(event_id: str, status: str):
    if event_id not in events:
        raise HTTPException(status_code=404, detail="Event not found")
    events[event_id].status = status
    return events[event_id]

@app.get("/events", response_model=List[Event])
async def list_events():
    return list(events.values())
