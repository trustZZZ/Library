import datetime
from fastapi.params import Depends
from fastapi import Request
from jose import JWTError
from jose import jwt

from app.config import settings
from app.exceptions import *
from app.users.dao import UsersDAO
from app.users.models import Users


def get_token(request: Request):
    token = request.cookies.get('library_access_token')
    if not token:
        raise TokenExistingException
    return token

async def get_current_user(token: str = Depends(get_token)):
    # Проверка
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except JWTError:
        raise UserEmailPasswordInvalid
    expire: str = payload.get("exp")

    # Проверка срока действия токена
    if (not expire) or (int(expire) < datetime.datetime.now(datetime.UTC).timestamp()):
        raise TokenExpireException

    user_id: str = payload.get("sub")
    user = await UsersDAO.find_by_id(int(user_id))
    if not user_id:
        raise UserExistingException

    return user.id

async def get_role(user_id: int = Depends(get_current_user)):
    user = await UsersDAO.find_by_id(model_id=user_id)
    return user.role