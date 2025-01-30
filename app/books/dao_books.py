from sqlalchemy import select

from app.books.models import Books, Register
from app.dao.base import BaseDAO


class LibraryDAO(BaseDAO[Books]):
    model = Books

class RegisterDAO(BaseDAO[Register]):
    model = Register
