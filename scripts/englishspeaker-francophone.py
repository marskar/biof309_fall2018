from dataclasses import dataclass

@dataclass
class EnglishSpeaker:
    first_name: str
    last_name: str

    def greet(self):
        print(f"Hello, my name is {self.last_name}... {self.first_name} {self.last_name}.")


@dataclass
class Francophone:
    name: str

    def greet(self):
        print(f"Bonjour, je suis {self.name}.")


def intro(speaker):
    speaker.greet()


agent007 = EnglishSpeaker(first_name="James", last_name="Bond")
oss117 = Francophone(name="Hubert Bonisseur de La Bath")

intro(agent007)
intro(oss117)