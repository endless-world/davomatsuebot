from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart


from tgbot.bot.keyboards.reply.buttons import generate_keyboard
from tgbot.bot.loader import dp, bot
from tgbot.models import BotUser


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

    # version 1: Django da hozir asinxron imkoniyat qo'shilgan, shuni methodlarini
    # ishlatsangiz bo'ladi 
    user, created = await BotUser.objects.aget_or_create(bot_id=message.from_user.id)
    user.username = message.from_user.username
    user.first_name = message.from_user.first_name
    user.last_name = message.from_user.last_name
    await user.asave()


    # print(user)
    keyboard = await generate_keyboard(message.from_user.id)
    # await message.answer(f"Salom, {message.from_user.full_name}!")
    await bot.send_message(message.chat.id, f"Salom, {message.from_user.full_name}!", reply_markup=keyboard)





    # version 2: bu eski usul. avval sync_to_async ga o'rab ishlatar edik
# from asgiref.sync import sync_to_async
    # user, created = await sync_to_async(BotUser.objects.get_or_create)(bot_id=message.from_user.id)
    # user.username = message.from_user.username
    # user.first_name = message.from_user.first_name
    # user.last_name = message.from_user.last_name
    # await sync_to_async(user.save)()