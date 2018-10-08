# Python Project Principles

## Learning Objectives

Learning Objectives: 
- Follow principles and best practices for working on Python projects.
- Use helpful technologies and techniques to save time and get better results!
- Write Python code and documentation that is organized and easy to 
    - read, 
    - use, 
    - maintain, and 
    - share. 

## What is a Project?

A project is a directory that contains project files.

Also, an opportunity to exercise empathy for anyone who might use your code (including your future self!)

Project files may be organized into subdirectories or kept at the top-level.

```
my_project
├── LICENSE
├── README.md
├── code
│   └── analysis.ipynb  <-  Not modular!
└── requirements.txt
```

First Python Project Principle: Modularity


## Modular versus Monolithic

The opposite of modular is monolithic.

A monolithic file, like `analysis.ipynb`, could contain all project 
- code, 
- documentation, and 
- output. 

To get the benefits of modularity and the convenience of a single file: 
1. start with small files and then 
2. combine them into a larger file later on. 

## Don't Repeat Yourself (DRY)

While working on a project, you may notice common patterns.

Reusability Principle: Don't repeat code! Reuse it! 

One way to avoid code repetition is to 
- define a block of reusable code called a function, and 
- replace the repetitive code with function calls. 

To further improve the modularity and reusability of our code, we will 
- define functions in `modules` and 
- use the functions in `scripts`. 

## Scripts versus modules

Scripts and modules
- are plain-text files that
- have `.py` extensions and
- contain only Python code.

Scripts and modules differ in how and why they are used.

| Filetype | Verb   | Goal             |
|----------|--------|------------------|
| Script   | Run    | Perform actions  |
| Module   | Import | Define objects   |

## Running Scripts

Scripts in data science projects are typically run in a particular order.

This order can be visualized as a diagram called a directed acyclic graph (DAG). 

![](https://assets.datacamp.com/production/repositories/3687/datasets/3d4fdb37d0924a05ab75fcc786dc590b33dbbf4b/simple_dag.png) 

Each script 
- handles one and only one step in the process 
- imports the tools it needs from modules that are included in the project. 

## Importing modules

1. Create a module named `say.py`, which uses the `def` statement to define a function called `hello` that prints `Hello World!` without accepting any input:
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

To demonstrate this, add the code below to the end of `say.py`: {{1}}
```python
if __name__ == '__main__':
    hello()
```
{{1}}

The code above calls the `hello` function only when `say` is run as a script. {{2}}

The `if` statement prevents `hello` from being called when `say` is imported. {{3}}

Adding `hello()` to `say.py` without the `if` statement, would make `greet.py` print `Hello World!` twice, because the entire `say.py` would be run upon import! {{4}}

## Running projects

In addition to running a module as a script, we can also run an entire project.

This requires that the project contain a top-level script called `__main__.py`. {{1}}

The `__main__.py` script can  {{2}}
- execute all of the code in the project simply by importing each script, {{2}}
- accept input from the user, and {{2}}
- work even if the project is turned into a zip file, e.g. `my_project.zip`. {{2}}

A great example of how we can enjoy the convenience of including everything in a single file without sacrificing modularity! {{3}}

1. Make a directory (`mkdir`) called `my_project`
2. Create a file called `__main__.py` with the contents `import greet`
3. Move (`mv`) `__main__.py`, `say.py`, and `greet.py` into `my_project`
4. Run the project like you would run a script

```bash
mkdir my_project
echo "import greet" > __main__.py
mv __main__.py say.py greet.py my_project
python my_project
```

To zip the whole project and then run the zip file:
```bash
python -m zipfile -c my_project.zip my_project/*
python my_project.zip
```

