import os
from tgbot.bot.filters.roles import admin_only
from tgbot.bot.handlers.utils.write_to_excel import write_data_to_excel
from tgbot.bot.handlers.utils.date_timestamp import get_str_date
from tgbot.bot.loader import bot,dp
from tgbot.models import Schedule
from datetime import datetime
from aiogram import types
from aiogram.dispatcher.filters import state



async def make_excel_file(message, data, file_name_key):
    data_list = [
        {
            'faculty_name': obj.faculty_name,
            'department_name': obj.department_name,
            'group_name': obj.group_name,
            'semester': obj.semester,
            'employee_name': obj.employee_name,
            'subject_name': obj.subject_name,
            'subject_type': obj.subject_type,
            'subject_date': obj.subject_date,
            'lesson_pair': obj.lesson_pair,
            'checked': obj.checked,

        }
        for obj in data
    ]
    # write to excel and take filepath
    # print("file_path: ", file_path)
    file_path = write_data_to_excel(
        data_list, file_name_key)

    try:
        # Ensure file exists before sending
        if not os.path.isfile(file_path):
            await message.answer("File not found!")
            return
        # send document to user
        # Open the file in binary read mode
        with open(file_path, 'rb') as file:
            document = types.InputFile(file)
            os.remove(file_path)
            await message.answer_document(document)
    except Exception as e:
        print(f"Error sending document: {e}")

@admin_only
async def today_handler(message, data=None):
    """Send today's schedule"""
    # today
    now = get_str_date(datetime.now())
    #  find today's datas from DB
    data = Schedule.objects.filter(subject_date=now)
    # If data is not exist, return message
    if data is None:
        await message.answer("Bu sanada hechnarsa yo'q")
        return
    

    await make_excel_file(message, data=data, file_name_key=f"{now[:2]}-{now[3:5]}-{now[6:]}")
    # write to excel and take filepath
    # print("file_path: ", file_path)
    # file_path = write_data_to_excel(
    #     data_list, f"{now[:2]}-{now[3:5]}-{now[6:]}")

    # try:
    #     # Ensure file exists before sending
    #     if not os.path.isfile(file_path):
    #         await message.answer("File not found!")
    #         return
    #     # send document to user
    #     # Open the file in binary read mode
    #     with open(file_path, 'rb') as file:
    #         document = types.InputFile(file)
    #         os.remove(file_path)
    #         await message.answer_document(document)
    # except Exception as e:
    #     print(f"Error sending document: {e}")


@admin_only
async def day_handler(message, data=None):
    
    text_data = message.text.lower()
    #  find today's datas from DB
    data = Schedule.objects.filter(subject_date=text_data)
    # If data is not exist, return message
    if data is None:
        await message.answer("Bu sanada hechnarsa yo'q.<br>Sanani <blockquote> kk/oo/yyyy </blockquote> shaklida kiritilganini tekshiring!")
        return
    await make_excel_file(message, data=data, file_name_key="Kunlik")
    # await state.finish()
