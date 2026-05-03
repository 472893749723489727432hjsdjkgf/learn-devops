from db.db_crud import send_content_data_to_db,get_path,check_exists_content
from db.database import SessionDep
from client.sc_client import ScClient
import os


async def install_track(url : str,db : SessionDep) -> dict[str,str]:
    if await check_exists_content(url,db):
        file_name = os.path.basename(await get_path(url,db))
        return {"path" :await get_path(url,db),
                "file_name" : file_name}
                
    client = ScClient(url)
    path = await client.install_video()
    await send_content_data_to_db(url,path,db)
    file_name = os.path.basename(path)
    return {"path" : path,
            "file_name" : file_name}
    

    