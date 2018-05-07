# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 15:44:01 2018

@author: Dane M4
"""
import data_analysis_fin
import networkx as nx
import matplotlib.pyplot as plt

nodes = data_analysis_fin.longest_cycle

edges = []



i = 0
while i < len(nodes) - 2:
    edges.append((nodes[i], nodes[i+1]))
    i+=1
   
edges.append((nodes[-2], nodes[-1]))
edges.append((nodes[-1], nodes[0]))

C = nx.Graph()

C.add_nodes_from(nodes)

C.add_edges_from(edges)






#nx.draw_circular(G, with_labels=True, edge_color = 'blue', font_weight = 'bold')
#plt.savefig('pkmn_super_effective.png', dpi=300)