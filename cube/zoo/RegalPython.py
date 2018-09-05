from zoo import Animal
from datetime import datetime
class RegalPython(Animal):
    def __init__(self, name, species = "Python regius", last_fed = datetime.now()):
        super().__init__(name, species, last_fed)
    def hiss(self) -> str:
        return "Hiss! " + super().say()