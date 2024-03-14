import json
import requests
from collections import deque
from config import MY_TOKEN

headers = {"Authorization": f"Bearer {MY_TOKEN}"}


# ? I---------------------------------------------------------------------------------
# todo:  This api take information about absent students in subject -----------
def attendance_list_api_call(ATTENDANCE_LIST_URL):
    response = requests.get(ATTENDANCE_LIST_URL, headers=headers)
    res = response.json()["data"]["items"]
    return res

    # attendance_list = []
    # for res_item in res:
    #     # print(type(res_item),res_item)
    #     attendance_list_item = {
    #         "subject_schedule": res_item["_subject_schedule"],
    #         "group_id": res_item["group"]["id"],
    #         "group_name": res_item["group"]["name"],
    #         "group_language": res_item["group"]["educationLang"]["name"],
    #         "subject_name": res_item["subject"]["name"],
    #         "subject_id": res_item["subject"]["id"],
    #         "subject_type": res_item["trainingType"]["name"],
    #         "subject_date": tspto_date(res_item["lesson_date"]),
    #         "student_id": res_item["student"]["id"],
    #         "student_name": res_item["student"]["name"],
    #         "employee_id": res_item["employee"]["id"],
    #         "employee_name": res_item["employee"]["name"],
    #         "education_year": res_item["educationYear"]["name"],
    #         "semester": res_item["semester"]["name"],
    #         "lesson_pair_id": int(res_item["lessonPair"]["name"]),
    #         "lesson_pair": res_item["lessonPair"]["start_time"] + "-" + res_item["lessonPair"]["end_time"],
    #         "absent_off": res_item["absent_off"],
    #     }
    #     attendance_list.append(attendance_list_item)

    # # print(attendance_list)
    

# attendance_list_api_call(ATTENDANCE_LIST_URL)


# ? II --------------------------------------------------------------------------------
# todo: This function takes a list of datas about only checked subjects----------

def attendance_control_list_api_call(ATTENDANCE_CONTROL_LIST_URL):
    response = requests.get(ATTENDANCE_CONTROL_LIST_URL, headers=headers)
    res = response.json()["data"]["items"]
    return res


# ? III ----------------------------------------------------------------
# todo: This function takes a list of all datas about schedule

def schedule_list_api_call(SCHEDULE_LIST_URL):
    response = requests.get(SCHEDULE_LIST_URL, headers=headers)
    res = response.json()["data"]["items"]
    return res


# ? ------------------------------------------------------------------
# todo Count the number of pages in the dataset
def count_pages(url):
    response = requests.get(url, headers=headers)
    res = response.json()["data"]["pagination"]["pageCount"]
    return res


# with open('schedule_list.json', 'w') as f:
#     json.dump(schedule_lists, f)
