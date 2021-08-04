import networkx as nx


g = nx.DiGraph()
g.add_node(1, label='root') 
g.add_node(2, label='child1') 
g.add_edge(1, 2, label='edge1')

A = nx.drawing.nx_agraph.to_agraph(g)
A.layout('dot')#, args='-Nfontsize=10 -Nwidth=".2" -Nheight=".2" -Nmargin=0 -Gfontsize=8')
A.draw("result.svg")
print(f'Graph generated: result.svg')
