from fastapi import FastAPI

from db_connection import create_timestamp, read_timestamps, update_timestamp, delete_timestamp
from model import TimestampCreate, Timestamp

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the CRUD API"}


@app.post("/timestamps/")
def create_timestamp_endpoint(timestamp: TimestampCreate):
    timestamp = create_timestamp(timestamp)
    return timestamp[0] if len(timestamp) > 0 else {}  # TODO: error handling, post failed


@app.get("/timestamps/")
def get_timestamps_endpoint():
    timestamps = read_timestamps()
    return {"timestamps": timestamps}


@app.put("/timestamps/")
def update_timestamp_endpoint(timestamp: Timestamp):
    timestamp = update_timestamp(timestamp)
    return timestamp[0] if len(timestamp) > 0 else {}


@app.delete("/timestamps/{timestamp_id}")
def delete_timestamp_endpoint(timestamp_id: int):
    timestamp_id = delete_timestamp(timestamp_id)
    return {"timestamp_id": timestamp_id}
