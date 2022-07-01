import numpy as np
import matplotlib.pyplot as plt; plt.close('all')
import networkx as nx
import matplotlib.animation as animation

# Create graph
nodes = range(9)
edges = [(0,1), (0,2), (1,2), (1,3), (1,4), (3,5), (5,6), (5,7), (5,8), (7,8), (8, 9)]
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# draw graph
pos   = nx.spring_layout(G)
nodes = nx.draw_networkx_nodes(G, pos)
edges = nx.draw_networkx_edges(G, pos)

plt.axis('off')
fig = plt.gcf()
#node_colors = ["#5583ba"] * 10
node_colors = np.random.randint(0, 100, size=(1, len(nodos)))
# Debe defirse este init para que funcione
def init():
    # AJustamos la escala del plot y regresamos una tupla
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 20)
    return scat,

def update_plot(frames, nodes, node_colors):
    print(frames)
    # nodes are just markers returned by plt.scatter;
    # node color can hence be changed in the same way like marker colors
    nodes.set_array(node_colors)
    return nodes,

# Los frames se iran repitiendo una y otra vez en un bucle infinito
ani = animation.FuncAnimation(fig, update_plot, frames=5,
                                  fargs=(nodes, node_colors))

#ani.save('scatter.gif', writer='pillow')  ## Para guardarlo en un gif
plt.show()
