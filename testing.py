import numpy as np
from STN import *
from algo import *
from parser import *

filelist = ['stn1.stn','stn2.stn','stn3.stn','stn4.stn','stn5.stn']

def prop_test(file):
    STN1 = STN_parser('sample_STNs/'+file)
    STN2 = STN1.copy()

    fw1 = floyd_warshall(STN1)
    STN1.update_distances(fw1)

    edge = ['D',4,'E']
    STN2.insert_edge(edge)
    fw2 = floyd_warshall(STN2)
    return np.all(prop_fwd_prop_bkwd(STN1, edge) == fw2)

for file in filelist:
    assert(prop_test(file))