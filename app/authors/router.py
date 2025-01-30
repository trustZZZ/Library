from fastapi import APIRouter
from fastapi.params import Depends

from app.authors.dao import AuthorsDAO
from app.authors.schemas import SAuthors, SAuthorsChanges

from app.users.dependencies import get_role

router = APIRouter(
    prefix="/Authors",
    tags=["Авторы"])

@router.delete("")
async def delete_author(author_id: int, role: str = Depends(get_role)):
    if role:
        await AuthorsDAO.delete_by_id(id=author_id)

@router.post("")
async def add_author(values: SAuthors, role: str = Depends(get_role)):
    if role:
        await AuthorsDAO.add(**values.model_dump())

@router.post("")
async def update_author(params: SAuthorsChanges, author_id: int, role: str = Depends(get_role)):
    if role:
        await AuthorsDAO.find_and_update(**params.model_dump(), id=author_id)