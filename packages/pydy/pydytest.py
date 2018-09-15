import pandas as pd
from pydy import pydy

def say_hi():
    print("Hi!")

say_hi()

pydy(['say_hi'])

say_hi()

pd.DataFrame.say_hi()
