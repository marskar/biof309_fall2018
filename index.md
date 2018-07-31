I recommend you use one of the following methods to make slides:

Knit (Ctrl/Cmd + Shift + K) slides from Rmd to HTML in RStudio or using the command below:

`Rscript -e "rmarkdown::render('slidy.Rmd', 'slidy_presentation')"`
- [ioslides from Rmd](/biof309_fall2018/slides/ioslides.html)
- [slidy from Rmd](/biof309_fall2018/slides/slidy.html)
- [xaringan from Rmd](/biof309_fall2018/slides/xaringan.html)

Create HTML slides from md using [Pandoc](http://pandoc.org/MANUAL.html#producing-slide-shows-with-pandoc) using the command below:

`pandoc -t slidy -s habits-pandoc.md -o slidy-pandoc.html`
- [dzslides from md](/biof309_fall2018/slides/dzslides-pandoc.html)
- [slidy from md](/biof309_fall2018/slides/slidy-pandoc.html)


Create HTML slides from ipynb using [nbconvert](https://nbconvert.readthedocs.io/en/latest/) using the command below:

`jupyter nbconvert revealjs.ipynb --to slides --reveal-prefix="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.5.0"`
- [revealjs from ipynb](/biof309_fall2018/slides/revealjs.slides.html)
The solution for making slides from JupyterLab is not great right now. It can work, but requires some setup.
I would not recommend trying it until the next version of `jupyter nbconvert` comes out.
