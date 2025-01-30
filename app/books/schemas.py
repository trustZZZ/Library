from pydantic import BaseModel
from datetime import date

class SBooks(BaseModel):
    name: str
    description: str
    date_published: date
    author_id: int
    genre: str
    quantity: int

class SBooksChanges(BaseModel):
    name: str
    description: str
    date_published: date
    genre: str
    quantity: int