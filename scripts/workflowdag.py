import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from([("pred.py","pkl"),
                  ("csv", "pred.py"),
                  ("csv", "plot.py"),
                  ("plot.py", "png"),
                  ("Rmd", "md"),
                  ("bib", "md"),
                  ("csl", "md"),
                  ("csv","Rmd"),
                  ("pkl","Rmd"),
                  ("png","Rmd"),
                  ("md","ipynb"),
                  ("ipynb", "md"),
                  ("ipynb", "html/tex"),
                  ("md","html/tex"),
                  ("html/tex", "pdf"),
                  ("md","docx/pptx")])
pos = {"Rmd" : (0,10),
       "md" : (0,0),
       "bib" : (-0.75,2),
       "csl" : (0.75,2),
       "pkl" : (0.75,10),
       "csv" : (0,20),
       "plot.py" : (-0.75,20),
       "pred.py" : (0.75,20),
       "png" : (-0.75,10),
       "ipynb" : (1,-5),
       "html/tex" : (0.3,-10),
       "pdf" : (-0.5,-10),
       "docx/pptx" : (-1,-10)
       }
lab = {("Rmd", "md"): "knitr",
       ("csv", "plot.py"): "pandas",
       ("csv", "pred.py"): "pandas",
       ("csv", "Rmd"): "pandas",
       ("pred.py", "pkl"): "pickle",
       ("pkl", "Rmd"): "pickle",
       ("plot.py", "png"): "matplotlib",
       ("png", "Rmd"): "knitr",
       ("bib", "md"): "pandoc",
       ("csl", "md"): "pandoc",
       ("md", "ipynb"): "notedown",
       ("ipynb", "html/tex"): "nbconvert",
       ("md", "html/tex"): "pandoc",
       ("md", "docx/pptx"): "pandoc",
       ("html/tex", "pdf"): "print/LaTeX",
       }
nx.draw_networkx_edge_labels(G, pos, font_size=10, edge_labels=lab, rotate=False)
nx.draw(G, pos, with_labels=True, font_size=10, node_size=1600, node_color="white")
plt.show()

N=len(pos)
keys=list(pos.keys())

X=[pos[key][0] for key in keys]
Y=[pos[key][1] for key in keys]

