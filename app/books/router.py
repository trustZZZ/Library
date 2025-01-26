
from fastapi import APIRouter
from fastapi.params import Depends

# from app.books.dao_main import LibraryDAO
# from app.books.schemas import SBooks
# from app.users.dao import UsersDAO
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/library",
    tags=["Библиотека"]
)

@router.get("")
async def get_books(user: Users = Depends(get_current_user)): #-> list[SBooks]:
    # result = await UsersDAO.find_one_or_none()
    # return result
    print(user.email, user.id)