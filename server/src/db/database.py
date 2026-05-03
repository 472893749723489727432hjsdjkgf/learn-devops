from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from config import settings

engine = create_async_engine(url=settings.URL)

session_maker = async_sessionmaker(bind=engine,expire_on_commit=False)

class Base(DeclarativeBase):
    pass


async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)



