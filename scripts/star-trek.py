from dataclasses import dataclass
@dataclass
class StarTrekCharacter:
    species: str = "Human"

# instantiate object with default attribute
kirk = StarTrekCharacter

# instantiate object and specify species attribute
spock = StarTrekCharacter(species="Vulcan")

# BONUS
# instantiate 2 objects with non-default attributes
# using tuple unpacking and list comprehension
spock, worf = [StarTrekCharacter(species = x)
               for x in ("Vulcan/Human", "Klingon")]
print(kirk.species, spock.species, worf.species)