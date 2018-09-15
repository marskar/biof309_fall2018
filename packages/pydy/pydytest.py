import pandas as pd
from pydy import pydy

def say_hi():
    print("Hi!")

say_hi() # this should work

pydy(['say_hi'])

say_hi() # this will not work

pd.DataFrame.say_hi() # this should work
