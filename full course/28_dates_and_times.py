"""The datetime module represents dates, times, and durations.
This example formats dates, parses date text, and calculates a future date.
"""

# Topic 28: Dates and times
# The datetime module provides date, time, and duration types.
from datetime import date, datetime, timedelta

today = date.today()
print("Today's date:", today)

now = datetime.now()
print("Current date and time:", now.strftime("%Y-%m-%d %H:%M"))

# Parse a date from text using its format.
birthday = datetime.strptime("2014-06-15", "%Y-%m-%d").date()
print("Birthday:", birthday.strftime("%B %d, %Y"))

# timedelta represents a duration that can be added to a date.
next_week = today + timedelta(days=7)
print("Date one week from now:", next_week)
