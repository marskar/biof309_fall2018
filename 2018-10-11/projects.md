# Python Project Principles

## Modularity and Reusability

A project is a directory that contains project files.

Learning Goal: Establish principles to follow for all projects.

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

The benefits of modularity with the convenience of a single file:
1. start with small code files called scripts and then
2. combine the scripts into a larger file later on.

## Python Scripts

Scripts
- are plain-text files that
- have `.py` extensions and
- contain Python code.

Scripts in data science projects are typically run in a particular order.

This order can visualized as a diagram called a directed acyclic graph (DAG). 

![](https://ndownloader.figshare.com/files/13168322/preview/13168322/preview.jpg)

## Don't Repeat Yourself (DRY)

While working on a project, you may notice common patterns.

Don't repeat code! Reuse it!

If code repeats in one file, we could define a function and use it throughout the file.

Defining the same function in multiple scripts would be repetitive.

Instead, we will save our function definition in a Python code file called a module.

Moving function definitions to modules -> smaller scripts.

## Scripts versus modules

Modules allow us to avoid code repetition, by making class and function definitions available throughout a project.

We can use the `import` statement to make the function definition available in each file that needs it.

Scripts and modules are similar in many ways, but differ in how and why they are used. 

| Action | Filetype | Goal                            |
|--------|----------|---------------------------------|
| Run    | Script   | Do things, e.g. create a plot   |
| Import | Module   | Define classes and/or functions |

## Importing modules

Inside of a directory called `my_project`, create 2 Python code files:

1. A module named `say.py`, which uses the `def` statement to define a function called `hello`:
```python
def hello():
    print("Hello World!")
```

2. A script named `greet.py`, which uses the `import` statement to import the `say` module:
```python
import say
```

## Running scripts

Right now, running `greet.py` will have no effect. 

To print "Hello World",

1. Add a function call to `greet.py`:
```python
import say
say.hello()
```

2. Run the `greet.py` script in a shell: 
```bash
python greet.py
```

## Running modules as scripts

It is possible for the same file to be used as both a module and a script.

Add the code below to `say.py`:
```python
if __name__ == '__main__':
    hello()
```
Now running `say.py` in a shell will also print "Hello World".

The difference is that we can import the `hello` function from `say.py`, but not `greet.py`.

This approach works best when we only want to call one function from a module.

## Running projects
1. Create a copy of `say.py` called `__main__.py` 
2. Go up one level in your folder system
3. Run the project

```bash
cp say.py __main__.py
cd ..
python my_project
```

You can zip the whole project and run it:
```bash
python -m zipfile -c my_project.zip my_project/*
python my_project.zip
```

The convenience of a single file without sacrificing modularity!
