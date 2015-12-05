# Function receives two dates as arguments and returns delta between them in days
# I've used datetime module for solving this task
# *date1 - this trick replace received variable with date

from datetime import date, timedelta

def days_diff(date1, date2):
    return abs((date(*date1) - date(*date2)).days)