from pydantic import BaseModel
from datetime import date

class SAuthors(BaseModel):
    id: int
    name: str
    biography: str
    birthdate: date

class SAuthorsChanges(BaseModel):
    name: str
    biography: str
    birthdate: date