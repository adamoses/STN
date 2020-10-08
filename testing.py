import numpy as np
from STN import *
from algo import *
from parser import *

names = 'A B C D E'
e1 = 'A 9 C'
e2 = 'B 4 D'
e3 = 'B 8 A'
e4 = 'C 5 B'
e5 = 'D -3 A'
e6 = 'E -7 C'
edges = np.array([e1,e2,e3,e4,e5,e6])

STN1 = STN(5,6,names,edges)
STN2 = STN(5,6,names,edges)

fw1 = floyd_warshall(STN1)
STN1.update_distances(fw1)

edge = ['D',4,'E']

STN2.insert_edge(edge)
fw2 = floyd_warshall(STN2)

print(prop_fwd_prop_bkwd(STN1, edge))