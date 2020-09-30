from STN import STN
import numpy as np

def succ_to_array(STN):
    succ = STN.get_succs()
    # print(succ)
    ret_arr = []
    counter = 0
    for hash_table in succ:
        for key in hash_table:
            temp_arr = [counter]
            temp_arr.append(key)
            temp_arr.append(hash_table[key])
            ret_arr.append(temp_arr)
        counter += 1
    # print(ret_arr)
    return ret_arr

#takes in STN and source point, where src is <= # time points - 1
def BellmanFord(self, src):  
  
    # Step 1: Initialize distances from src to all other vertices  
    # as INFINITE  
    dist = [float("Inf")] * self.get_num_tp()
    dist[src] = 0
    
  
    # Step 2: Relax all edges |V| - 1 times. A simple shortest  
    # path from src to any other vertex can have at-most |V| - 1  
    # edges  
    for _ in range(self.get_num_tp() - 1):  
        # Update dist value and parent index of the adjacent vertices of  
        # the picked vertex. Consider only those vertices which are still in  
        # queue  
        for u, v, w in succ_to_array(self):  
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:  
                dist[v] = dist[u] + w  
  
        # Step 3: check for negative-weight cycles. The above step  
        # guarantees shortest distances if graph doesn't contain  
        # negative weight cycle. If we get a shorter path, then there  
        # is a cycle.  
  
        for u, v, w in succ_to_array(self):  
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:  
                print("Graph contains negative weight cycle") 
                return

    self.print(dist)

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

BellmanFord(test_stn, test_stn.get_num_tp() - 1)