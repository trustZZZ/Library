from sqlalchemy import Column, Integer, String, DATE, ForeignKey

from app.database import Base

class Books(Base):
    __tablename__ = "library"


    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    date_published = Column(DATE, nullable=False)
    author_id = Column(ForeignKey("authors.id"))
    genre = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
