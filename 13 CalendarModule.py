import datetime
import calendar

date = input()

def findDay(date):
    day = datetime.datetime.strptime(date, '%m %d %Y').weekday()
    return (calendar.day_name[day])

print(findDay(date).upper())
