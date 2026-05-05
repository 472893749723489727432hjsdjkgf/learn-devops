from .routers.bot_routers import sc_router
from .keyboards import kb
from db.database import init_tables
from config.config_bot import bot_settings
from aiogram import Bot,Dispatcher,types
from aiogram.filters import Command
import asyncio
import logging

logging.basicConfig(level=logging.INFO)
bot = Bot(token=bot_settings.API_TOKEN)

dp = Dispatcher()
 
dp.include_router(sc_router)

@dp.message(Command("start"))
async def cmd_start(message : types.Message):
    await message.answer("Бот для скачивания контента",reply_markup=kb)


async def main():
    await init_tables()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())