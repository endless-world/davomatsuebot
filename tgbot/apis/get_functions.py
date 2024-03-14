from tgbot.apis.get_apis import schedule_list_api_call, attendance_control_list_api_call, count_pages
# from models import AbsentStudents, Schedule

# import xlsxwriter
import datetime
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")



# ATTENDANCE_LIST_URL = "https://talaba.tsue.uz/rest/v1/data/attendance-list?limit=200&lesson_date_from=1708905600&lesson_date_to=1709337599"

def get_schedule():
    schedule_pages = count_pages(SCHEDULE_LIST_URL)
    
    schedule_list = []
    for i in range(schedule_pages):
        schedule = schedule_list_api_call(
            SCHEDULE_LIST_URL=f"{SCHEDULE_LIST_URL}&page={str(i+1)}")
        schedule_list += schedule
    
    return schedule_list

def get_checked_schedule():
    checked_schedule = count_pages(ATTENDANCE_CONTROL_LIST_URL)

    checked_schedules_list = []
    for i in range(checked_schedule):
        checked_schedule = attendance_control_list_api_call(
            CHECKED_SCHEDULE_LIST_URL=f"{ATTENDANCE_CONTROL_LIST_URL}&page={str(i+1)}")
        checked_schedules_list += checked_schedule

    return checked_schedules_list