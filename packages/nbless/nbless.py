from typing import List
from . import nbuild, nbexec

def nbless(filenames: List,
           nbuild_name: str = 'raw.ipynb',
           nbuild_path: str = './',
           nbexec_name: str = 'output.ipynb',
           nbexec_path: str = './') -> None:

    nbuild(filenames=filenames,
           output_name=nbuild_name,
           output_path=nbuild_path)

    if not nbuild_path.endswith('/'):
        nbuild_path += '/'

    nbexec(input_name=nbuild_path+nbuild_name,
           output_name=nbexec_name,
           output_path=nbexec_path)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
          description='Create and execute a notebook from the command line.')

    parser.add_argument('names', nargs='+', help='A series of filenames.')

    parser.add_argument('--out', '-o', default='raw.ipynb',
                       help='The filename of the output notebook.')

    parser.add_argument('--path', '-p', default='./',
                       help='The path where the output notebook is saved.')

    args = parser.parse_args()
    names = args.names
    out_name = args.out
    out_path = args.path

    nbuild(filenames=names,
           output_name=out_name,
           output_path=out_path)
    nbexec(input_name=out_path,
           output_name=nbexec_name,
           output_path=nbexec_path)
