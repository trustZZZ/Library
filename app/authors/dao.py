from app.authors.models import Authors
from app.dao.base import BaseDAO

class AuthorsDAO(BaseDAO[Authors]):
    model = Authors