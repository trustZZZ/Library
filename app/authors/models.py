from sqlalchemy import Column, Integer, String, DATE

from app.database import Base

class Authors(Base):
    __tablename__ = "authors"


    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    biography = Column(String, nullable=False)
    birthdate = Column(DATE, nullable=False)
