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
        return f"{self.name} was last fed {round((datetime.now() - self.last_fed).total_seconds() / 60)} minutes ago at {self.last_fed.strftime('%H:%m')}."