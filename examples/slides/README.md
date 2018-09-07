# Host your HTML slides on GitHub pages

The goal of this tutorial is to demonstrate how to make HTML slidedecks that can be put on the web.

Instructions for how to turn [Markdown ](https://www.markdownguide.org/) (`.md`), [R Markdown ](https://rmarkdown.rstudio.com/lesson-1.html) (`.Rmd`), and [Jupyter Notebook ](https://jupyterlab.readthedocs.io/en/stable/user/notebook.html) (`ipynb`) files into slides are detailed below.

By the way, the document you are reading now is written in [Markdown](https://www.markdownguide.org/)!

One major advantage of HTML slidedecks is that you can host them on GitHub for free and share a url, instead of resorting to email or transferring files using USB drives.

Check out the rendered examples at [https://marskar.github.io/slides/](https://marskar.github.io/slides/).

Instead of using Powerpoint, Keynote, or Google Slides, I recommend you try to generate slides programmatically using the steps below.

Speaking of Powerpoint, I suggest that you avoid the horrors of Microsoft Office entirely.
- Instead of using Microsoft Word & Powerpoint and the doc(x) & ppt(x) formats, write documents and [slideshows](https://marskar.github.io/slides/) in [Markdown](https://www.markdownguide.org/) format and then converted into the desired output format using one of the three options below:
    1. [Pandoc](https://pandoc.org/) and [Pypandoc](https://github.com/bebraw/pypandoc)
    2. [RStudio](https://www.rstudio.com/products/rstudio/download/) (which requires installing the [R programming language](https://www.rstudio.com/products/rstudio/download/))
    3. [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) (or the classic [Jupyter Notebook](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html))
- Instead of using Microsoft Excel and the xls(x) format, save tabular data as comma-separated value (csv) files. [PyCharm](https://www.jetbrains.com/pycharm/features/), [RStudio](https://www.rstudio.com/products/rstudio/download/) and [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) all have csv viewers. These csv viewers are better options for looking at data than Excel, because they do not have the ability to edit or auto-format your raw data.
- [Tables that are meant to be displayed in documents](https://www.markdownguide.org/extended-syntax/#tables) can also be written in [Markdown](https://www.markdownguide.org/) format instead of in Excel.

## Create HTML slides from markdown (md) using [Pandoc](http://pandoc.org/MANUAL.html#producing-slide-shows-with-pandoc) and [Pypandoc](https://github.com/bebraw/pypandoc)

The easiest way to create a slideshow is to write a simple markdown file, like `habits.md`, and use [Pandoc](http://pandoc.org/MANUAL.html#producing-slide-shows-with-pandoc) to convert it to one of the possible HTML formats.

There are many ways to [install Pandoc](https://pandoc.org/installing.html), but I recommend to use [Anaconda](https://conda.io/docs/glossary.html#anaconda-glossary) or [Miniconda](https://conda.io/docs/glossary.html#miniconda-glossary). The [Anaconda installer](https://docs.anaconda.com/anaconda/install/) is hundreds of MB in size because the Anaconda Python distribution includes hundreds of Python packages plus the Anaconda Navigator program. The [Miniconda installer](https://conda.io/miniconda.html) is more than ten times smaller and includes only Python and conda.

Once you have [Anaconda](https://conda.io/docs/glossary.html#anaconda-glossary) or [Miniconda](https://conda.io/docs/glossary.html#miniconda-glossary) installed, you can install [Pandoc](http://pandoc.org/MANUAL.html#producing-slide-shows-with-pandoc) using this command-line command `conda install -yc conda-forge pandoc` and then run the one of the options below:

```
pandoc -t dzslides --self-contained -s habits.md -o pandoc/dzslides-pandoc.html
pandoc -t slidy --self-contained -s habits.md -o pandoc/slidy-pandoc.html
```

Instead of using [Pandoc](http://pandoc.org/MANUAL.html#producing-slide-shows-with-pandoc) in the terminal as described above, you can also install [Pypandoc](https://github.com/bebraw/pypandoc) and convert [Markdown](https://www.markdownguide.org/) to almost any format in your Python environment (e.g. in [PyCharm](https://www.jetbrains.com/pycharm/features/))!

- Pro-tip 1: You can write [Markdown](https://www.markdownguide.org/) in [PyCharm](https://www.jetbrains.com/pycharm/features/)! Press Ctrl/Cmd+N, then Enter, type out the name of the [Markdown](https://www.markdownguide.org/) file (must end in `.md`) you want to create, and press Enter again. You get [Markdown](https://www.markdownguide.org/) syntax highlighting and a live preview of your rendered [Markdown](https://www.markdownguide.org/)!
- Pro-tip 2: If you create a new Python scratch file in [PyCharm](https://www.jetbrains.com/pycharm/features/) (Press Ctrl/Cmd+Shift+N, then Enter) and change the extension from `.py` to `.md`, PyCharm will continue to treat the file like a Python script giving you the ability to run code in your [Markdown](https://www.markdownguide.org/) document! As soon as you take the file out of the Scratches folder, [PyCharm](https://www.jetbrains.com/pycharm/features/) will treat it like a [Markdown](https://www.markdownguide.org/) file again! In short, [PyCharm](https://www.jetbrains.com/pycharm/features/) will auto-detect the file type based on its extension, but this does not apply to scratch files!
- Pro-tip 3: To get automatic python syntax highlighting in your [Markdown](https://www.markdownguide.org/) documents on [GitHub](https://github.com/) and in [slideshows](https://marskar.github.io/slides/) created from [Markdown](https://www.markdownguide.org/) files, put three backticks (\`) followed by the word "python" above your code and then a new line below your code put another three backticks (\`). This is called a [code block](https://pandoc.org/MANUAL.html#fenced-code-blocks) in [Markdown](https://www.markdownguide.org/).

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
