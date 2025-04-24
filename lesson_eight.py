import datetime

now = datetime.datetime.now()

print(now)

current_date = datetime.date.today()

print(current_date)

print(dir(datetime))

d = datetime.date(2022, 12, 25)
print(d)

from datetime import date
todays_date = date.today()

print("Today's date =", todays_date)

timestamp = date.fromtimestamp(1426299364)
print("Date =", timestamp)

today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

from datetime import time

a = time()
print(a)

b = time(11, 34, 56)
print(b)

c = time(hour = 11, minute = 34, second = 56)
print(c)

d = time(11, 34, 56, 234566)
print(d)


a = time(11, 34, 56)

print("Hour =", a.hour)
print("Minute =", a.minute)
print("Second =", a.second)
print("Microsecond =", a.microsecond)

from datetime import datetime

a = datetime(2022, 12, 28)
print(a)

b = datetime(2022, 12, 28, 23, 55, 59, 342380)
print(b)


from datetime import datetime, date

t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)

t3 = t1 - t2

print("t3 =", t3)

t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 =datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print("t6 =", t6)

print("Type of t3 =", type(t3))
print("Type of t6 =", type(t6))

from datetime import timedelta

t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)

t3 = t1 - t2

print("t3 =", t3)

from datetime import timedelta

t = timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
print("Total seconds =", t.total_seconds())

from datetime import datetime

dt_string = "12/11/2018 09:15:32"

# Considering date is in dd/mm/yyyy format
dt_object1 = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
print("dt_object1 =", dt_object1)

# Considering date is in mm/dd/yyyy format
dt_object2 = datetime.strptime(dt_string, "%m/%d/%Y %H:%M:%S")
print("dt_object2 =", dt_object2)

from datetime import date

today = date.today()
print("Today's date:", today)

from datetime import date

today = date.today()
print("Today's date:", today)

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

import time

print("Printed immediately.")
time.sleep(2.4)
print("Printed after 2.4 seconds.")

import time

t = (2022, 12, 28, 8, 44, 4, 4, 362, 0)

result = time.asctime(t)
print("Result:", result)

# Output: Result: Fri Dec 28 08:44:04 2022

import json

person = '{"name": "Bob", "languages": ["English", "French"]}'
person_dict = json.loads(person)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
print( person_dict)

# Output: ['English', 'French']
print(person_dict['languages'])

import json

with open('path_to_file/person.json', 'r') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
print(data)

import json

person_dict = {"name": "Bob",
"languages": ["English", "French"],
"married": True,
"age": 32
}

with open('person.txt', 'w') as json_file:
  json.dump(person_dict, json_file)

  import json

  person_dict = {"name": "Bob",
                 "languages": ["English", "French"],
                 "married": True,
                 "age": 32
                 }

  with open('person.txt', 'w') as json_file:
      json.dump(person_dict, json_file)

