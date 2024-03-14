from aiogram import types

from tgbot.bot.handlers.users.admin_functions import today_handler
from tgbot.bot.loader import dp, bot


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    if 'bugun' in message.text.lower():
        await today_handler(message)
    else:
        await message.answer(message.text)
