from fastapi import APIRouter
from fastapi.responses import FileResponse
from service.service import install_track
from db.database import SessionDep
from schemas.sc_schema import ScUrlSchema

sc_router = APIRouter(prefix="/api/soundcloud")

@sc_router.post("/install_track")
async def install_track_router(data : ScUrlSchema,db : SessionDep) -> FileResponse :
    url = data.url
    file_data = await install_track(url,db)
    return FileResponse(file_data["path"],media_type="audio/m4a",filename=file_data["file_name"])

    
        
    