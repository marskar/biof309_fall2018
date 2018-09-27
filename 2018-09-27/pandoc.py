import pypandoc


def write_file(filename, contents):
    with open(filename, 'w') as f:
        f.write(contents)


# With an input file: pypandoc will infer the input format from the filename
output = pypandoc.convert_file('2018-09-27/about.md', to='rst')
write_file('2018-09-27/about.rst', output)

# You can make a slidy HTML slide deck
slides = pypandoc.convert_file('2018-09-27/slides.md', to='slidy', extra_args=['-s'])

# And specify style with a css file, e.g. https://github.com/alblaine/countess
slides = pypandoc.convert_file('2018-09-27/slides.md', to='slidy', extra_args=['-s', '--css=style.css'])

# Another option is to make a dzslides HTML slide deck
slides = pypandoc.convert_file('2018-09-27/slides.md', to='dzslides', extra_args=['-s'])

# And now with a css style: https://gist.github.com/bjin/2264634
slides = pypandoc.convert_file('2018-09-27/slides.md', to='dzslides', extra_args=['-s', '--css=slide.css'])

# You can also make a revealjs HTML slide deck
slides = pypandoc.convert_file('2018-09-27/slides.md', to='revealjs', extra_args=['-s', '-V', 'revealjs-url=http://lab.hakim.se/reveal-js'])

# Try the sky revealjs theme
slides = pypandoc.convert_file('2018-09-27/slides.md', to='revealjs', extra_args=['-s', '-V', 'revealjs-url=http://lab.hakim.se/reveal-js', '-V', 'theme=sky'])

# Try the moon revealjs theme
slides = pypandoc.convert_file('2018-09-27/slides.md', to='revealjs', extra_args=['-s', '-V', 'revealjs-url=http://lab.hakim.se/reveal-js', '-V', 'theme=moon'])

write_file('2018-09-27/about.html', slides)
