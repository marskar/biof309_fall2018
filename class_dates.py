from datetime import datetime, timedelta
from typing import List, Iterable
from os import makedirs


def weekly_event(start: int, end: int, weekdays: Iterable[int]) -> List[str]:
    start_str, end_str = str(start), str(end)
    if not hasattr(weekdays, '__iter__'):
        weekdays = [weekdays]

    def parse_date(date_str):
        def remove_punc(string):
            return ''.join(char for char in string if char.isdigit())

        return datetime.strptime(remove_punc(date_str), '%Y%m%d').date()

    start_date, end_date = map(parse_date, [start_str, end_str])
    day_range = range(0, int((end_date - start_date).days) + 1)
    return [(start_date + timedelta(days=i)).strftime('%Y-%m-%d')
            for i in day_range
            if (start_date + timedelta(days=i)).weekday() in weekdays]


def make_folders(names: List[str]) -> str:
    try:
        any(map(makedirs, names))
        return f'Created {len(names)} folders.'
    except FileExistsError as e:
        return f'File already exists: {e}.'


cd = weekly_event(start=20180913, end=20181213, weekdays=[3])

make_folders(cd)

# tests
# cd = weekly_event(start = '2018-09-13', end = '2018-12-13', weekdays = 3)
# cd = weekly_event(start = '2018-09-13', end = '2018-12-13', weekdays = [3])
# cd = weekly_event(start = '2018-09-13', end = '2018-12-13', weekdays = (3))
# cd = weekly_event(start = '2018-09-13', end = '2018-12-13', weekdays = {3})
# cd = weekly_event(start = 20180913, end = 20181213, weekdays = [0, 3])
# cd = weekly_event(start = 20180913, end = 20181213, weekdays = (0, 3))
# cd = weekly_event(start = 20180913, end = 20181213, weekdays = {0, 3})
