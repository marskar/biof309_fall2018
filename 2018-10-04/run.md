# Many ways to run code in Python

## Running code inside of a file

1. Line by line
2. By selecting multiple lines
3. Using code cells in PyCharm or Spyder

```python

#%%
print("One way to start a code cell is with a comment that starts with #%%")

# %%
print("You can also start the comment like this # %%")

# In[
print("or with something similar the IPython console below: # In[")
```

## Running an entire code file

### In an IPython environment:
%run my_script.py

### In a shell environment:

#### On Mac/Linux
python my_script.py

#### On Windows
py my_script.py

## Running an entire project

1. Create a `__main__.py` file
2. Include code in the file, e.g. `print("Main!")`
3. Pass the entire project to `python` or `py` in a shell environment

Some advantages of this are:
You can zip the whole project and still run `__main__.py`
```bash
python -m zipfile -c my_project.zip my_project/*
python my_project.zip
```

You can publish the whole project to PyPI, pip install it, and then run `__main__.py`
```bash
pip install skippy
skippy
```
