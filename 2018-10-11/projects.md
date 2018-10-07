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

The benefits of modularity with the convenience of a single file:
1. start with small files and then
2. combine them into a larger file later on.

## Don't Repeat Yourself (DRY)

While working on a project, you may notice common patterns.

Don't repeat code! Reuse it!

One way to deal with code repetition is to define a function.

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
| Import | Module   | Provide tools    |

## Running Scripts

Scripts in data science projects are typically run in a particular order.

This order can be visualized as a diagram called a directed acyclic graph (DAG). 

![](https://ndownloader.figshare.com/files/13168322/preview/13168322/preview.jpg)

1. Create a script named `greet.py`:
```python
print("Hello World!")
```
2. Run the script in a shell:
```bash
python greet.py
```

## Importing modules

1. Create a module named `say.py`, which uses the `def` statement to define a function called `hello`:
```python
def hello():
       print("Hello World!")
```

2. Edit the `greet.py` script to import the `say` module and call the `hello` function:
```python
import say
say.hello()
```
3. Run the `greet.py` script in a shell as before. 

## Running modules as scripts

It is possible for the same file to be used as both a module and a script.

Add the code below to `say.py`:
```python
if __name__ == '__main__':
    hello()
```
Now running `say.py` in a shell will also print "Hello World!".

The difference is that we can import the `hello` function from `say.py`, but not `greet.py`.

This approach works when we only want to call one function from a module.

## Running projects
1. Create a directory called `my_project`
2. Make a copy of `say.py` called `__main__.py` 
3. Move `__main__.py` into `my_project`
4. Run the project

```bash
mkdir my_project
cp say.py __main__.py
mv __main__.py my_project
python my_project
```

You can zip the whole project and run it:
```bash
python -m zipfile -c my_project.zip my_project/*
python my_project.zip
```

The convenience of a single file without sacrificing modularity!
