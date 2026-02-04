## ----- math module -----
# import math
# print(math.sqrt(9))
# print(math.factorial(5))
# radius = 7
# area = math.pi * radius ** 2
# print("Area of circle =", area)


## ----- datetime module -----
# import datetime
# now = datetime.datetime.now()
# today = datetime.date.today()
# past = today - datetime.timedelta(days=10)
# future = today + datetime.timedelta(days=10)

# print("Today :", today)
# print("Now :", now)
# print("10 days ago :", past)
# print("10 days later :", future)
# print("Year :", now.year)
# print("Month :", now.month)
# print("Day :", now.day)
# print("Day Name :", today.strftime("%A"))

import datetime
import calendar

day_names = datetime.date.today().weekday()
day_names =calendar.day_name[day_names]


## ----- random module -----
import random
print(random.randint(1, 6))
print(random.random())

# # Dice simulation
# dice = random.randint(1, 6)
# print("We rolled:", dice)

# # Number guessing game
print("Guess a number :",random.randint(1,10))


# ## ----- os module -----
import os
print("Current Working Directory:", os.getcwd())
print("Files and Folders in Directory:")
print(os.listdir())


# ## ----- sys module -----
import sys
print("Python Version:", sys.version)
print("Executable Path:", sys.executable)
print("Platform:", sys.platform)


# ## ----- platform module -----
import platform
print("Operating System:", platform.system())
print("Python Version:", platform.python_version())
print("Machine Type:", platform.machine())
print("Processor Info:", platform.processor())


# ## ----- time module -----
import time
print(time.ctime())
print("Wait for 2 seconds...")
time.sleep(2)
print("Done after 2 seconds!")