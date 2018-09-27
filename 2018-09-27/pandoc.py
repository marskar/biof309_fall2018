import pypandoc


def write_file(filename, contents):
    with open(filename, 'w') as f:
        f.write(contents)


# With an input file: it will infer the input format from the filename
output = pypandoc.convert_file('2018-09-27/about.md', to='rst')

write_file('about.rst', output)
