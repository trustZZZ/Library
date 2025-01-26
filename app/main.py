from secrets import token_bytes

from fastapi import FastAPI
from typing import Optional

from sqlalchemy.util import b64decode, b64encode

from app.users.router import router as users_router
from app.books.router import router as books_router


app = FastAPI()
app.include_router(users_router)
app.include_router(books_router)
