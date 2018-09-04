# Create and run a jupyter notebook programmatically

1. Edit the `nbcreate.py` script
    - List the names of source files you want to include (line 3)
    - Save the `nbcreate.py` script
2. Run `nbcreate.py` script from the command line
    - `python nbcreate.py`
3. Execute the notebook created by the `nbcreate.py` script
    - `jupyter nbconvert raw.ipynb --to notebook --execute --output out.ipynb`
 
You can change `out.ipynb` to a more descriptive filename in the command above.
