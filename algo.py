from STN import STN
import numpy as np
from util import *

def floyd_warshall(STN):

    num_tp = STN.get_num_tp()
    distanceMatrix = np.zeros(shape=(num_tp, num_tp)) + np.inf
    successors = STN.get_succs()

    for succ_dict in np.arange(num_tp):
        for key in successors[succ_dict].keys():
            distanceMatrix[succ_dict][key] = successors[succ_dict][key]

    for i in np.arange(num_tp):
        for j in np.arange(num_tp):
            for k in np.arange(num_tp):
                distanceMatrix[j][k] = min(distanceMatrix[j][k], 
                                           distanceMatrix[j][i] + distanceMatrix[i][k])

    return distanceMatrix
    

def dijkstra(STN, src, src_string=False):

    distances = np.zeros(STN.get_num_tp())+np.inf
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

#takes in STN and source point, where src is <= # time points - 1
def BellmanFord(stn, src):  

    ## Arrange edges into a readable array for BellmanFord
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
  
    succ = succ_to_array(stn)
    num_tp = stn.get_num_tp()
    
    # Step 1: Initialize distances from src to all other vertices  
    # as INFINITE  
    dist = [float("Inf")] * num_tp
    dist[src] = 0
    
    # Step 2: Relax all edges |V| - 1 times. A simple shortest  
    # path from src to any other vertex can have at-most |V| - 1  
    # edges  
    for _ in range(num_tp - 1):  
        # Update dist value and parent index of the adjacent vertices of  
        # the picked vertex. Consider only those vertices which are still in  
        # queue  
        #print("Step 2:")
        for u, v, w in succ:  
            #print(str(dist[u]) + " + " + str(w) + " < " + str(dist[v]))
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:  
                dist[v] = dist[u] + w  
                #print(dist[v])
        #print(dist)
        # Step 3: check for negative-weight cycles. The above step  
        # guarantees shortest distances if graph doesn't contain  
        # negative weight cycle. If we get a shorter path, then there  
        # is a cycle.  
        #print("Step 3:")
        for u, v, w in succ:  
            #print(str(dist[u]) + " + " + str(w) + " < " + str(dist[v]))
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:  
                print("Graph contains negative weight cycle") 
                return

    return(dist)

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
BellmanFord(test_stn, 0)
