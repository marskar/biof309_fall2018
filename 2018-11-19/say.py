import doctest


# This only exists in the current file

def say(string: str = 'hello', mult: int = 1) -> None:
    """prints the provided string
    >>> say()
    hello
    >>> say('world')
    world
    >>> say('world', 2)
    worldworld
    """
    print(string * mult)


if __name__ == '__main__':
    doctest.testmod(verbose=True)
    help(say)
    print(say.__annotations__)
    print(say.__doc__)
