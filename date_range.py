import datetime

def date_range(*args):
    '''
    range(stop) -> iterable of datetime.date objects
    range(start, stop[, step]) -> iterable of datetime.date objects
    '''
    if len(args) == 3:
        start, stop, step = args
        parsed_args = (start.toordinal(), stop.toordinal(), step)
    else:
        parsed_args = tuple(x.toordinal() for x in args)

    return map(datetime.date.fromordinal, range(*parsed_args))
