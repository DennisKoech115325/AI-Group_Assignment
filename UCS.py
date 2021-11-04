import networkx as nx
import matplotlib.pyplot as plt
import queue as Q
from collections import defaultdict
def checkKey(dict,key):
    if key in dict.keys():
        return True
    else:
        return False
def UCS(Routes,Points=[]):
    sVertex = Points[0]
    fVertex = Points[1]
    result = []
    result.append(sVertex)
    queue = []
    visitedSet = set()
    visitedSet.add(sVertex)
    queue.append(sVertex)
    val = 0
    value = 0
    PQ = {}
    PQ.update({sVertex:val})
    nic = sVertex
    check = 0
    while nic != fVertex:
        print("{}".format(nic))
        for k in Routes[nic]:
            x = Routes[nic].get(k)
            x+=val
            print("\t {} and value: {}".format(k,x))
            if PQ.get(k)!=None:
                value = PQ[k]
                if value>x:
                    PQ.update({k:x})
                else:
                    continue
            else:
                PQ.update({k:x})
        if PQ.get(fVertex) != None:
            result.append(fVertex)
            val += Routes[nic].get(fVertex)
            break
        PQ.pop(nic)
        nic = min(PQ,key=PQ.get)
        val = PQ[nic]
        result.append(nic)
    return result, val
SportsComplex= {
    "Siwaka":450
    }
Siwaka = {
    "Ph1.A":10,
    "Ph1.B":230,
    }
Ph1A = {
    "Ph1.B":100,
    "Mada":850,
    }
Ph1B = {
    "STC":50,
    "Phase2":112
    }
STC = {
    "ParkingLot":250,
    "Phase2":50
    }
Phase2 = {
    "Phase3":500,
    "J1":600
    }
Phase3 = {
    "ParkingLot":350
    }
J1 = {
    "Mada":200
    }
Mada={
    "ParkingLot":700
    }
Routes = {
    "SportsComplex":SportsComplex,
    "Siwaka":Siwaka,
    "Ph1.A":Ph1A,
    "Ph1.B":Ph1B,
    "STC":STC,
    "Phase2":Phase2,
    "Phase3":Phase3,
    "J1":J1,
    "Mada":Mada
    }
points = ["SportsComplex","ParkingLot"]
x = Routes["Siwaka"].get("Ph1.B")

k = "Siwaka"
a, b = UCS(Routes, points)
print(a)
print(b)
G = nx.Graph()

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
sizes_red = [7500, 2000, 1700, 1700, 1500, 4500]

pos = nx.get_node_attributes(G, 'pos')
nx.draw(G,pos,with_labels=1,node_size=500)
nx.draw_networkx_nodes(G,pos,node_size=sizes)
nx.draw_networkx_nodes(G,pos,node_color="tab:red",nodelist=a,node_size=sizes_red)
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

