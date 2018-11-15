In the spirit of the Emacs-Vim Editor War and the tabs-versus-spaces debate, the summer of 2018 ended with another epic conflict, the First Notebook War. We'll discuss what all the fuss was about, the event that triggered the war, what we can learn from the opponents and proponents of Jupyter and R notebooks, and how best to benefit from the rapid technological advances of computational notebooks.

[Jupyter notebooks](https://jupyterlab.readthedocs.io/en/stable/user/notebook.html) are data science tools that combine text, code, and output to help data scientists communicate the goals, methods, and results of data analyses. Despite their popularity in [academia](https://www.oreilly.com/ideas/all-the-cool-kids-are-doing-it-maybe-we-should-too) and industry, including at companies like [Amazon](https://www.oreilly.com/ideas/machine-learning-and-ai-technologies-and-platforms-at-aws), [Netflix](https://medium.com/netflix-techblog/scheduling-notebooks-348e6c14cfd6), and [PayPal](https://medium.com/paypal-engineering/paypal-notebooks-powered-by-jupyter-fd0067bd00b0), Jupyter notebooks have [drawbacks that can confound novices and frustrate experts](https://conferences.oreilly.com/jupyter/jup-ny/public/schedule/detail/68282). The fervent discussion of the advantages and disadvantages of notebooks during the summer of 2018 has been dubbed the [First Great Notebook War](https://twitter.com/pgbovine/status/1034626381735317504) and threatens to erupt into a conflict on the scale of the [Emacs-Vim Editor War](https://www.explainxkcd.com/wiki/index.php/1823:_Hottest_Editors) or the [tabs-versus-spaces debate](https://dev.to/__shadz_/tabs-vs-space-49l5).

This talk will discuss the pros and cons of computational notebooks for data science, describe the differences between Jupyter notebooks and [R notebooks](https://rmarkdown.rstudio.com/r_notebooks), and suggest workflows and tools for getting the most out of computational notebooks, including how to 1) work with Jupyter notebooks, R markdown, and Julia, Python, and R scripts using [JupyText](https://github.com/mwouts/jupytext) 2) configure Jupyter Notebooks to run on markdown files with [notedown](https://github.com/aaren/notedown) 3) create and run Jupyter and R notebooks from scripts and markdown files with [nbless](https://github.com/marskar/nbless) and 4) combine Python and R code in R notebooks using the [RStudio IDE](https://www.rstudio.com/) or the [rmarkdown R package](https://rmarkdown.rstudio.com/) at the command line.


the [First Notebook War](https://twitter.com/pgbovine/status/1034626381735317504) was triggered by the criticism of [Jupyter notebooks](https://jupyterlab.readthedocs.io/en/stable/user/notebook.html) in the ["I Don't Like Notebooks" talk Joel Grus gave at Jupytercon 2018](https://conferences.oreilly.com/jupyter/jup-ny/public/schedule/detail/68282). 
Joel Grus' talk focused on  and did not discuss other types of computational notebooks. Notably, R notebooks differ from Jupyter notebooks in that the source file is plain text, flat structure. rather than .  which differ from can be considered the final product of a data analysis, like a Microsoft Word file (`.docx`) .   contrast to LaTeX Computational notebooks 

 in particular have been widely embraced in [academia](https://www.oreilly.com/ideas/all-the-cool-kids-are-doing-it-maybe-we-should-too) and industry, including by companies like [Amazon](https://www.oreilly.com/ideas/machine-learning-and-ai-technologies-and-platforms-at-aws), [Netflix](https://medium.com/netflix-techblog/scheduling-notebooks-348e6c14cfd6), and [PayPal](https://medium.com/paypal-engineering/paypal-notebooks-powered-by-jupyter-fd0067bd00b0).

war was not about R notebooks versus Python, but rather between fans of computational notebooks and proponents of code editors.

[R notebooks](https://yihui.name/en/2018/09/notebook-war/) represent a very different approach to computational notebooks and provide a more beneficial. 

This talk will discuss the advantages and disadvantages of working with Jupyter notebooks, differences between Jupyter notebooks.
Furthermore, many data science platforms, such as Google [colab](https://colab.research.google.com/) and [datalab](https://cloud.google.com/datalab/), [Microsoft Azure notebooks](https://notebooks.azure.com/), [IBM Watson Studio](www.ibm.com/Watson/Studio), and [Kaggle kernels](https://towardsdatascience.com/introduction-to-kaggle-kernels-2ad754ebf77), offer Jupyter notebook interfaces.
For example, Jupyter notebooks have a nested structure based on JSON (JavaScript Object Notation) and thus must be renderd to be easily viewed by users in version control systems like git. in most code editors and. and need to be rendered to easily amenable to. notebooks tempt users to put all of the code, documentation, and output can be included in a single file, and thereby violate the software engineering principle of modularity. F, 
R notebooks represent a very different approach to the common goal of enabling literate programming by juxtapositioning output and code.
Data Science teams at companies like Netflix and PayPal uses notebooks e
Google 
R notebooks represent two very different approaches to the common goal of enabling literate programming by juxtapositioning output and code. Tools and workflows to bridge the gap between lovers and haters of Jupyter and R Notebooks.
, and enable a literate programming approach 

Knuth, Donald E. (1992). Literate Programming. California: Stanford University Center for the Study of Language and Information. ISBN 978-0-937073-80-3.
Represent a [literate programming approach](http://www.literateprogramming.com/) to communicating the details of data analyses.

Notebooks are very popular tools in the R and Python data science communities, 


Computational notebooks are very popular tools in the R and Python communities. Jupyter and R notebooks represent two very different approaches to the common goal of enabling literate programming by juxtapositioning output and code. Tools and workflows to bridge the gap between lovers and haters of Jupyter and R Notebooks.
