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
        >>> infile_path = tempfile.mkstemp()[1] # tempfile 1
        >>> write_file(infile_path, "Let's pretend this a Markdown file")
        >>> out = tempfile.mkstemp()[1] # tempfile 2
        >>> write_file(out, make_slides(infile_path))
        >>> import fleep
        >>> with open(out, "rb") as file: fleep.get(file.read(128)).extension
        ['xml']
    """
    if slide_type in ('slidy', 'dzslides'):
        return pypandoc.convert_file(path, to=slide_type, format='html', extra_args=['-s'])
    elif slide_type == 'revealjs':
        return pypandoc.convert_file(path, to=slide_type, format='html',
                                     extra_args=['-s', '-V',
                                                 'revealjs-url=http://lab.hakim.se/reveal-js'])
    else:
        raise TypeError("Slide type must be 'revealjs', 'slidy', or 'dzslides', "
                        f'not {slide_type}.')


if __name__ == '__main__':
    doctest.testmod(verbose=True)
    write_file('slides.html', make_slides())
