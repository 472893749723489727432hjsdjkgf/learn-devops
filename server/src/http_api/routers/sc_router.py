from fastapi import APIRouter,Body
from fastapi.responses import FileResponse
from service.service import install_track

sc_router = APIRouter(prefix="/api/soundcloud")

@sc_router.post("/install_track")
async def install_track_router(data  = Body(embed=True)) -> FileResponse :
    url = data
    file_data = await install_track(url)
    return FileResponse(file_data["path"],media_type="audio/m4a",filename=file_data["file_name"])

    
        
    