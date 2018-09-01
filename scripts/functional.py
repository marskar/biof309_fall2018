temps = [65, 32, 50, -2]

for i in range(len(temps)):
    temps[i] = round(((temps[i] - 32)/1.8), 1)
print(temps)

mins = 0
temp =110

while temp >=30:
    mins += 1
    temp *= 0.98
    print(temp, str(mins))

print.__call__()

callable(print)

print()

print("1st arg", "2nd arg", "3rd arg")
print("1st arg", "2nd arg", sep = ", ")
print(sep = ", ", "1st arg", "2nd arg")
print(sep='')
from math import sqrt
sqrt
from random import randint
import random as rd
lunch_choices = 'burrito', 'sushi', 'pasta'
lunch_choices[randint(0, 3)]
help(help)
import random as rd

randint = print("No longer a problem!")
lunch_choices[rd.randint(0, 3)]  # does not raise a NoneType Error

randint = print("Oops!")
lunch_choices[randint(0, 3)] # This produces a NoneType Error
lunch_choices = list(['burrito', 'sushi', 'pasta'])
list = ['burrito', 'sushi', 'pasta']
lunch_choices = list(lunch_choices)

print(*lunch_choices)
import random as rd, datetime as dt
import math
from datetime import date, time
date
math.

import random as rd
lunch_choice1, lunch_choice2, lunch_choice3 = x

lunch_choices = 'burrito', 'sushi', 'pasta'
d = {'sep': '\n', 'end': '!'}
print(*lunch_choices, **d)

rd.randint(0, 3)
restaurants = "Mexican", "Japanese", "Italian"
d = dict(zip(restaurants, lunch_choices))
lunch_spot = restaurants[rd.randint(0, 3)]
my_lunch = d[lunch_spot]
my_lunch

print()

def do_nothing:
    pass

def do_nothing(arg1):
    pass

do_nothing('pointless')

Remember args should come before kwargs.

lunch_choices = 'burrito', 'sushi', 'pasta'
print_options = {'sep': '\n', 'end': '!'}

def print_arg(arg):
    print(arg)

print_arg(1)

def print_args(*args):
    for arg in args:
        print(arg)

print_args(1, 2)


def print_kwargs(**kwargs):
    for kwarg in kwargs.items():
        print(kwarg)
# OR
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

print_kwargs(one=1, two=2)

d
lunch_choices = 'burrito', 'sushi', 'pasta'
print_options = {'sep': '\n', 'end': '!'}
print(*lunch_choices, **print_options)


def return_something():
    return 'something'

return_something()


def return_something():
    return 'something'


b = 1
def increment(a):
    return a + b

increment(1)

def pure_sum(a, b):
    return a + b

pure_sum(1, 1)


def fib(n: int):
    a, b = 0, 1
    for _ in range( n):
        yield a
        a, b = b, a + b

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

from typing import Generator


def generate() -> Generator[int, None, None]:
    for i in range(10):
        yield i
l = [i for i in generate()]
il = iter(l)
next(il)
generate.__annotations__
for i in fib(n=5):
    print(i)
a =fib()
next(a)
list(fib(5))
[*fib(5)]
[x for x in fib(n=5)]
[*fib(n=5)]
fib5_list
l
fib = fib()

del fib
fib().

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def infinite_fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

inf_fib = infinite_fib()

for i in fib(5):
    print(i)

print(*inf_fib)
for _ in range(5):
    print(next(inf_fib))

while _ < 5:
    print(next(inf_fib))

[x < 5 for x in inf_fib]
[next(inf_fib) for _ in range(5)]
list(next(inf_fib) for _ in range(5))

print("HI")
fib5 = fib(5)


def sum_args(*args):
    return sum(args)


pure_sum(1, 1)  # pure
sum_args(1, 1)  # pure

def arg_info(*args):
    return len(args), sum(args), max(args)
b=1
globals(b)
arg_info(1,2,3)

def arg_info(*args):
    return len(args), sum(args), max(args)

arg_info(1,2,3)


def arg_info(*args):
    return {'length': len(args), 'sum': sum(args), 'max': max(args)}


arg_info(1, 2, 3)

l = []

def create_list1(*args):
    for arg in args:
        l.append(arg)

create_list1(1, 2, 3)

l


def create_list2(*args):
    return [x for x in args]


create_list2(1, 2, 3)

append_to_list2(1, 2)


def pure_sum(a: int, b: int) -> int:
    """adds two ints together"""
    return a + b

locals()
help(pure_sum)
pure_sum.__annotations__
pure_sum.__closure__

print_arg(yes=1)

def many_prints(a, b):
    print(a)
    print(b)

many_prints('this', 'that')

def many_returns(a, b):
    return a
    return b

many_returns('yes', 'no')

def which_is_greater(a, b):
    if a > b:
        return a
    elif a == b:
        return 'Neither is greater'
    else:
        return b
which_is_greater(1, 2)

def which_is_greater2(a, b):
        return a if a > b else 'Neither is greater' if a == b else b

l_which_is_greater = lambda a, b: a if a > b else "Neither is greater" if a == b else b

l_which_is_greater.__doc__
l_which_is_greater(3, 2)
l_which_is_greater('z', 'b')

which_is_greater.__annotations__
which_is_greater2(3, 2)
which_is_greater2('z', 'b')

x = NaN

def snake_to_camel(s):
    return ''.join([w.capitalize() for w in s.split('_')])
import re
def camel_to_snake(s):
    return ''.join([w.lower() for w in s.split(re.findall())])

camelcase("snake_case")
