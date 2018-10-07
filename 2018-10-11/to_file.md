## An example of code repetition

Every script that produces a file might include
```python
with open(filename, 'w') as f:
    f.write(contents)
```

## The solution

Write and import a module:

1. Write a function named `to_file` that saves a Python object to a file:
```python
def to_file(filename, contents):
       with open(filename, 'w') as f:
           f.write(contents)
```
2. Save the function in a file called `my_module.py`.
3. Import the `to_file` function into every script that produces a file:
```python
import my_module
answer = "The answer to life is 42."
my_module.to_file('answer.txt', answer)
```
