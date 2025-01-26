from fastapi import FastAPI
from typing import Optional
from app.books.router import router as books_router


app = FastAPI()
app.include_router(books_router)

