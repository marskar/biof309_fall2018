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
        return f"My name is {self.name} and my species is {self.species}!"
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
        return f"{self.name} was last fed at {(datetime.now() - self.last_fed).strftime(%Y-%m-%d %H:%m)}."

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
        return f"My name is {self.name} and my species is {self.species}!"
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
        return f"{self.name} was last fed at {(datetime.now() - self.last_fed).strftime(%Y-%m-%d %H:%m)}."


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

class RegalPython(Animal):
    def __init__(self, name, species = "Python regius", last_fed = datetime.now()):
        super().__init__(name, species, last_fed)
    def hiss(self) -> str:
        return "Hiss! " + super().say()

class ReticulatedPython(Animal):
    def __init__(self, name, species = "Python reticulatus", last_fed = datetime.now()):
        super().__init__(name, species, last_fed)
    def hiss(self) -> str:
        return "Hiss! " + super().say()

class Lion(Animal):
    def __init__(self, name, species = "Pantera leo", last_fed = datetime.now()):
        super().__init__(name, species, last_fed)
    def roar(self) -> str:
        return "Roar! " + super().say()

leo = Lion("Leo")
leo.name
leo.species
leo.last_fed
leo.roar()

reina = RegalPython("Reina")
rex = RegalPython("Rex")
rhett = ReticulatedPython("Rhett")
rhett.hiss()
Animal.inventory
Animal.names
