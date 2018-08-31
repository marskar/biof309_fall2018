# Host your HTML slides on GitHub pages

The goal of this tutorial is to demonstrate how to make HTML slidedecks that can be put on the web.

One major advantage of this is that you can share a url, instead of resorting to email or transferring files using USB drives.

Instead of using Powerpoint, Keynote, or Google Slides, I recommend you try to generate slides programmatically using the steps below.

Check out the rendered examples at [https://marskar.github.io/slides/](https://marskar.github.io/slides/).

## Create HTML slides from markdown (md) using [Pandoc](http://pandoc.org/MANUAL.html#producing-slide-shows-with-pandoc)

The easiest way to create a slideshow is to write a simple markdown file, like `habits.md`, and use Pandoc to convert it to one of the possible HTML formats.

There are many ways to install Pandoc, but I recommend to use [Anaconda](https://conda.io/docs/glossary.html#anaconda-glossary) or [Miniconda](https://conda.io/docs/glossary.html#miniconda-glossary). The [Anaconda installer](https://docs.anaconda.com/anaconda/install/) is hundreds of MB in size because the Anaconda Python distribution includes hundreds of Python packages plus the Anaconda Navigator program. The [Miniconda installer](https://conda.io/miniconda.html) is more than ten times smaller and includes only Python and conda.

Once you have [Anaconda](https://conda.io/docs/glossary.html#anaconda-glossary) or [Miniconda](https://conda.io/docs/glossary.html#miniconda-glossary) installed, you can install pandoc using this command-line command `conda install -yc conda-forge pandoc` and then run the one of the options below:

```
pandoc -t dzslides -s habits.md -o pandoc/dzslides-pandoc.html
pandoc -t revealjs -s habits.md -o pandoc/revealjs-pandoc.html -V revealjs-url=http://lab.hakim.se/reveal-js
pandoc -t slidy -s habits.md -o pandoc/slidy-pandoc.html
```

## Knit slides from md or Rmd to HTML in [RStudio](https://rmarkdown.rstudio.com/lesson-11.html) or from the command-line

First, you will need to install R. Again, I recommend installing [Anaconda or Miniconda](https://docs.anaconda.com/anaconda/install/) and then running `conda install -yc r r-essentials`.

Then, write you can run one of the commands below to make the html slideshow.
```
Rscript -e "rmarkdown::render('habits.md', 'ioslides_presentation', 'r/ioslides-r.html')"
Rscript -e "rmarkdown::render('habits.md', 'slidy_presentation', 'r/slidy-r.html')"
```

You can also install RStudio by running `conda install -yc r rstudio`, open up a markdown file in RStudio, add a YAML header that specifies the `output_format` as in `habits.Rmd`, save the file and then click Preview/Knit or Press Ctrl/Cmd + Shift + K.

For revealjs and xaringan slides, you must first run `install.packages('revealjs')` and `install.packages('xaringan')` in RStudio before you can Knit (Ctrl/Cmd + Shift + K). 

**You only need to install the packages once!**

You can also run install the packages and render slides from the command-line as below:

```
Rscript -e "install.packages('revealjs', repos='http://cran.us.r-project.org')"
Rscript -e "install.packages('xaringan', repos='http://cran.us.r-project.org')"
```

```
Rscript -e "rmarkdown::render('revealjs.Rmd', output_file = 'r/revealjs-r.html')"
Rscript -e "rmarkdown::render('xaringan.Rmd', output_file = 'r/xaringan.html')"
```

## Create HTML slides from ipynb using [nbconvert](https://nbconvert.readthedocs.io/en/latest/) from the command-line

You can also create slides from a Jupyter Notebook using `jupyter nbconvert`.

If you have [Anaconda](https://conda.io/docs/glossary.html#anaconda-glossary) installed, you should already be able to run `jupyter nbconvert`, but if you are using [Miniconda](https://conda.io/docs/glossary.html#miniconda-glossary) you will need to install `nbconvert` by running `conda install -yc conda-forge jupyter nbconvert`.

```
url="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.5.0"
jupyter nbconvert revealjs.ipynb --to slides --reveal-prefix=$url
```

Exporting slides from JupyterLab does not work (great) right now.
It requires some [additional setup](https://github.com/jupyterlab/jupyterlab/issues/4067).
I would not recommend trying it until the next version of `jupyter nbconvert` comes out.

Luckily, there are other ways to make slides from a Jupyter Notebook.

1. The easiest way is to use [nbviewer](https://nbviewer.jupyter.org/), so that you can switch between [notebook](http://nbviewer.jupyter.org/github/marskar/biof309_spring2018/blob/master/slides.ipynb) and [slide view](http://nbviewer.jupyter.org/format/slides/github/marskar/biof309_spring2018/blob/master/slides.ipynb).
2. Another approach is to use [binder for interactive notebooks/slideshows](https://mybinder.org/v2/gh/mgeier/jupyter-presentation/master?filepath=jupyter-presentation.ipynb).

These two options are not the same as [creating an html slideshow from a jupyter notebook and hosting it on your website](https://marskar.github.io/jupyter-notebook-slides), but they get the job done.
