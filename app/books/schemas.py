from pydantic import BaseModel
from datetime import date

class SBooks(BaseModel):
    id: int
    name: str
    description: str
    date_published: date
    author_id: int
    genre: str
    quantity: int