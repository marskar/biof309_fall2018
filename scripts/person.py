from datetime import date
from dataclasses import dataclass

@dataclass
class Person:
    first_name: str
    last_name: str
    birth_date: datetime

    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year

        if today < date(today.year,
                        self.birth_date.month,
                        self.birth_date.day):
            age -= 1

        return age

person = Person(
    "Jane",
    "Doe",
    date(1992, 3, 12) # year, month, day
)

person.age()
