# Create and execute a Jupyter notebook in the terminal

## Dependencies

If you installed [Anaconda](https://www.anaconda.com/download/), you already have Python and Jupyter.

If not, or if you have [Miniconda](https://conda.io/miniconda.html) installed, run 
 
```sh
conda install -yc conda-forge jupyter nbconvert
```

If you have any other Python installation, run

```sh
pip install jupyter nbconvert
```

## Step 1. Create a notebook

Run `nbcreate.py` script in your terminal, providing all of the names of the source files as arguments, e.g.

```sh
python nbcreate.py README.md plot.py notes.txt
```  
    
## Step 2. Execute the notebook

Run the following command in your terminal:
    
```sh
jupyter nbconvert raw.ipynb --to notebook --execute --output out.ipynb`
```

You can change `out.ipynb` to a more descriptive filename in the command above.

## Too many file names to type out?

You can use the `ls` command to assign all of the relevant names in the current directory to a variable and pass this variable as an argument to `nbconvert.py`.
 
To preserve the order and differentiate files that should be incorporated into the notebook, I recommend left padding your file names with zeros (e.g. 01_intro.md, 02_figure1.py).
 
Consider the example below:

```sh
touch {01..09}.py
name_list=`ls 0*.py`
python nbcreate.py `echo $name_list`
```
