"""
Weekly task 5

Write a program that outputs whether or not today is a weekday. An example of running this program on a Thursday is given below.

$ python weekday.py
Yes, unfortunately today is a weekday.

An example of running it on a Saturday is as follows.

$ python weekday.py
It is the weekend, yay!

"""
from datetime import datetime
now = datetime.now()

print(now)