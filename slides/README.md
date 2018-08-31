## Host your HTML slides on GitHub pages

### Create HTML slides from md using [Pandoc](http://pandoc.org/MANUAL.html#producing-slide-shows-with-pandoc) from the command-line as below:

```
pandoc -t dzslides -s habits.md -o pandoc/dzslides-pandoc.html
pandoc -t revealjs -s habits.md -o pandoc/revealjs-pandoc.html -V revealjs-url=http://lab.hakim.se/reveal-js
pandoc -t slidy -s habits.md -o pandoc/slidy-pandoc.html
```
Examples:
- [dzslides](/biof309_fall2018/slides/pandoc/dzslides-pandoc.html)
- [revealjs](/biof309_fall2018/slides/pandoc/revealjs-pandoc.html)
- [slidy](/biof309_fall2018/slides/pandoc/slidy-pandoc.html)

### Knit (Ctrl/Cmd + Shift + K) slides from md or Rmd to HTML in [RStudio](https://rmarkdown.rstudio.com/lesson-11.html) or from the command-line as below:

```
Rscript -e "rmarkdown::render('habits.md', 'ioslides_presentation', 'r/ioslides-r.html')"
Rscript -e "rmarkdown::render('habits.md', 'slidy_presentation', 'r/slidy-r.html')"
```

For revealjs and xaringan slides, you must first run `install.packages('revealjs')` and `install.packages('xaringan')` in RStudio before you can Knit (Ctrl/Cmd + Shift + K). 

You can also run install the packages and render slides from the command-line as below:

**You only need to install the packages once!**

```
Rscript -e "install.packages('revealjs', repos='http://cran.us.r-project.org')"
Rscript -e "install.packages('xaringan', repos='http://cran.us.r-project.org')"
```
```
Rscript -e "rmarkdown::render('revealjs.Rmd', output_file = 'r/revealjs-r.html')"
Rscript -e "rmarkdown::render('xaringan.Rmd', output_file = 'r/xaringan.html')"
```
Examples:
- [ioslides](/biof309_fall2018/slides/r/ioslides.html)
- [slidy](/biof309_fall2018/slides/r/slidy.html)
- [revealjs](/biof309_fall2018/slides/r/revealjs.html)
- [xaringan](/biof309_fall2018/slides/r/xaringan.html)


### Create HTML slides from ipynb using [nbconvert](https://nbconvert.readthedocs.io/en/latest/) from the command-line as below:

```
url="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.5.0"
jupyter nbconvert revealjs.ipynb --to slides --reveal-prefix=$url
```

- [revealjs](/biof309_fall2018/slides/revealjs.slides.html)

Exporting slides from JupyterLab does not work (great) right now.
It requires some [additional setup](https://github.com/jupyterlab/jupyterlab/issues/4067).
I would not recommend trying it until the next version of `jupyter nbconvert` comes out.
I would not recommend trying it until the next version of `jupyter nbconvert` comes out.
Luckily, there are other ways to make slides from a jupyter notebook.
1. The easiest way is to use nbviewer, so that you can switch between notebook
http://nbviewer.jupyter.org/github/marskar/biof309_spring2018/blob/master/slides.ipynb
and slide view
http://nbviewer.jupyter.org/format/slides/github/marskar/biof309_spring2018/blob/master/slides.ipynb
2. Another great approach is to use binder for interactive notebooks/slideshows, e.g. https://mybinder.org/v2/gh/mgeier/jupyter-presentation/master?filepath=jupyter-presentation.ipynb
3. At some point, you will want to host an html slideshow on your website, e.g. https://marskar.github.io/jupyter-notebook-slides 
