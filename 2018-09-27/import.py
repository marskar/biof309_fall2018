# Two ways to import: import a module or import a function from a module
# If you import a module, you need to use it as a namespace with dot notation
# Use 'as' to alias a package name, e.g. import pandas as pd
# In normal mode, type gg to go to top, G to go bottom, 9gg or 9G to go to line 9
# ideavimrc: space is to run current line
# 50% takes you to the middle of a file
# ideavimrc: surround, e.g. ys$' to surround the rest of the line with '
# V selects a line, then you can expand the selection by moving around
# with multiple lines selected, press alt+shift+E to run multiple lines of code
import math # import math module
from math import sqrt # import a function
from math import pi # import an attribute
import numpy as np # follows convention
import pandas as pd # follows convention
from pandas import * # very NOT good idea
from pandas import DataFrame # generally not a good idea

math.sqrt # a function
math.pi # an attribute

sqrt(42)
pi

# fun imports
import this
import __hello__
from __future__ import braces
import antigravity

# Antigravity comic: https://xkcd.com/353/
# What does whitespace mean in the antigravity comic?
for i in range(10):
    print('a') # included in the loop
    print(i) # included in the loop
print('b') # not included in the loop
print(i) # not included in the loop

# What does it that Python is dynamically typed?
x = 5
x = '5'

# You can include type hints (optional, but helpful)
x: int =5
x: str ='5'
x

# print is a function in python 3, but a statement in python 2
print("Hello world")

# namespaces are useful
# The example below shows a name conflict with the list function
list = [1, 2, 3] # list variable conflicts with list function
list() # TypeError! 'list' object is not callable
del list # remove the list variable
list() # Should be ok now.
