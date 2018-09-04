import argparse
import nbformat

parser = argparse.ArgumentParser(
    description='Create a notebook programmatically.')

parser.add_argument('filenames', metavar='N', type=str,
                    nargs='+', help='A series of filenames')

args = parser.parse_args()
filenames = list(args.filenames)


def read_file(filename):
    with open(filename) as f:
        return f.read()


nb = nbformat.v4.new_notebook()
md_cell = nbformat.v4.new_markdown_cell
code_cell = nbformat.v4.new_code_cell

nb['cells'] = [code_cell(read_file(name))
               if name.endswith('.py')
               else md_cell(read_file(name))
               for name in filenames]

nbformat.write(nb, 'raw.ipynb')
