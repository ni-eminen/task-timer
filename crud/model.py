from pydantic import BaseModel

class TimestampCreate(BaseModel):
 topic: str
 start: bool
 timestamp: str

class Timestamp(TimestampCreate):
    id: int
