from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.database import Base

class Books(Base):
    __tablename__ = "library"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    date_published = Column(Date, nullable=False)
    author_id = Column(ForeignKey("authors.id"))
    genre = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)

class Register(Base):

    __tablename__ = "register"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey('users.id'))
    book_id = Column(ForeignKey('library.id'))
    issue_date = Column(Date)
    return_date = Column(Date)