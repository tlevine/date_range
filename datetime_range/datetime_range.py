import datetime

def datetime_range(left, right):
    return map(datetime.date.fromordinal, range(left.toordinal(), right.toordinal()))

def date_range(le
