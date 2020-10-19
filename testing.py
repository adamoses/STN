import numpy as np
import random
from STN import *
from algo import *
from stn_parser import *
import os

directory = 'C:\\Users\\Cameron\\Desktop\\STN\\STN\\sample_STNs'

def dpc_test(file):
    stn = stringToSTN(file)
    node_ordering = stn.get_names()
    counter = 0

    for x in node_ordering:
        node_ordering[counter] = counter
        counter = counter + 1
    random.shuffle(node_ordering)

    dpc(stn, node_ordering)

def test_sample_stns():
    for file in os.listdir(directory):
        dpc_test(file)

test_sample_stns()

# def prop_test(file):
#     STN1 = stringToSTN(file)
#     STN2 = STN1.copy()

#     fw1 = floyd_warshall(STN1)
#     STN1.update_distances(fw1)

#     edge = ['D',4,'E']
#     STN2.insert_edge(edge)
#     fw2 = floyd_warshall(STN2)
#     return np.all(prop_fwd_prop_bkwd(STN1, edge) == fw2)

# for file in filelist:
#     assert(prop_test('sample_STNs/'+file))


# names = 'A B C D E'
# e1 = 'A 9 C'
# e2 = 'D -3 A'
# e3 = 'B 8 A'
# e4 = 'C 5 B'
# e5 = 'E -7 C'
# e6 = 'B 4 D'
# edges = np.array([e1,e2,e3,e4,e5,e6])

# s = STN(5,6,names,edges)
# s.update_distances(floyd_warshall(s))
# edge = ['D',4,'E']

# print(prop_fwd_prop_bkwd(s, edge))

# names = 'A0 C0 A1 C1 X'

# edge1 = 'X 12 C0'
# edge2 = 'C1 11 C0'
# edge3 = 'C0 -7 X'
# edge4 = 'C0 -1 C1'
# edge5 = 'A0 3 C0'
# edge6 = 'C0 -1 A0'
# edge7 = 'A1 10 C1'
# edge8 = 'C1 -1 A1'

# edges = np.array([edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8])
# test_stn = STN(5, 8, names, edges)

# BellmanFord(test_stn, 0)

# names = 'A0 C0 A1 C1 X'

# edge1 = 'X 12 C0'
# edge2 = 'C1 11 C0'
# edge3 = 'C0 -7 X'
# edge4 = 'C0 -1 C1'
# edge5 = 'A0 3 C0'
# edge6 = 'C0 -1 A0'
# edge7 = 'A1 10 C1'
# edge8 = 'C1 -1 A1'

# edges = np.array([edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8])
# test_stn = STN(5, 8, names, edges)

# DPC(test_stn)

# edge1 = 'X -12 C0'
# edge2 = 'C1 -11 C0'
# edge3 = 'C0 -7 X'
# edge4 = 'C0 -1 C1'
# edge5 = 'A0 -3 C0'
# edge6 = 'C0 -1 A0'
# edge7 = 'A1 -10 C1'
# edge8 = 'C1 -1 A1'

# edges = np.array([edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8])
# test_stn = STN(5, 8, names, edges)
# DPC(test_stn)

