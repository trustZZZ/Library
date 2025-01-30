from sqlalchemy import select, insert, update, delete
from sqlalchemy.dialects.mysql import insert
from typing import Generic, TypeVar
from app.database import async_session_maker, Base

T = TypeVar("T", bound=Base)

class BaseDAO(Generic[T]):

    model = type[T]

    #Поиск данных по фильтрам
    @classmethod
    async def find_one_or_none(cls, **filters):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filters)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def delete_by_id(cls, **filter_by):
        async with async_session_maker() as session:
            query = delete(cls.model).filter_by(**filter_by)
            await session.execute(query)
            await session.commit()

    #Добавление данных в БД
    @classmethod
    async def add(cls, **values):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**values)
            await session.execute(query)
            await session.commit()


    @classmethod
    async def find_by_id(cls, model_id: int) -> T:
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()


    @classmethod
    async def get_all(cls, skip: int = 0, limit: int = 10, **filters):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filters).limit(limit).offset(skip)
            library = await session.execute(query)
            result = library.scalars().all()
            return result

    @classmethod
    async def find_and_update(cls, params: dict, **filter_by):
        async with async_session_maker() as session:
            query = update(cls.model).filter_by(**filter_by).values(params)
            await session.execute(query)
            await session.commit()