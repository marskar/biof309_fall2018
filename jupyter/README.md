# Create and execute a Jupyter notebook in the terminal

1. Create a notebook
    - Run `nbcreate.py` script in your terminal, providing all of the names of the source files as arguments, e.g.
    
    `python nbcreate.py README.md plot.py notes.txt`
    
2. Execute the notebook
    - Run the following command in your terminal:
    
    `jupyter nbconvert raw.ipynb --to notebook --execute --output out.ipynb`
 
You can change `out.ipynb` to a more descriptive filename in the command above.
