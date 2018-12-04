import pytest
import sys


def fun(x: int = 5) -> str:
    """Turns x into a string.
    :param x:
    :return: x as a string
    >>> fun() # no argument
    '5'
    >>> fun('a') # str argument
    'a'
    >>> fun(['a','b']) # list argument
    "['a', 'b']"
    """

    return str(x)


if __name__ == '__main__':
    pytest.main(args=[sys.argv[0]])

