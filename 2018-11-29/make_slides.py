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


def make_slides(path: str = 'slides.md', framework: str = 'slidy') -> str:
    """Writes contents to a file named filename

    Args:
        path: The filepath of the target file
        framework: The HTML slideshow type, must be revealjs, slidy, or dzslides

    Returns:
        A string of characters that are the contents of an html slideshow.

    Raises:
        TypeError: The framework argument must be passed as string.
        ValueError: Only three html slide frameworks: revealjs, slidy, or dzslides,
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
        '<?xml version="1.0" encoding="utf-8"?>'
        >>> lines[-4] # fourth to last line
        '<div id="markdown-header" class="title-slide slide section level1"><h1>Markdown header</h1></div>'
    """
    if type(framework) is str:
        if framework in ('slidy', 'dzslides'):
            return pypandoc.convert_file(path, to=framework, extra_args=['-s'])
        elif framework == 'revealjs':
            return pypandoc.convert_file(path, to=framework,
                                         extra_args=['-s', '-V', 'revealjs-url=http://lab.hakim.se/reveal-js'])
        else:
            raise ValueError("Framework argument must be 'revealjs', 'slidy', or 'dzslides', not {framework}.")
    else:
        raise TypeError("Framework argument type must be str, not {type(framework)}.")


if __name__ == '__main__':
    doctest.testmod(verbose=True)
    write_file('slides.html', make_slides())
