from db.database import session_maker,SessionDep
from db.models import ContentModel
from sqlalchemy import select,exists

async def send_content_data_to_db(url : str,path : str, db : SessionDep):
    content_data = ContentModel(url=url,path=path)
    db.add(content_data)
    await db.commit()


async def check_exists_content(url : str,db : SessionDep) -> bool:
    stmt = select(exists().where(ContentModel.url == url))
    res = await db.execute(stmt)
    is_exist = res.scalar()
    return is_exist or False

async def get_path(url : str,db : SessionDep) -> str:
    stmt = select(ContentModel.path).where(ContentModel.url==url)
    path = await db.execute(stmt)
    return path.scalar()

