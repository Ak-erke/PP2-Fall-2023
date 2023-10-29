#task2
'''
from datetime import datetime, timedelta
new_date = datetime.now() - timedelta(days=5)

formatted_date = new_date.strftime("%Y-%m-%d")
print("Date 5 days ago:", formatted_date)
'''
#task2
'''
from datetime import datetime, timedelta

yesterday = datetime.now() - timedelta(days=1)
tomorrow = datetime.now() + timedelta(days=1)

print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", datetime.now().strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))
'''
#task3
'''
from datetime import datetime

datetime_without_microseconds = datetime.now().replace(microsecond=0)

print("Original DateTime:", datetime.now())
print("DateTime without Microseconds:", datetime_without_microseconds)
'''
#task4
from datetime import datetime

date_str1=input()
date_str2=input()
#date_str1 = "2023-10-01 12:00:00"
#date_str2 = "2023-10-01 12:30:30"

date_format = "%Y-%m-%d %H:%M:%S"
date1 = datetime.strptime(date_str1, date_format)
date2 = datetime.strptime(date_str2, date_format)

time_difference = (date2 - date1).total_seconds()

print(f"Time difference in seconds: {time_difference} seconds")





