from utils.main import main
from dateutil import rrule
from datetime import date

"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the mntury (1 Jan 1901 to 31 Dec 2000)?
"""


def number_of_mondays():
    start = date(1901, 1, 1)
    end = date(2000, 12, 31)
    count = 0

    for dt in rrule.rrule(rrule.MONTHLY, dtstart=start, until=end):
        if dt.weekday() == 6:
            count += 1

    return count

if __name__ == '__main__':
    main(number_of_mondays)
