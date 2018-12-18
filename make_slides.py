import sys
import pytest
from pypandoc import convert_file


def write_file(filename: str, contents: str) -> None:
    """Writes contents to a file named filename

    Args:
        filename: The name of the target file
        contents: The contents of the target file

    Examples:
        >>> import tempfile
        >>> outfile_path = tempfile.mkstemp()[1]
        >>> write_file(outfile_path, "Test file contents")
        >>> with open(outfile_path) as file: file.read()
        'Test file contents'
    """
    with open(filename, 'w') as f:
        f.write(contents)


def make_slides(source: str = 'slides.md', target: str = 'slidy') -> str:
    """Writes contents to a file named filename

    Args:
        source: The filepath of the target file
        target: The HTML slideshow type, must be revealjs, slidy, or dzslides

    Returns:
        A string of characters that are the contents of an html slideshow.

    Raises:
        ValueError: Only three target frameworks: revealjs, slidy, or dzslides,
            are currently supported.

    Examples:
        A minimal example using temporary input and output files
        >>> import tempfile # library needed to make temp files
        >>> infile_path = tempfile.mkstemp('.md')[1] # markdown file path
        >>> write_file(infile_path, "# Markdown header") # markdown content
        >>> outfile_path = tempfile.mkstemp(suffix='.html')[1] # html file path
        >>> write_file(outfile_path, make_slides(infile_path)) # html slides
        >>> with open(outfile_path, "r") as f: outfile_contents = f.read()
        >>> lines = outfile_contents.split('\\n') # split contents into lines
        >>> lines[0] # first line
        '<?xml version="1.0" encoding="utf-8" ?>'
        >>> lines[-4] # fourth to last line
        '<div id="markdown-header" class="titleslide slide section level1"><h1>Markdown header</h1></div>'
    """
    if target in ('slidy', 'dzslides', 'revealjs'):
        return convert_file(source, to=target, extra_args=['--self-contained']
                            if target is not 'revealjs'
                            else ['-sV', 'revealjs-url=https://revealjs.com'])
    else:
        raise ValueError(f"{target} is not one of the 3 supported formats.")

if __name__ == '__main__':
    pytest.main(sys.argv)
    write_file('revealjs.html', make_slides(target='revealjs'))
