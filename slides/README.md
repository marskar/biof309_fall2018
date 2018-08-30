## Host your HTML slides on GitHub pages

### Knit (Ctrl/Cmd + Shift + K) slides from Rmd to HTML in [RStudio](https://rmarkdown.rstudio.com/lesson-11.html) or from the command-line as below:

```
Rscript -e "rmarkdown::render('slidy.Rmd', 'slidy_presentation')"
```
- [ioslides](/biof309_fall2018/slides/ioslides.html)
- [slidy](/biof309_fall2018/slides/slidy.html)
- [xaringan](/biof309_fall2018/slides/xaringan.html)

### Create HTML slides from md using [Pandoc](http://pandoc.org/MANUAL.html#producing-slide-shows-with-pandoc) from the command-line as below:

```
pandoc -t slidy -s habits-pandoc.md -o slidy-pandoc.html
```
- [dzslides](/biof309_fall2018/slides/dzslides-pandoc.html)
- [slidy](/biof309_fall2018/slides/slidy-pandoc.html)

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
