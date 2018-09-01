import this
with open('zen.txt', 'w') as f:
    f.write("".join([this.d.get(c, c) for c in this.s]))


from this import s
from codecs import decode
with open('zen.txt', 'w') as f:
    f.write(decode(s, "rot-13"))

with open('zen.txt') as f:
    my_list = [line for line in f]

with open('zen.txt') as f:
    my_string = f.readline()

my_list
f = open('zen.txt')

for line in f:
    print(line, end='')

print(my_list[-0])

    return [line for line in f]

def file2list(filename):
    with open(filename, 'r') as f:
        return [line for line in f]

zen = file2list("zop.txt")

len(zen)

def file2list(file):
    with open(file) as f:
        return [line for line in f]

file2list("zen.txt")

class TextFile:
    def __init__(self, filename):
        self.file = file

    def read(self):
        self.lines = [line for line in self.file]


    def file2list(file):
        with open(file) as f:
            return [line for line in f]

TextFile.file2list("zen.txt")
print()

zen = TextFile('zen.txt')

print(zen.lines)

zen.read()

zen.zen = TextFile.file2list('zen.txt')
zen.zen


class SimplestPossibleClass:
    pass

example = SimplestPossibleClass

SimplestPossibleClass.ans
example.ans = 42
another = SimplestPossibleClass
another.ans

from dataclasses import dataclass

@dataclass
class TextFile:
    """Informative docstring"""
    count = 0
    filename: str

    def read(self) -> list:
        with open(self.filename) as f:
            self.lines = [line for line in f]
        TextFile.count += 1

    def reset(self) -> None:
        del self.lines
        TextFile.count -= 1

@dataclass
class ProgrammingLanguage:
    language_name: str
    creator_name: str
    created_year: int
    open_source: bool = True

python = ProgrammingLanguage("Python", "Guido van Rossum", 1991)
python
with open('zen.txt') as f:
    my_list = [line for line in f]


my_list = [line for line in open('zen.txt')]

@dataclass
class TextFile:
    file: str

    def read(self):
        with open(self.file) as f:
            self.lines = f.read()

TextFile.read = read
TextFile.read
zen.read()
zen = TextFile('zen.txt')
zen.read()
zen.lines.split('\n', 1)[0]

zen.lines.splitlines()[0]

zen.test = 0

TextFile.test

test = TextFile

test.test = 0


class textfile:
    def __init__(self, filename):
        self.file = file

class TextFile:
    count = 0
    def __init__(self, file: str) -> None:
        self.file = file

    def read(self) -> str:
        with open(self.file) as f:
            self.text = f.read()
        TextFile.count += 1

    def reset(self) -> None:
        del self.text
        TextFile.count -= 1

zen = TextFile('zen.txt')

zen.read()
TextFile.count
zen.text.splitlines()[0]
@dataclass
class TextFile:
    filename: str

    def read(self) -> list:
        with open(self.file) as f:
            self.string = f.read()
