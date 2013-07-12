import networkx as nx
import matplotlib.pyplot as plt
from math import sqrt

i = 1

def save(G, path):
    "Draw a graph with specific x, y coordinates"
    global i
    pos = {}
    x=nx.get_node_attributes(G,'x')
    y=nx.get_node_attributes(G,'y')

    for n in G.node:
        pos[n] = [x[n], y[n]]

    plt.figure(i)
    i = i + 1
    nx.draw(G, pos)
    plt.savefig(path)


def draw(G):
    "Draw a graph with specific x, y coordinates"
    pos = {}
    x=nx.get_node_attributes(G,'x')
    y=nx.get_node_attributes(G,'y')

    for n in G.node:
        pos[n] = [x[n], y[n]]

    nx.draw(G, pos)
    plt.show()

def initgraph(G):
    "Initialize graph with all edge their weight. Weight function is euclidean diastance"
    x=nx.get_node_attributes(G,'x')
    y=nx.get_node_attributes(G,'y')

    for i in sorted(nx.nodes(G)):
        for j in range(int(i)+1, len(G)):
            G.add_edge(i, str(j), weight=sqrt((x[i] - x[str(j)])**2 + (y[i] - y[str(j)])**2))            

def addEdge(L, G, listnode, item, index):
    cost = 0
    try:
        L.add_edge(item, listnode[index+1], weight=G[item][listnode[index+1]]['weight'])
        cost = G[item][listnode[index+1]]['weight']
    except KeyError as e:
        L.add_edge(listnode[index+1], item, weight=G[listnode[index+1]][item]['weight'])
        cost = weight=G[listnode[index+1]][item]['weight']
    finally:
        return cost

def randomCityGraph(n):
    G = nx.random_geometric_graph(n,1)
    pos=nx.get_node_attributes(G,'pos')

    weight = {};

    for u,v,d in G.edges(data=True):
        G.add_edge(u, v, weight=sqrt((pos[u][0] - pos[v][0])**2 + (pos[u][1] - pos[v][1])**2))

    return G