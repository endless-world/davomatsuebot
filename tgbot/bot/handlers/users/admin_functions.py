import os
from tgbot.bot.filters.roles import admin_only
from tgbot.bot.handlers.utils.write_to_excel import write_data_to_excel
from tgbot.bot.handlers.utils.date_timestamp import get_str_date
from tgbot.bot.loader import bot
from tgbot.models import Schedule
from datetime import datetime
from aiogram import types


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
    file_path = write_data_to_excel(data_list, f"{now[:2]}-{now[3:5]}-{now[6:]}")

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
