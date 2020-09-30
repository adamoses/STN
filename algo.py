from stn import STN
import numpy as np
from util import *

def dijkstra(STN, src, src_string=False):

    distances = np.ones(STN.get_num_tp())*np.inf
    successors = STN.get_succs()
    visited = []
    
    if src_string:
        source = STN.find_tp(src)
    else:
        source = src
    
    distances[source] = 0

    p_queue = PriorityQueue()
    visited.append(source)
    p_queue.push(source, distances[source])

    while not p_queue.isEmpty():
        node = p_queue.pop()
        visited.append(node)
        for succ in successors[node].keys():
            if not succ in visited:
                distances[succ] = min(distances[succ], distances[node]+successors[node][succ])
                p_queue.update(succ, distances[succ])
                

    return distances


#turns successor array of dictionary into 2d array of the form (from_tp, to_tp, edge_val) for easier processing by bellman_ford
def succ_to_array(STN):
    succ = STN.get_succs()
    print(succ)
    ret_arr = []
    counter = 0
    for hash_table in succ:
        for key in hash_table:
            temp_arr = [counter]
            temp_arr.append(key)
            temp_arr.append(hash_table[key])
            ret_arr.append(temp_arr)
        counter += 1
    print(ret_arr)

#takes in STN and source point, where src is <= # time points - 1
def bellman_ford(self, src):  
  
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
        for u, v, w in self.ord_edges:  
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:  
                dist[v] = dist[u] + w  
  
        # Step 3: check for negative-weight cycles. The above step  
        # guarantees shortest distances if graph doesn't contain  
        # negative weight cycle. If we get a shorter path, then there  
        # is a cycle.  
  
        for u, v, w in self.graph:  
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:  
                print("Graph contains negative weight cycle") 
                return

    #self.print(dist)


names = 'A0 C0 A1 C1 X'

edge1 = 'X 12 C0'
edge2 = 'C1 11 C0'
edge3 = 'C0 -7 X'
edge4 = 'C0 -1 C1'
edge5 = 'A0 3 C0'
edge6 = 'C0 -1 A0'
edge7 = 'A1 10 C1'
edge8 = 'C1 -1 A1'

name1 = 'A B C D E'
e1 = 'A 2 B'
e2 = 'B 12 D'
e3 = 'D 3 A'
e4 = 'A 4 E'
e5 = 'E 7 C'
e6 = 'C 9 E'
e7 = 'C 1 D'

edges1 = np.array([e1,e2,e3,e4,e5,e6,e7])

edges = np.array([edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8])

test_stn = STN(5, 8, names, edges)

succ_to_array(test_stn)
testSTN = STN(5, 8, names, edges)
t1STN = STN(5, 7, name1, edges1)

#pred_to_array(testSTN)

print(dijkstra(t1STN, 'A', src_string=True))
