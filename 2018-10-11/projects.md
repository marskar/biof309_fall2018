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

### tl;dr
A project is a directory that contains project files.

Also, an opportunity to exercise empathy for anyone who might use your code (including your future self!)

Project files may be organized into subdirectories or kept at the top-level.

First Python Project Principle: Modularity

### In other words...

A project is a folder with project files inside.
I like to think of each project as a chance to
practice empathy for people who might want to use your code.
Time spent on crafting a good project is an investment in the future.

Project files can be in subdirectories or in the top-level directory.
In the example below, all of the files are at the top level except for analysis.ipynb, which is in the "code" subdirectory.
```
my_project
├── LICENSE
├── README.md
├── code
│   └── analysis.ipynb  <-  Not modular!
└── requirements.txt
```
This brings us to our first Python Project Principle: Modularity.
`analysis.ipynb` is not in line with the Modularity Principle,
because every step in the analysis is done by one file.
A more modular approach would be to have one file for each step in the analysis.

## Modular versus Monolithic

### tl;dr

The opposite of modular is monolithic.

A monolithic file, like `analysis.ipynb`, could contain all project 
- code, 
- documentation, and 
- output. 

To get the benefits of modularity and the convenience of a single file: 
1. start with small files and then 
2. create a separate larger file later.

### In other words...

A monolithic file, like the analysis.ipynb file we saw earlier,
might contain all of the project's code, docs, and output.
This can be very convenient, but this convenience comes at a price. 
To get the best of both worlds start small
and then create a separate large file later on.

## Don't Repeat Yourself (DRY)

### tl;dr
While working on a project, you may notice common patterns.

Reusability Principle: Don't repeat code! Reuse it! 

One way to avoid code repetition is to 
- define a block of reusable code called a function, and 
- replace the repetitive code with function calls. 

To further improve the modularity and reusability of our code, we will 
- define functions in `modules` and 
- use the functions in `scripts`. 

### In other words...

If you begin to notice patterns in the code, it is time to start thinking about the next Python Project Principle: Reusability.
According to the Reusability Principle, you should reuse code instead of repeating it. 
To avoid code repetition, you will need to use functions.
Functions are reusable blocks of code that can be defined once and then called as many times as needed to get the job done.
To take our use of functions to the next level, we will define functions in files called modules and then call the functions in files called scripts. 

## Modules versus Scripts

### tl;dr

Modules and scripts
- are plain-text files that
- have `.py` extensions and
- contain only Python code.

Modules and scripts differ in how and why they are used.

| Filetype |  How?  |       Why?       |
|:--------:|:------:|:----------------:|
| Module   | Import | Define functions |
| Script   | Run    |  Call functions  |

### In other words...

Modules and scripts are Python code files with .py extensions.
They differ only in how and why they are used.
Modules are imported to define functions (and other Python objects),
while scripts are run to perform actions (typically by calling functions).

## Importing Modules

### tl;dr

1. Create a module named `say.py`, which uses the `def` statement to define a function named `hello` that prints `Hello World!` without accepting any input:
```python
def hello():
       print("Hello World!")
```

2. Create a script named `greet.py`, which imports the `say` module and calls the `hello` function:
```python
import say
say.hello()
```

3. Type `python greet.py` in a shell and press Enter.

### In other words...
Above is an example module named say that defines a function named hello.
There is also an example script named greet that imports the say module and calls its hello function.
You may have noticed that I do not include the .py extension when referring to modules and scripts.

## Running Modules as Scripts

### tl;dr
It is possible for the same file to be used as both a module and a script.

To demonstrate this, we could add the code below to the end of the `say` module: 
```python
if __name__ == '__main__':
    hello()
```

The code above calls the `hello` function only when `say` is run as a script. 

The `if` statement prevents `hello` from being called when `say` is imported. 

Adding `hello()` to `say` without the `if` statement, would make `greet` print `Hello World!` twice.
Once when the `say` module is imported and again when `greet` calls `hello`. 
This is because the `say` module, like all `.py` files, is executed immediately upon import! 

### In other words...

A Python code file can be used as both a module and a script.

To make a module/script hybrid we need to use an if statement that calls a function only when the file is run as a script and not when it is imported as a module. 

In the example of the say module and greet script, this if statement allows say to print "Hello World!" when it is run, but also keeps the hello function from being called when say is imported.

What if we added the function call to say without the if statement? 
In that case, running greet would print "Hello World!" twice:
The first time when say is imported and then again when greet calls the hello function.

Python code files, regardless of whether they are modules or scripts, are executed immediately upon import.

## Running Scripts

### tl;dr

Scripts in data science projects are typically run in a particular order.

This order can be visualized as a diagram called a directed acyclic graph (DAG): 

![](https://assets.datacamp.com/production/repositories/3687/datasets/3d4fdb37d0924a05ab75fcc786dc590b33dbbf4b/simple_dag.png) 

Each script handles one step in the process and imports the tools it needs from modules that are included in the project. 

To run a series of scripts, use the `import` statement as in the example below.
```python
import get_data, clean_data, fit_model, evaluate_model
```

### In other words...

Scripts in data science projects are typically run in a sequence that be shown as a directed acyclic graph.

In the sequence, each script does one job and imports the tools it needs from modules in the project.

It can be tedious to run each script one after another.
Your first instinct may be to combine the scripts into a monolithic file.
Instead, you could write a script to run all of the other scripts in the project.
A clever way to do this is to use the import statement.
You can import one script per line or include all of the scripts on one line separated by commas.

I think it's worth repeating: Python code files, regardless of whether they are modules or scripts, are executed immediately upon import.

## Running Projects

### tl;dr

The `import` statement used to execute all of the scripts in a project would be most useful in a top-level script called `__main__.py`.

The `__main__.py` script can  {{2}}
- be run outside of the project, {{2}}
- accept input from the user, and {{2}}
- work even if the project is turned into a zip file, e.g. `my_project.zip`. {{2}}

A great example of how we can enjoy the convenience of including everything in a single file without sacrificing modularity! {{3}}

### In other words...

The script that uses the import statement to execute all of the other scripts in a project should be at the top level and will be most useful if it is named `__main__.py`.
Double underscores around Python names are pronounced dunder.
The double underscores indicate that the name is special.
Python objects that have such names usually have some superpowers. 
The superpower of `__main__.py` is that
it can be executed from outside of a project using the project name.
This will work even if the project is zipped!

The ability to run a zipped project is a great example of
enjoying the convenience of a single file without sacrificing modularity!

### Some shell code to demonstrate `__main__.py`

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

