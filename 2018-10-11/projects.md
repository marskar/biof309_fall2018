# Python Project Principles

## Modularity and Reusability

A project is a directory that contains project files.

Learning Goal: Establish principles to follow for all projects

Following the Modularity and Reusability Principles makes code easier to 
- read,
- organize, 
- maintain, 
- debug, and
- test.

## Modular versus Monolithic

The opposite of modular is monolithic.

A monolithic file could, for example, contain all project
- code,
- documentation, and
- output.

To get the benefits of modularity and the convenience of a single file:
1. start with small files and then
2. combine them into a larger file later on.

## Don't Repeat Yourself (DRY)

While working on a project, you may notice common patterns.

Don't repeat code! Reuse it!

One way to avoid code repetition is to define a function.

Defining the same function in multiple code files would be repetitive.

Instead, we will 
- save our function definitions in `modules` and 
- use the definitions in `scripts`.

## Scripts versus modules

Scripts and modules
- are plain-text files that
- have `.py` extensions and
- contain only Python code.

Scripts and modules differ in how and why they are used. 

| Verb   | Filetype | Goal             |
|--------|----------|------------------|
| Run    | Script   | Perform actions  |
| Import | Module   | Define objects   |

## Running Scripts

Scripts in data science projects are typically run in a particular order.

This order can be visualized as a diagram called a directed acyclic graph (DAG). 

![](https://ndownloader.figshare.com/files/13168322/preview/13168322/preview.jpg)

Each script
- handles one and only one step in the process
- imports the tools it needs from modules that are included in the project.

It is common to run scripts in a shell, for example Bash (Bourne again shell).

## Importing modules

1. Create a module named `say.py`, which uses the `def` statement to define a function called `hello`:
```python
def hello():
    print("Hello World!")
```

2. Create a script called `greet.py`, which imports the `say` module and calls the `hello` function:
```python
import say
say.hello()
```
3. Type `python greet.py` in a shell and press Enter.


## Running modules as scripts

It is possible for the same file to be used as both a module and a script.

To demonstrate this, add the code below to the end of `say.py`:
```python
if __name__ == '__main__':
    hello()
```

The code above calls the `hello` function only when `say` is run as a script. 

The `if` statement prevents `hello` from being called when `say` is imported as a module.

Adding `hello()` to `say.py` without the `if` statement, would make `greet.py` print `Hello World!` twice!. 

## Running projects

1. Make a directory (`mkdir`) called `my_project`
2. Create a copy (`cp`) of `say.py` called `__main__.py` 
3. Move (`mv`) `__main__.py` into `my_project`
4. Run the project like you would run a script

```bash
mkdir my_project
cp say.py __main__.py
mv __main__.py my_project
python my_project
```

You can zip the whole project and then run the zip file:
```bash
python -m zipfile -c my_project.zip my_project/*
python my_project.zip
```

The convenience of a single file without sacrificing modularity!
