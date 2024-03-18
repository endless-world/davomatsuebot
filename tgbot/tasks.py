from config import CONTROL_SCHEDULE_URL, SCHEDULE_URL
from tgbot.apis.get_apis import attendance_control_list_api_call, count_pages, schedule_list_api_call
from tgbot.models import Schedule, ScheduleChecked
from tgbot.bot.handlers.utils.date_timestamp import get_date
import time

# Write schedule list to Schedule Model object


async def write_schedule_db():
    schedule_pages = count_pages(SCHEDULE_URL)
    print(schedule_pages)

    for i in range(schedule_pages):
        if i % 50 == 0 and i != 0:
            print(i)
            # Pause for 15 seconds
            time.sleep(15)

        schedule_list = schedule_list_api_call(
            SCHEDULE_LIST_URL=f"{SCHEDULE_URL}&page={str(i+1)}")
        # print(f"Schedule_list- {len(schedule_list)} ta data oldim")

        for schedule_item in schedule_list:

            data = {
                'id': schedule_item["id"],
                'subject_id': schedule_item["subject"]["id"],
                'subject_name': schedule_item["subject"]["name"],
                'subject_type': schedule_item["trainingType"]["name"],
                'subject_date': get_date(schedule_item["lesson_date"]),
                'subject_date_tmp': schedule_item["lesson_date"],
                'semester': schedule_item["semester"]["name"],
                'education_year': schedule_item["educationYear"]["name"],
                'group_id': schedule_item["group"]["id"],
                'group_name': schedule_item["group"]["name"],
                'group_language': schedule_item["group"]["educationLang"]["name"],
                'lesson_pair_id': int(schedule_item["lessonPair"]["name"]),
                'lesson_pair': schedule_item["lessonPair"]["start_time"] +
                "-" + schedule_item["lessonPair"]["end_time"],
                'employee_id': schedule_item["employee"]["id"],
                'employee_name': schedule_item["employee"]["name"],
                'faculty_id': schedule_item["faculty"]["id"],
                'faculty_name': schedule_item["faculty"]["name"],
                'department_id': schedule_item["department"]["id"],
                'department_name': schedule_item["department"]["name"],
                'department_parent_id': schedule_item["department"]["parent"],
                'building': schedule_item["auditorium"]["building"]["name"],
                'room': schedule_item["auditorium"]["name"]
            }

            # Extract unique identifier field
            identifier = schedule_item["id"]

            # Attempt to get the object using the identifier
            obj, created = await Schedule.objects.aget_or_create(id=identifier, defaults=data)

            # Update object if it exists, otherwise the defaults will be used for creation
            if not created:
                for field, value in data.items():
                    setattr(obj, field, value)
                obj.save()

# ?----------------------------------------------------------------
# Write controlled schedule list to Controlled Schedule Model object


async def write_checked_schedule_db():
    checked_schedule = count_pages(CONTROL_SCHEDULE_URL)

    for i in range(checked_schedule):
        if i % 50 == 0 and i != 0:
            print(i)
            # Pause for 15 seconds
            time.sleep(30)

        checked_schedules = attendance_control_list_api_call(
            ATTENDANCE_CONTROL_LIST_URL=f"{CONTROL_SCHEDULE_URL}&page={str(i+1)}")

        for schedule_item in checked_schedules:

            data = {
                "id": schedule_item["id"],
                "schedule_id": schedule_item["_subject_schedule"],
                "subject_name": schedule_item["subject"]["name"],
                "subject_type": schedule_item["trainingType"]["name"],
                "subject_date": get_date(schedule_item["lesson_date"]),
                "subject_date_tmp": schedule_item["lesson_date"],
                "semester": schedule_item["semester"]["name"],
                "education_year": schedule_item["educationYear"]["name"],
                "group_name": schedule_item["group"]["name"],
                "lesson_pair": schedule_item["lessonPair"]["start_time"] +
                "-" + schedule_item["lessonPair"]["end_time"],
                "employee_name": schedule_item["employee"]["name"]
            }

            # Extract unique identifier field
            identifier = schedule_item["id"]
            print("identifier= ", identifier)
            # Attempt to get the object using the identifier
            obj, created = await ScheduleChecked.objects.aget_or_create( pk=identifier, defaults=data)
            print("obj= ", obj)
            print("created= ", created)

            # Update object if it exists, otherwise

            # Update object if it exists, otherwise the defaults will be used for creation
            if not created:
                for field, value in data.items():
                    setattr(obj, field, value)
                obj.save()
