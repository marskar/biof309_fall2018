from dataclasses import dataclass

@dataclass
class ProgrammingLanguage:
    language_name: str
    creator_name: str
    created_year: int
    open_source: bool = True

python = ProgrammingLanguage("Python", "Guido van Rossum", 1991)

class ProgrammingLanguage:
    def __init__(self, language_name: str, creator_name: str,
                 created_year: int, open_source: bool = True):
        self.language_name =language_name
        self.creator_name = creator_name
        self.created_year = created_year
        self.open_source = open_source

python.created_year