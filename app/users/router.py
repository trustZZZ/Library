from typing import Literal

from ecdsa.test_malformed_sigs import params
from fastapi import APIRouter
from fastapi.params import Depends

from starlette.responses import Response


from app.exceptions import *
from app.users.auth import get_password_hash, authenticate_user, create_access_token
from app.users.dao import UsersDAO
from app.users.dependencies import get_role, get_role
from app.users.schemas import SUsers

router = APIRouter(
    prefix='/auth',
    tags=["Аутентификация"]
)

@router.post("/register")
async def register_user(user_data: SUsers):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password, role='user', quantity=0)

@router.post("/login")
async def login_user(response: Response, user_data: SUsers):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise UserExistingException
    access_token = create_access_token({"sub": f"{user.id}"})
    response.set_cookie("library_access_token", access_token, httponly=True)

@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie(key="library_access_token")

#Права администратора - может изменять роль пользователей по id
@router.post("/settings")
async def update_role(user_id: int, set_role: Literal['user', 'admin'], user_role = Depends(get_role)):
    if user_role == 'admin':
        existing_user = await UsersDAO.find_by_id(model_id=user_id)
        if not  existing_user:
            raise UserExistingException
        await UsersDAO.find_and_update(params={'role': set_role}, id=user_id)
    else: raise AuthException

@router.get("/get_users")
async def get_all_users(user_role = Depends(get_role)):
    result = await UsersDAO.get_all()
    return result
