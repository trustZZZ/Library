
from fastapi import APIRouter

from app.books.dao_main import LibraryDAO
from app.books.schemas import SBooks

router = APIRouter(
    prefix="/library",
    tags=["Библиотека"]
)

@router.get("")
async def get_books() -> list[SBooks]:
    result = await LibraryDAO.get_all()
    return result