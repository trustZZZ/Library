from fastapi import HTTPException, status

class LibraryException(HTTPException):

    status_code = 500 # <-- задаем значения по умолчанию
    detail = ""
    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)

class UserAlreadyExistsException(LibraryException):
    status_code=status.HTTP_409_CONFLICT
    detail="Пользователь уже существует"

class UserEmailPasswordInvalid(LibraryException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Отаказано в доступе. Неверный email или пароль"

class TokenExpireException(LibraryException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Время действия токена истекло"

class AuthException(LibraryException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Нет прав доступа"

class TokenExistingException(LibraryException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токена не существует"

class UserExistingException(LibraryException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Пользователь не найден"

class QuantityException(LibraryException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Превышено допустимое количество книг для получения"

class ExistingException(LibraryException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Совпадений не найдено"