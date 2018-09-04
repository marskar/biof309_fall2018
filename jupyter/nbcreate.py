import nbformat as nbf

filenames = [
    'README.md',
    'plot.py',
    'notes.txt'
]


def read_file(filename):
    with open(filename) as f:
        return f.read()


nb = nbf.v4.new_notebook()
md_cell = nbf.v4.new_markdown_cell
code_cell = nbf.v4.new_code_cell

nb['cells'] = [code_cell(read_file(name))
               if name.endswith('.py')
               else md_cell(read_file(name))
               for name in filenames]

nbf.write(nb, 'raw.ipynb')
