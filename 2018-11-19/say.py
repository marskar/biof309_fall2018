import doctest


# Comments are good
def get_info_about(attr):
    """but docstrings are better"""
    return getattr(get_info_about, attr)


get_info_about('__doc__')


# Docstrings are better with examples
# Functions are better with type hints
def say(string: str = 'hello', multiple: int = 1) -> None:
    """prints the provided string multiple times
    >>> say()
    hello
    >>> say('world')
    world
    >>> say('world', 2)
    worldworld
    """
    print(string * multiple)

# Test the docstring examples when running the whole file
if __name__ == '__main__':
    doctest.testmod(verbose=True)
