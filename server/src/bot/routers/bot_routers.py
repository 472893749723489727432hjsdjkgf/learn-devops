from aiogram import Router, types, F 
from aiogram.types import FSInputFile
from service.service import install_track
from db.database import get_session

sc_router = Router()

@sc_router.message(F.text == "SoundCloud")
async def cmd_get_url(message: types.Message):
    await message.answer("Отправь мне ссылку на трек")

@sc_router.message(F.text.contains("soundcloud.com"))
async def cmd_install_track(message: types.Message):
    async for session in get_session(): 
        data = await install_track(message.text, session)
        
        path = data["path"]
        file_name = data["file_name"]
        track = FSInputFile(path=path, filename=file_name)
        
        await message.answer_audio(
            track,
            caption="Вот твой трек!",
            performer="install sc bot",
            title=file_name
        )
        break
    

