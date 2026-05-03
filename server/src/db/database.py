from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,async_session,AsyncSession
from sqlalchemy.orm import DeclarativeBase
from typing import Annotated
from fastapi import Depends
from config import settings

engine = create_async_engine(url=settings.URL)

session_maker = async_sessionmaker(bind=engine,expire_on_commit=False)

class Base(DeclarativeBase):
    pass


async def get_session():
    async with session_maker() as session:
        yield session


async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)



SessionDep = Annotated[AsyncSession,Depends(get_session)]