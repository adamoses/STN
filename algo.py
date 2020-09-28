from STN import *

def predsToArray(STN):
    

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

    self.print(dist)
                          