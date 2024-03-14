import datetime

def get_date(timestamp):
    # Convert timestamp to datetime object
    datetime_obj = datetime.datetime.fromtimestamp(timestamp)

    # Format the datetime object as day/month/year
    formatted_date = datetime_obj.strftime("%d/%m/%Y")

    return formatted_date

def get_str_date(date):
    # Output: "DD/MM/YYYY" (e.g., 13/03/2024)
    formatted_date_str = date.strftime("%d/%m/%Y")

    return formatted_date_str


def get_timestamp(dt):
    # Define your specific datetime
    # Year, month, day, hour, minute, second
    if dt["type"] == "today" or dt["type"] == "day":
        morning = datetime.datetime(
            dt["year"], dt["month"], dt["day"], 1, 0, 0)
        afternoon = datetime.datetime(
            dt["year"], dt["month"], dt["day"], 23, 59, 0)

        # Convert to timestamp
        morning_timestamp = int(morning.timestamp())
        afternoon_timestamp = int(afternoon.timestamp())
        # print("morning_timestamp:", morning_timestamp)
        # print("afternoon_timestamp:", afternoon_timestamp)

        return {"start_time": morning_timestamp, "end_time": afternoon_timestamp}

    elif dt["type"] == "month":
        pass
# {
#     "type": "today",
#     "year": 2024,
#     "month": 3,
#     "day": 2,
# }


# get_date(1647010200)
