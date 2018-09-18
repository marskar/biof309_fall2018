import pandas as pd
import pydy

def say_hi():
    print("Hi!")

say_hi() # this should work

pydy(['say_hi']) # this will remove functions from global namespace

say_hi() # this will not work

pd.DataFrame.say_hi() # this should work
