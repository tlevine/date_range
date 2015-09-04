from ..date_range import date_range

testcases = [
    (datetime.date(2015, 1, 1), datetime.date(2015, 1, 3),
        [datetime.date(2015, 1, 1), datetime.date(2015, 1, 2)]),
]

@pytest.mark.parametrize('left, right, output', testcases)
def test_date_range(left, right, output):
    assert list(date_range(left, right)) == output
