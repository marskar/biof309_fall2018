from . import Animal
from datetime import datetime
class Lion(Animal):
    def __init__(self, name, species = "Pantera leo", last_fed = datetime.now()):
        super().__init__(name, species, last_fed)
    def roar(self) -> str:
        return "Roar! " + super().say()