import datetime

from ecdsa.test_malformed_sigs import params
from fastapi import APIRouter
from fastapi.params import Depends

from app.books.dao_books import LibraryDAO, RegisterDAO
from app.books.schemas import SBooks, SBooksChanges
from app.exceptions import ExistingException, AuthException, QuantityException
from app.users.dao import UsersDAO

from app.users.dependencies import get_role, get_current_user

router = APIRouter(
    prefix="/library",
    tags=["Библиотека"]
)

#Получение списка книг
@router.get("/get_book_p{page}")
async def get_all_books():
    result = await LibraryDAO.get_all()
    return result

#Удалить книгу
@router.delete("/delete_book_{book_id}")
async def delete_book(book_id: int, role: str = Depends(get_role)):
    if role != 'admin':
        raise AuthException
    await LibraryDAO.delete_by_id(id=book_id)

#Добавить новую книгу
@router.post("")
async def add_book(values: SBooks, role: str = Depends(get_role)):
    if role != 'admin':
        raise AuthException
    await LibraryDAO.add(**values.model_dump())

#Изменить данные по книге
@router.post("/update_book_{book_id}")
async def update_book(params: SBooksChanges, book_id: int, role: str = Depends(get_role)):
    if role != 'admin':
        raise AuthException
    await LibraryDAO.find_and_update(params=params.model_dump(), id=book_id)

@router.post("/issue_book_{book_id}")
async def issue_book(book_id: int, user_id = Depends(get_current_user)):

    issue_quantity = await UsersDAO.find_one_or_none(id=user_id)
    book_quantity = await LibraryDAO.find_one_or_none(id=book_id)

    #Проверка наличия экземпляра книги у читателя
    book = await RegisterDAO.find_one_or_none(user_id=user_id, book_id=book_id)
    if book: # если такая книга уже есть у читателя, то вторая не выдается
        raise QuantityException

    #Проверка авторизован ли пользователь (по id пользователя) и есть ли книга с указанными id
    if (not issue_quantity) or (not book_quantity):
        raise ExistingException
    #Проверка наличия книг в библиотеке и доступного количества книг для одного читателя (<=5)
    if (issue_quantity.quantity == 0) or (book_quantity.quantity == 0):
        raise QuantityException

    #Если все ок, то добавляется запись в реестр библиотеки
    await RegisterDAO.add(
        user_id=user_id,
        book_id=book_id,
        issue_date=datetime.datetime.now().date(),
        return_date=(datetime.datetime.now() + datetime.timedelta(days=3)).date()
    )

    #Изменение количества экземпляров книги и выданных книг пользователю
    await LibraryDAO.find_and_update(params={"quantity": book_quantity.quantity - 1}, id=book_id)
    await UsersDAO.find_and_update(params={'quantity':issue_quantity.quantity - 1},id=user_id)


@router.post("/return_book_{book_id}")
async def return_book(book_id: int, user_id = Depends(get_current_user)):
    book = await RegisterDAO.find_one_or_none(user_id=user_id, book_id=book_id)
    issue_quantity = await UsersDAO.find_one_or_none(id=user_id)

    if not book:
        raise ExistingException
    await RegisterDAO.delete_by_id(user_id=user_id, book_id=book_id)
    book_data = await LibraryDAO.find_by_id(model_id=book_id)

    await LibraryDAO.find_and_update(params={"quantity": book_data.quantity + 1})
    await UsersDAO.find_and_update(params={'quantity': issue_quantity.quantity + 1}, id=user_id)


@router.get("/look_register_{user_id}")
async def look_register(user_id = Depends(get_current_user)):
    result = await RegisterDAO.get_all(user_id=user_id)
    return result