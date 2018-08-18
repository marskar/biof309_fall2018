from datetime import datetime, timedelta
from typing import List
from os import makedirs

def class_dates(start: str, end: str) -> List[str]:
    def format_date(date_str):
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    start_date, end_date = map(format_date, [start, end])
    weeks_int = int((end_date - start_date).days / 7)
    return [(start_date + timedelta(weeks=i)).strftime("%Y-%m-%d")
            for i in range(weeks_int+1)]

cd = class_dates(start = "2018-09-13", end = "2018-12-13")
print(cd)
any(map(makedirs, cd))