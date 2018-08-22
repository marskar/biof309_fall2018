from datetime import datetime, timedelta
from typing import List


def weekly_event(start: int, end: int, weekdays: int,
                 input_format: str = '%Y%m%d',
                 output_format: str = '%Y-%m-%d') -> List[str]:
    """Fill in the dates between the start and end dates.

    Args:
        start: The first date in YYYYMMDD format or as per input_format.
        end: The last date in YYYYMMDD format or as per input_format.
        weekdays: The days of the week to include, 0 = Monday
                                                   1 = Tuesday
                                                   2 = Wednesday
                                                   3 = Thursday
                                                   4 = Friday
                                                   5 = Saturday
                                                   6 = Sunday
        input_format: the format of the dates in the start and end arguments
        output_format: the format of the dates in the output

    Returns:
        A list of dates in 'YYYY-MM-DD' format, or as per output_format.

    Examples:
        All arguments that do no have default values should be integers.
        `>>> weekly_event(start = 20180913, end = 20180917, weekdays = 1234560)`
        ['2018-09-13', '2018-09-14', '2018-09-15', '2018-09-16', '2018-09-17']
        All arguments that do no have default values can be strings.
        `>>> weekly_event('20180913', end = '20180917', weekdays = '03456')`
        Punctuations and whitespace in non-default string arguments are ignored.
        `>>> weekly_event('2018-09-13', '2018-09-17', weekdays = '0, 3, 4, 5')`
        The weekdays argument can be any iterable, e.g. list or range object.
        `>>> weekly_event(20180913, 20180917, weekdays = [0, 1, 2, 3, 4, 5, 6])`
        `>>> weekly_event(20180913, 20180917, weekdays = range(0, 7))`

    """

    def keep_digits(string):
        return ''.join(char for char in string if char.isdigit())

    def parse_date(date_str):
        return datetime.strptime(keep_digits(date_str), input_format).date()

    start_date, end_date = map(parse_date, [str(start), str(end)])
    day_range = range(0, int((end_date - start_date).days) + 1)

    if isinstance(weekdays, str):
        weekdays = [int(x) for x in list(keep_digits(weekdays))]
    if isinstance(weekdays, int):
        weekdays = [int(x) for x in list(str(weekdays))]

    return [(start_date + timedelta(days=i)).strftime(output_format)
            for i in day_range
            if (start_date + timedelta(days=i)).weekday() in weekdays]
