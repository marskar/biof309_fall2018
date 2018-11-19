import doctest


def say(string: str = 'hello') -> None:
    """prints the provided string
    >>> say()
    hello
    >>> say('world')
    world
    """
    print(string)


if __name__ == '__main__':
    doctest.testmod(verbose=True)
    help(say)
    print(say.__annotations__)
    print(say.__doc__)
