import numpy as np
from STN import *
from algo import *
from stn_parser import *

# List of files containing STNs on which to run tests
filelist = ['stn1.stn','stn2.stn','stn3.stn','stn4.stn','stn5.stn']

def prop_test(file):

    # Create 2 identical STNs from file
    STN1 = STN_parser(file)
    STN2 = STN1.copy()

    # Compute and update distance matrix for STN1
    fw1 = floyd_warshall(STN1)
    STN1.update_distances(fw1)

    # Insert new edge to STN2 and compute and update STN2's distance matrix from scratch
    edge = ['D',4,'E']
    STN2.insert_edge(edge)
    fw2 = floyd_warshall(STN2)

    # Assert each index is identical in STN2's distance matrix 
    # and the distance matrix that returns from prop_fwd_prop_bkwd given STN1 and new edge
    return np.all(prop_fwd_prop_bkwd(STN1, edge) == fw2)


#for each sample STN file, assert each test is true
for file in filelist:
    assert(prop_test('sample_STNs/'+file))


#test on stn2
def naive_test(file_1):
    stn_1 = string_to_stn(file_1)
    edge = "A 43 B"
    stn_1.update_distances(floyd_warshall(stn_1))
    print(stn_1.get_dist_mat())
    stn_1.naive_update_distances(edge)
    print(stn_1.get_dist_mat())

file_location = "C://Users\gptacekLaptop\Downloads\Vassar\Sem5\cmpu382\code\STN\sample_STNs\stn2.stn"
naive_test(file_location)