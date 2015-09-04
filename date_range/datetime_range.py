import datetime

def date_range(left, right):
    return map(datetime.date.fromordinal, range(left.toordinal(), right.toordinal()))
