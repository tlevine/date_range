import datetime

import pytest

from date_range import date_range

testcases = [
    (
        (datetime.date(2015, 1, 1), datetime.date(2015, 1, 3)),
        [datetime.date(2015, 1, 1), datetime.date(2015, 1, 2)]
    ),
    (
        (datetime.date(2015, 1, 1), datetime.date(2015, 1, 6), 2),
        [
            datetime.date(2015, 1, 1),
            datetime.date(2015, 1, 3),
            datetime.date(2015, 1, 5),
        ]
    ),
]

@pytest.mark.parametrize('args, output', testcases)
def test_date_range(args, output):
    assert list(date_range(*args)) == output
