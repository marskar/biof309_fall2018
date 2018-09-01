from dataclasses import dataclass
@dataclass
class Employee:
    first_name: str
    last_name: str
    monthly_salary: float = 1234.56
    months_worked: int = 12
    def total_salary(self) -> float:
        return self.monthly_salary * self.months_worked
Employee.total_salary(Employee)

class Spider:
    species: str
    number_of_legs: int = 8
Spider.number_of_legs

from dataclasses import dataclass

@dataclass
class Company:
    name: str
    unit_price: float
    quantity_on_hand: int = 0
    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand

doug = Employee("Doug", "Smith", 500, 3)

doug.total_salary()
pants = InventoryItem("Pants", 40, 2)
pants.total_cost()

@dataclass
class ProgrammingLanguage:
    language_name: str
    creator_name: str
    year_created: int
    def info(self) -> str:
        return f"{self.language_name} was created in {self.year_created} by {self.creator_name}"
    def age(self) -> str:
        return f"{self.language_name} is {datetimeself.year_created} by {self.creator_name}"

py = ProgrammingLanguage("Python", "Guido van Russom", 1991)

landpy.info()

@dataclass
class Location:
    name: str
    longitude: float
    latitude: int

@dataclass
class City(Location):
    is_capital = False
    population: int

@dataclass
class Capital(City):
    is_capital = True
    capital_of: str

dc = Capital(name='Washington DC',
             longitude=-77.0,
             latitude=38.9,
             population=693972,
             capital_of='USA')

nyc = City(name='New York City',
           longitude=-73.9,
           latitude=40.7,
           population=8622698)

dc.is_capital
nyc.is_capital
issubclass(Capital,City)
dc.capital_of
isinstance(dc, Capital)
isinstance(dc, City)
isinstance(nyc, City)
