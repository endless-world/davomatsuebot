from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from tgbot.bot.filters.who_is import is_admin


async def generate_keyboard(user_id):
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True)
    if is_admin(user_id):
        keyboard.add(KeyboardButton("Kunlik"),KeyboardButton("Bugun"))
        keyboard.add(KeyboardButton("Davomat Umumiy"),KeyboardButton("1 oylik"))
    else:
        keyboard.add(KeyboardButton("Xato"), KeyboardButton("Kiribsiz"))
    return keyboard
