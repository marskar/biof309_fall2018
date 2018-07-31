## Host your HTML slides on GitHub pages

#### Knit (Ctrl/Cmd + Shift + K) slides from Rmd to HTML in RStudio or using the command below:

```
Rscript -e "rmarkdown::render('slidy.Rmd', 'slidy_presentation')"
```
- [ioslides](/biof309_fall2018/slides/ioslides.html)
- [slidy](/biof309_fall2018/slides/slidy.html)
- [xaringan](/biof309_fall2018/slides/xaringan.html)

#### Create HTML slides from md using [Pandoc](http://pandoc.org/MANUAL.html#producing-slide-shows-with-pandoc) using the command below:

```
pandoc -t slidy -s habits-pandoc.md -o slidy-pandoc.html
```
- [dzslides](/biof309_fall2018/slides/dzslides-pandoc.html)
- [slidy](/biof309_fall2018/slides/slidy-pandoc.html)

#### Create HTML slides from ipynb using [nbconvert](https://nbconvert.readthedocs.io/en/latest/) using the code below:

```
url="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.5.0"
jupyter nbconvert revealjs.ipynb --to slides --reveal-prefix=$url
```

- [revealjs](/biof309_fall2018/slides/revealjs.slides.html)

Exporting slides from JupyterLab does not work (great) right now.
It requires some [additional setup](https://github.com/jupyterlab/jupyterlab/issues/4067).
I would not recommend trying it until the next version of `jupyter nbconvert` comes out.
