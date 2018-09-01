from dataclasses import dataclass

@dataclass
class ThingOnTheBus:
   name: str
   sound: str
    def sing(self):
        return f"The {self.name} on the bus go {self.sound}"

wheels = ThingOnTheBus("wheels", "round and round")

wheels.sing()

def sing(verse):
    return f"The {verse.name} on the bus go {verse.sound}"

sing(wheels)

class WipersOnTheBus:
    def go(self):
        print("Swish Swish Swish")

class BabiesOnTheBus:
    def go(self):
        print("Wah Wah Wah")

class MothersOnTheBus:
    def go(self):
        print("Shush Shush Shush")

def sing(verse):
    return f"The {verse.self.name} on the bus go {verse.self.sound}"

verse1 = WheelsOnTheBus()
sing(verse1)

