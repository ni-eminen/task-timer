from fastapi import FastAPI

from db_connection import create_timestamp, read_timestamps, update_timestamp
from model import TimestampCreate

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the CRUD API"}

@app.post("/timestamps/")
def create_timestamp_endpoint(timestamp: TimestampCreate):
    timestamp_id = create_timestamp(timestamp)
    return {"id": timestamp_id, **timestamp.dict()}

@app.get("/timestamps/")
def get_timestamps_endpoint():
    timestamps = read_timestamps()
    return {"timestamps": timestamps}

@app.put("/timestamps/{timestamp_id}")
def update_timestamp_endpoint(timestamp: TimestampCreate):
    timestamp = update_timestamp(timestamp)
    return {"timestamp": timestamp}
