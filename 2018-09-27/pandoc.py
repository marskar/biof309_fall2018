import pypandoc


def write_file(filename, contents):
    with open(filename, 'w') as f:
        f.write(contents)


# With an input file: pypandoc will infer the input format from the filename
output = pypandoc.convert_file('2018-09-27/about.md', to='rst')
write_file('2018-09-27/about.rst', output)

# You can make a slidy HTML slide deck
slides = pypandoc.convert_file('2018-09-27/slides.md', to='slidy', extra_args=['-s'])

# You can make a slidy HTML slide deck
slides = pypandoc.convert_file('2018-09-27/slides.md', to='slidy', extra_args=['-s', '--css=style.css'])

# You can make a dzslides HTML slide deck
slides = pypandoc.convert_file('2018-09-27/slides.md', to='dzslides', extra_args=['-s'])

# You can also make a revealjs HTML slide deck
slides = pypandoc.convert_file('2018-09-27/slides.md', to='revealjs', extra_args=['-s', '-V', 'revealjs-url=http://lab.hakim.se/reveal-js'])

# Try a different revealjs theme
slides = pypandoc.convert_file('2018-09-27/slides.md', to='revealjs', extra_args=['-s', '-V', 'revealjs-url=http://lab.hakim.se/reveal-js', '-V', 'theme=sky'])

write_file('2018-09-27/about.html', slides)

