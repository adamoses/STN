import numpy as np
from STN import *
from algo import *
from parser import *

filelist = ['stn1.stn','stn2.stn','stn3.stn','stn4.stn','stn5.stn']

def prop_test(file):
    STN1 = STN_parser(file)
    STN2 = STN1.copy()

    fw1 = floyd_warshall(STN1)
    STN1.update_distances(fw1)

    edge = ['D',4,'E']
    STN2.insert_edge(edge)
    fw2 = floyd_warshall(STN2)
    return np.all(prop_fwd_prop_bkwd(STN1, edge) == fw2)

def dijk_vs_floy(file):
    s = STN_parser(file)

    fw = floyd_warshall(s)
    s.update_distances(fw)

    for t in np.arange(s.get_num_tp()):
        if not fw[t] == dijkstra(s, t):
            return False

    return True

for file in filelist:
    assert(prop_test('sample_STNs/'+file))
    #assert(dijk_vs_floy('sample_STNs/'+file))


names = 'A B C D E'
e1 = 'A 9 C'
e2 = 'D -3 A'
e3 = 'B 8 A'
e4 = 'C 5 B'
e5 = 'E -7 C'
e6 = 'B 4 D'
edges = np.array([e1,e2,e3,e4,e5,e6])

s = STN(5,6,names,edges)
s.update_distances(floyd_warshall(s))
edge = ['D',4,'E']

print(prop_fwd_prop_bkwd(s, edge))