
from fastapi import APIRouter
from sqlalchemy import select

from app.books.models import Books
from app.dao_main import LibraryDAO

router = APIRouter(
    prefix="/library",
    tags=["Библиотека"]
)

@router.get("")
async def get_books():
    result = await LibraryDAO.find_by_id(model_id=1)
    return result