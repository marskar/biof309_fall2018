import pypandoc
import doctest


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


def make_slides(path: str = 'slides.md', slide_type: str = 'slidy') -> str:
    """Writes contents to a file named filename

    Args:
        path: The filepath of the target file
        slide_type: The HTML slideshow type, must be revealjs, slidy, or dzslides

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
        '<?xml version="1.0" encoding="utf-8"?>'
        >>> lines[-4] # fourth to last line
        '<div id="markdown-header" class="title-slide slide section level1"><h1>Markdown header</h1></div>'
    """
    if slide_type in ('slidy', 'dzslides'):
        return pypandoc.convert_file(path, to=slide_type, extra_args=['-s'])
    elif slide_type == 'revealjs':
        return pypandoc.convert_file(path, to=slide_type,
                                     extra_args=['-s', '-V',
                                                 'revealjs-url=http://lab.hakim.se/reveal-js'])
    else:
        raise TypeError("Slide type must be 'revealjs', 'slidy', or 'dzslides', "
                        f'not {slide_type}.')


if __name__ == '__main__':
    doctest.testmod(verbose=True)
    write_file('slides.html', make_slides())
