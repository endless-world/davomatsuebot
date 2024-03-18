from aiogram import types

from tgbot.bot.handlers.states.schedule_states import ScheduleState
from tgbot.bot.handlers.users.admin_functions import day_handler, today_handler
from tgbot.bot.loader import dp, bot


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    if 'bugun' in message.text.lower():
        await today_handler(message)
    elif "kunlik" in message.text.lower():
        await message.answer("Iltimos, sanani <blockquote> kk/oo/yyyy </blockquote> shaklida kiriting")
        await ScheduleState.day.set()
        current_state = await state.get_state()
        print(f"Current state: {current_state}")

    else:
        await message.answer(message.text)


@dp.message_handler(state=ScheduleState.day)
async def echo_day(message: types.Message):
    await day_handler(message)
