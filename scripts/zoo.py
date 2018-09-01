# Your first job as a freelance data scientist is to create an animal inventory for the national zoo.
# To really excel at this task, you will have to go beyond the [[built-in Python data types]] and build your own!

e.g. `list`, `tuple`, `set`, and `dict`. For more, check out the official [Python Tutorial](
    https://docs.python.org/3/library/stdtypes.html)

Python is a flexible, general-purpose language.

As such, Python offers many ways to complete tasks, including

- **functional programming** (FP) and
- **object-oriented programming** (OOP).

As its name suggests, the focus of FP is on [functions], while OOP solves problems by defining [data types].

# types in Python not only store data,
# but can also contain methods.
# For example, the [string] below has a [method] called [`upper`].
# Object-oriented programming solves problems by defining new data types and methods.

In this lesson, we'll learn about OOP principles as we work towards creating a new data type to

You may remember  methods
s = "Let's go to the zoo!"
"Let's go to the zoo!".upper()
"Let's go to the zoo!".upper
dir(1)
1.__class__
if __bool__:

class NationalZooAnimal:
    location = "National Zoo"

Lion = NationalZooAnimal


python.__name__
Snake.__name__
Lion.location
# Python is a flexible, general-purpose language that offers many ways to complete tasks. In addition to OOP, Python also supports **Functional Programming (FP)**. As its name suggests, the focus of FP is on [functions], while OOP combines data and tools to work data into [objects].
s.upper()
s.upper
class Snake:
    number_of_legs = 1

Snake.number_of_legs = 2
Snake.number_of_legs

python.number_of_legs
class Snake:
    def __init__(self):
        pass

class Snake:
    pass
python = Snake()

class Snake:
    names = set()
    def __init__(self, name):
        self.name = name
        Snake.names.add(self.name)

reina = Snake("Reina")
rhett = Snake("Rhett")

reina.name
Snake.names

reina = Snake("Reina", "Python regius")
rhett = Snake("Rhett", "Python reticulatus")
rex = Snake("Rex", "Python regius")

reina.names
reina.inventory

class Snake:
    names = set()
    inventory = {}
    def __init__(self, name, species):
        self.name = name
        self.species = species
        Snake.names.add(self.name)
        if self.species in Snake.inventory.keys():
            Snake.inventory[self.species] += 1
        else:
            Snake.inventory.update({self.species: 1})


class Snake:
    names = set()
    inventory = {}
    def __init__(self, name, species):
        self.name = name
        self.species = species
        Snake.names.add(self.name)
        if self.species in Snake.inventory.keys():
            Snake.inventory[self.species] += 1
        else:
            Snake.inventory.update({self.species: 1})
    def hiss(self):
        return f"Hisss! My name is {self.name} and I'm a {self.species}!"


class Snake:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def hiss(self):
        return f"Hisss! My name is {self.name} and I'm a {self.species}!"

reina = Snake("Reina", "Python regius")
rex = Snake("Rex", "Python regius")
rhett = Snake("Rhett", "Python reticulatus")

regal_python = Snake("Python regius")
rex.hiss()
Snake.hiss()

class Snake:
    names = set()
    inventory = {}
    def __init__(self, name, species):
        self.name = name
        self.species = species
        Snake.names.add(self.name)
        if self.species in Snake.inventory.keys():
            Snake.inventory[self.species] += 1
        else:
            Snake.inventory.update({self.species: 1})
    def hiss(self):
        return f"Hisss! My name is {self.name} and I'm a {self.species}!"
    def remove(self):
        Snake.names.remove(self.name)
        if Snake.inventory[self.species] > 1:
            Snake.inventory[self.species] -= 1
        else:
            Snake.inventory.pop(self.species)
    def replace(self):
        if self.name not in Snake.names:
            Snake.names.add(self.name)
            Snake.inventory[self.species] += 1
            return f"The current {self.species} count is {Snake.inventory[self.species]}"
        else:
            return f"{self.name} is already in the inventory"

reina = Snake("Reina", "Python regius")
rex = Snake("Rex", "Python regius")
rhett = Snake("Rhett", "Python reticulatus")

reina.inventory
reina.species
Snake.inventory
Snake.names

class Snake:
    names = set()
    inventory = {}
    def __init__(self, name, species):
        self.name = name
        self.species = species
        Snake.names.add(self.name)
        if self.species in Snake.inventory.keys():
            Snake.inventory[self.species] += 1
        else:
            Snake.inventory.update({self.species: 1})
    def hiss(self):
        return f"Hisss! My name is {self.name} and I'm a {self.species}!"
    def remove(self):
        Snake.names.remove(self.name)
        if Snake.inventory[self.species] > 1:
            Snake.inventory[self.species] -= 1
        else:
            Snake.inventory.pop(self.species)
    def replace(self):
        if self.name not in Snake.names:
            Snake.names.add(self.name)
            Snake.inventory[self.species] += 1
            return f"The current {self.species} count is {Snake.inventory[self.species]}"
        else:
            return f"{self.name} is already in the inventory"

class Snake:
    names = set()
    inventory = {}
    def __init__(self, name: str, species: str) -> None:
        self.name = name
        self.species = species
        Snake.names.add(self.name)
        if self.species in Snake.inventory.keys():
            Snake.inventory[self.species] += 1
        else:
            Snake.inventory.update({self.species: 1})
    def hiss(self) -> str:
        return f"Hisss! My name is {self.name} and I'm a {self.species}!"
    def remove(self) -> str:
        Snake.names.remove(self.name)
        if Snake.inventory[self.species] > 1:
            Snake.inventory[self.species] -= 1
            return f"The current {self.species} count  is {Snake.inventory[self.species]}"
        else:
            Snake.inventory.pop(self.species)
            return f"The species {self.species} was removed from the inventory"
    def replace(self) -> str:
        if self.name not in Snake.names:
            Snake.names.add(self.name)
            Snake.inventory[self.species] += 1
            return f"The current {self.species} count is {Snake.inventory[self.species]}"
        else:
            return f"{self.name} is already in the inventory"

# Old-style class definition

from datetime import datetime
class Animal:
    names = set()
    inventory = {}
    def __init__(self, name: str, species: str,
                 last_fed: datetime = datetime.now()):
        self.name = name
        self.species = species
        self.last_fed = last_fed
        if self.name not in Animal.names:
            Animal.names.add(self.name)
            if self.species in Animal.inventory.keys():
                Animal.inventory[self.species] += 1
            else:
                Animal.inventory.update({self.species: 1})
    def say(self) -> str:
        return f"My name is {self.name} and I'm a {self.species}!"
    @classmethod
    def len_names(cls) -> int:
        return len(cls.names)
    @classmethod
    def len_inventory(cls) -> int:
        return len(cls.inventory)
    @classmethod
    def sum_inventory(cls) -> int:
        return sum(cls.inventory.values())
    def remove(self) -> str:
        try:
            Animal.names.remove(self.name)
        except KeyError:
            return f"{self.name} was already removed!"
        if Animal.inventory[self.species] > 1:
            Animal.inventory[self.species] -= 1
            return f"The current {self.species} count is {Animal.inventory[self.species]}."
        else:
            Animal.inventory.pop(self.species)
            return f"The last {self.species} was removed from the inventory."
    def replace(self) -> str:
        if self.name not in Animal.names:
            Animal.names.add(self.name)
            Animal.inventory[self.species] += 1
            return f"The current {self.species} count is {Animal.inventory[self.species]}."
        else:
            return f"{self.name} is already in the inventory."
    def feed(self) -> str:
        self.last_fed = datetime.now()
        return "Yum!"
    def status(self) -> str:
        return f"{self.name} was last fed at {datetime.now() - self.last_fed}."

#You can think of a dataclass as a robot that writes code for you.

from datetime import datetime
from dataclasses import dataclass

@dataclass
class Animal:
    names = set()
    inventory = {}
    name: str
    species: str
    last_fed: datetime = datetime.now()
    def __post_init__(self):
        if self.name not in Animal.names:
            Animal.names.add(self.name)
            if self.species in Animal.inventory.keys():
                Animal.inventory[self.species] += 1
            else:
                Animal.inventory.update({self.species: 1})
    def say(self) -> str:
        return f"My name is {self.name} and I'm a {self.species}!"
    @classmethod
    def len_names(cls) -> int:
        return len(cls.names)
    @classmethod
    def len_inventory(cls) -> int:
        return len(cls.inventory)
    @classmethod
    def sum_inventory(cls) -> int:
        return sum(cls.inventory.values())
    def remove(self) -> str:
        try:
            Animal.names.remove(self.name)
        except KeyError:
            return f"{self.name} was already removed!"
        if Animal.inventory[self.species] > 1:
            Animal.inventory[self.species] -= 1
            return f"The current {self.species} count is {Animal.inventory[self.species]}."
        else:
            Animal.inventory.pop(self.species)
            return f"The last {self.species} was removed from the inventory."
    def replace(self) -> str:
        if self.name not in Animal.names:
            Animal.names.add(self.name)
            Animal.inventory[self.species] += 1
            return f"The current {self.species} count is {Animal.inventory[self.species]}."
        else:
            return f"{self.name} is already in the inventory."
    def feed(self) -> str:
        self.last_fed = datetime.now()
        return "Yum!"
    def status(self) -> str:
        return f"{self.name} was last fed at {datetime.now() - self.last_fed}."


reina = Animal("Reina", "Python regius")
rex = Animal("Rex", "Python regius")
leo = Animal("Leo", "Panthera leo")
rhett = Animal("Rhett", "Python reticulatus")

Animal.names
Animal.inventory

Animal.len_names()
Animal.len_inventory()
Animal.sum_inventory()
Animal.inventory

feeding_schedule = iter(Animal.names)
next(feeding_schedule)

reina.remove()
reina.replace()



