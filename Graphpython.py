import networkx as nx
import matplotlib.pyplot as plt

vertices = range(1,10)
edges = [(7,2),(2,3),(7,4),(4,5),(7,3),(7,5),(1,6),(1,7),(2,8),(2,9)]

graph = nx.Graph()
graph.add_nodes_from(vertices)
graph.add_edges_from(edges)
positions= nx.spring_layout(graph)

nx.draw_networkx_nodes(graph,positions,nodelist=[1,4,8,3,9],node_color = 'g', node_size=1300)
nx.draw_networkx_nodes(graph,positions,nodelist=[2,5,6,7], node_color = 'y', node_size=1300)
labels={1:'1 NF',2:'2 F',3:'3 NF',4:'4 NF',5:'5 F',6:'6 F',7:'7 F',8:'8 NF',9:'9 NF'}
nx.draw_networkx_labels(graph,positions,labels,font_size=16)
nx.draw_networkx_edges(graph,positions,edges,width=3,alpha=0.5,edge_color='b')
plt.show()

print(nx.degree_centrality(graph))