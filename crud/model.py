from pydantic import BaseModel

class TimestampCreate(BaseModel):
 topic: str
 start: bool
 timestamp: float

class Timestamp(TimestampCreate):
    id: int
