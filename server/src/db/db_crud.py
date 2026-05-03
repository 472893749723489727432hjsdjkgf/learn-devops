from db.database import session_maker
from db.models import ContentModel
from sqlalchemy import select,exists

async def send_content_data_to_db(url : str,path : str):
    content_data = ContentModel(url=url,path=path)
    async with session_maker.begin() as conn:
        conn.add(content_data)
        await conn.commit()


async def check_exists_content(url : str) -> bool:
    async with session_maker() as conn:
        stmt = select(exists().where(ContentModel.url == url))
        res = await conn.execute(stmt)
        is_exist = res.scalar()
        return is_exist or False

async def get_path(url : str) -> str:
    async with session_maker() as conn:
        stmt = select(ContentModel.path).where(ContentModel.url==url)
        path = await conn.execute(stmt)
        return path.scalar()

