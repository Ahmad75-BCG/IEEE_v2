from fastapi import FastAPI
from pydantic import BaseModel
from database.db_config import session_scope

app = FastAPI()

class EnergyRead(BaseModel):
    energy_kwh: float
    temperature: float
    occupancy: int
    level_source: int

@app.post("/ingest")
def ingest_data(data: EnergyRead):
    with session_scope() as session:
        # Add logic to save to PostgreSQL
        # ... logic to trigger real-time alerts if energy is too high ...
        return {"status": "success"}