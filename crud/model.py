from pydantic import BaseModel

class TimestampCreate(BaseModel):
 topic: str
 start: bool
 timestamp: float
 id_start_timestamp: int

class Timestamp(TimestampCreate):
    id: int
