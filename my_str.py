"""Use pytest to check types and test examples in docstrings"""

import sys
from typing import Union, Iterable

import pytest


def my_str(x: Union[int, str, Iterable] = 5) -> str:
    """Turns x into a string.
    :param x:
    :return: x as a string
    >>> my_str() # no argument
    '5'
    >>> my_str('a') # str argument
    'a'
    >>> my_str(['a','b']) # list argument
    "['a', 'b']"
    """
    return str(x)


if __name__ == '__main__':
    pytest.main(args=sys.argv)
