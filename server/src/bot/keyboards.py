from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

keyboard = [
    [KeyboardButton(text="SoundCloud")],
]

kb = ReplyKeyboardMarkup(keyboard=keyboard,resize_keyboard=True)