import networkx as nx
import matplotlib.pyplot as plt
import queue as Q
from collections import defaultdict
def gbfs(adjacencyList, heuristics):
    i = 0
    sVertex=max(heuristics,key=heuristics.get)
    fVertex=min(heuristics,key=heuristics.get)
    print("\nThe Starting Node is {} and the end is {}".format(sVertex,fVertex))
    visitedSet = set()
    queue = []
    visitedSet.add(sVertex)
    queue.append(sVertex)
    result=[]
    while queue:
        search=[]
        v = queue[i]
        if v == fVertex:
            result.append(v)
            break
        result.append(v)
        for neighbor in adjacencyList[v]:
            if neighbor not in visitedSet:
                search.append(heuristics[neighbor])
        x = min(search,default="Nimededi")
        for k, v in heuristics.items():
            if x == v:
                queue.append(k)
                visitedSet.add(k)
        i+=1
    return result
def generateAdjacencyLst(edges):
    adjacencyList = defaultdict(list)
    for u, v in edges:
        adjacencyList[u].append(v)
        adjacencyList[v].append(u)
    return adjacencyList
edges = [["SportsComplex","Siwaka"]
         ,["Siwaka","Ph1.A"]
         ,["Ph1.A","Ph1.B"]
         ,["Siwaka","Ph1.B"]
         ,["Ph1.A","Mada"]
         ,["Ph1.B","Phase2"]
         ,["Ph1.B","STC"]
         ,["STC","Phase2"]
         ,["STC","ParkingLot"]
         ,["Phase2","J1"]
         ,["Phase2","Phase3"]
         ,["Phase3","ParkingLot"]
         ,["J1","Mada"]
         ,["Mada","ParkingLot"]]
adjacencyList = generateAdjacencyLst(edges)
for i in adjacencyList:
    print(i)
    print("\t{}".format(adjacencyList[i]))
heuristics = {
    'SportsComplex':730,
    'Siwaka':405,
    'Ph1.A':380,
    'Ph1.B':280,
    'STC':213,
    'Phase2':210,
    'J1':500,
    'Phase3':160,
    'Mada':630,
    'ParkingLot':0
    }
x = gbfs(adjacencyList,heuristics)
G = nx.Graph()

print("\nThe route given is {}".format(x))

# Define nodes with specific positions on the graph
G.add_node('SportsComplex', pos=(0,-1))
G.add_node('Siwaka', pos=(3,-1))
G.add_node('Ph1.A', pos=(5,-1))
G.add_node('Ph1.B', pos=(5,-2.5))
G.add_node('Phase2', pos=(7,-2.5))
G.add_node('J1', pos=(9,-2.5))
G.add_node('Mada', pos=(11,-2.5))
G.add_node('STC', pos=(5,-5))
G.add_node('Phase3', pos=(8,-4))
G.add_node('ParkingLot', pos=(8,-6))

# Define edges from node A to node B and a label corresponding to the distance between the two nodes
G.add_edge('SportsComplex', 'Siwaka')
G.add_edge('Siwaka', 'Ph1.A')
G.add_edge('Siwaka', 'Ph1.B')
G.add_edge('Ph1.A', 'Ph1.B')
G.add_edge('Ph1.A', 'Mada')
G.add_edge('Ph1.B', 'Phase2')
G.add_edge('Ph1.B', 'STC')
G.add_edge('Phase2', 'J1')
G.add_edge('Phase2', 'STC')
G.add_edge('Phase2', 'Phase3')
G.add_edge('J1', 'Mada')
G.add_edge('STC', 'ParkingLot')
G.add_edge('Phase3', 'ParkingLot')
G.add_edge('Mada', 'ParkingLot')

# Array of node sizes
sizes = [7500, 2000, 1700, 1700, 2400, 1000, 1700, 1500, 3000, 4500]
sizes_red = [7500, 2000, 1700, 2400, 3000, 4500]

pos = nx.get_node_attributes(G, 'pos')
nx.draw(G,pos,with_labels=1,node_size=500)
nx.draw_networkx_nodes(G,pos,node_size=sizes)
nx.draw_networkx_nodes(G,pos,node_color="tab:red",nodelist=x,node_size=sizes_red)
nx.draw_networkx_edge_labels(G,pos,edge_labels={
    ("SportsComplex","Siwaka"):"UnkRoad 450m"
    ,("Siwaka","Ph1.A"):"SangaleRd 10m"
    ,("Ph1.A","Ph1.B"):"ParkingWalkWay 100m"
    ,("Siwaka","Ph1.B"):"SangaleLink 230m"
    ,("Ph1.A","Mada"):"SangaleRd 850m"
    ,("Ph1.B","Phase2"):"KeriRd 112m"
    ,("Ph1.B","STC"):"KeriRd 50m"
    ,("STC","Phase2"):"STCwalkway 50m"
    ,("STC","ParkingLot"):"LibraryWalkWay 250m"
    ,("Phase2","J1"):"KeriRd 600m"
    ,("Phase2","Phase3"):"KeriRd 500m"
    ,("Phase3","ParkingLot"):"HimaGardensRd 350m"
    ,("J1","Mada"):"SangaleRd 200m"
    ,("Mada","ParkingLot"):"langataRd 700m"
    },font_size=7,horizontalalignment='center', verticalalignment='center')
plt.show()
