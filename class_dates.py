from datetime import datetime, timedelta
from typing import List
from os import makedirs

def class_dates(start: str, end: str) -> List[str]:
    def format_date(date_str):
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    start_date, end_date = map(format_date, [start, end])
    if start_date.weekday() == end_date.weekday():
        return [(start_date + timedelta(weeks=i)).strftime('%Y-%m-%d')
                for i in range(int((end_date - start_date).days / 7) + 1)]
    else:
        print(f'{start_date} and {end_date} are not on the same weekday!')

cd = class_dates(start = '2018-09-13', end = '2018-12-13')

def make_folders(names: List[str]) -> str:
    try:
        any(map(makedirs, names))
        return f'Created {len(names)} folders.'
    except FileExistsError as e:
        return f'File already exists: {e}.'

make_folders(cd)
