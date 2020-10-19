from STN import STN
import numpy as np

## Accepts sink and source nodes
## Sink nodes edge: 'node 0 node'
## Source: 'node 0 first_node'

def BellmanFord(stn, src):  
  
    succ = stn.get_succs()
    num_tp = stn.get_num_tp()
    
    # Step 1: Initialize distances from src to all other vertices  
    # as INFINITE  
    dist = [float("Inf")] * (num_tp)
    dist[src] = 0
    
    # Step 2: Relax all edges |V| - 1 times. A simple shortest  
    # path from src to any other vertex can have at-most |V| - 1  
    # edges  
    
    for u, hash_table in enumerate(succ):
        # Update dist value and parent index of the adjacent vertices of  
        # the picked vertex. Consider only those vertices which are still in  
        # queue  
        for key in hash_table:  
            if dist[u] != float("Inf") and dist[u] + hash_table[key] < dist[key]:  
                dist[key] = dist[u] + hash_table[key]  
        # Step 3: check for negative-weight cycles. The above step  
        # guarantees shortest distances if graph doesn't contain  
        # negative weight cycle. If we get a shorter path, then there  
        # is a cycle.  
        for key in hash_table:  
            if dist[u] != float("Inf") and dist[u] + hash_table[key] < dist[key]:  
                print("Graph contains negative weight cycle") 
                return

    print(dist)

names = 'A0 C0 A1 C1 X'

edge1 = 'X 12 C0'
edge2 = 'C1 11 C0'
edge3 = 'C0 -7 X'
edge4 = 'C0 -1 C1'
edge5 = 'A0 3 C0'
edge6 = 'C0 -1 A0'
edge7 = 'A1 10 C1'
edge8 = 'C1 -1 A1'

edges = np.array([edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8])
test_stn = STN(5, 8, names, edges)

BellmanFord(test_stn, 0)

# For testing random node_orderings
# import random
# random.shuffle(array)
# also takes in node ordering input
# consistency check (test on consistent and non-consistent STN)
# node ordering is an array of numbers representing the time points of the given STN
def DPC(stn, node_ordering):
    succs = stn.get_succs()
    preds = stn.get_preds()
    # num_tp = stn.get_num_tp()
    dist = stn.get_dist_mat()

    # Traversing the nodes in reverse order
    for k in reversed(node_ordering):
        # Look for incoming edges we iterate through the keys
        for i in preds[k].keys():
            #for the edges before Yk 
            if i < k :
                # process pred 
                dist[i][k] = preds[k][i]
                # Look for outgoing edges
                for j in succs[k].keys():
                    #for the edges before Yk
                    if j < k :
                        # process succ
                        dist[k][j] = succs[k][j]
                        # insert new 2 path edge
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) 
                        # check for negative cycle
                        if dist[i][j] != float("Inf") and dist[j][i] != float("Inf") and dist[i][j] + dist[j][i] < 0:
                            print("Graph contains negative weight cycle") 
                            print(dist)
                            return False
    print("DPC: \n", dist)
    return True

names = 'A0 C0 A1 C1 X'

edge1 = 'X 12 C0'
edge2 = 'C1 11 C0'
edge3 = 'C0 -7 X'
edge4 = 'C0 -1 C1'
edge5 = 'A0 3 C0'
edge6 = 'C0 -1 A0'
edge7 = 'A1 10 C1'
edge8 = 'C1 -1 A1'

edges = np.array([edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8])
test_stn = STN(5, 8, names, edges)

DPC(test_stn)

edge1 = 'X -12 C0'
edge2 = 'C1 -11 C0'
edge3 = 'C0 -7 X'
edge4 = 'C0 -1 C1'
edge5 = 'A0 -3 C0'
edge6 = 'C0 -1 A0'
edge7 = 'A1 -10 C1'
edge8 = 'C1 -1 A1'

edges = np.array([edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8])
test_stn = STN(5, 8, names, edges)
DPC(test_stn)

