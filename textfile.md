The code below creates a text file called `zen.txt`.
```{python}
from this import s
from codecs import decode
with open('zen.txt', 'w') as f:
    f.write(decode(s, "rot-13"))
```

The standard approach to reading in files, as described in the [Python Tutorial](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files).
```{python}
with open('zen.txt') as f:
    my_list = [line for line in f]

with open('zen.txt') as f:
    my_string = f.readline()
```

Obtain the first line.
```{python}
my_list[0]
my_string.splitlines()[0]
```


Define functions to read in text.
```{python}
def read_list(file):
    with open(file) as f:
        return [line for line in f]

def read_str(file):
    with open(file) as f:
        return f.read()
```

Use functions to read in text.
```{python}
my_list = read_list('zen.txt')

my_string = read_str('zen.txt')
```

Create a class to represent text files
```{python}
class TextFile:
    count = 0
    def __init__(self, file: str) -> None:
        self.file = file

    def read(self) -> list:
        with open(self.file) as f:
            self.string = f.read()
        TextFile.count += 1

    def reset(self) -> None:
        del self.string
        TextFile.count -= 1
```

Create a class using dataclass decorator
```{python}
@dataclass
class TextFile:
    count = 0
    filename: str

    def read(self) -> list:
        with open(self.file) as f:
            self.string = f.read()
        TextFile.count += 1

    def reset(self) -> None:
        del self.string
        TextFile.count -= 1
```

Test the `TextFile` class
```{python}
zen = TextFile('zen.txt')
TextFile.count
zen.read()
TextFile.count
zen.string.splitlines()[0]
```

