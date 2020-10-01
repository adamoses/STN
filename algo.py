from STN import STN
import numpy as np

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
    # changed from num_tp -1 to num_tp to account for extra source node
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