import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from([("obtain\ndata", "process\ndata"),
                  ("process\ndata", "model"),
                  ("model", "metrics\n& plots"),
                  ])
pos = {"obtain\ndata": (1, 0),
       "process\ndata": (2, 0),
       "model": (3, 0),
       "metrics\n& plots": (4, 0),
       }
lab = {("obtain\ndata", "process\ndata"): "raw\ndata",
       ("process\ndata", "model"): "final\ndata",
       ("model", "metrics\n& plots"): "fitted\nvalues"
       }
nx.draw_networkx_edge_labels(G, pos, font_size=10, edge_labels=lab, rotate=True)
nx.draw(G, pos, with_labels=True, font_size=10, node_size=1800, node_color="white")
plt.savefig('simple_dag.png', dpi=2000)
plt.show()
