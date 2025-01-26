from sqlalchemy import select

from app.books.models import Books
from app.dao.base import BaseDAO


class LibraryDAO(BaseDAO):
    model = Books

