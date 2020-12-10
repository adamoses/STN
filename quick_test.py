import numpy as np
import random
from STN import *
from algo import *
from stn_parser import *

queue = ['A', 'B', 'C']
print(queue.pop())

#test update_potential
num_tp = 5
num_edges = 8
time_points = "A0 C0 A1 C1 X"
edge1 = "X 12 C0"
edge2 = "C1 11 C0"
edge3 = "C0 -7 X"
edge4 = "C0 -1 C1"
edge5 = "A0 3 C0"
edge6 = "C0 -1 A0"
edge7 = "A1 10 C1"
edge8 = "C1 -1 A1"
edge_list = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8]
stn1 = STN(num_tp, num_edges, time_points, edge_list)

stn1.update_distances(floyd_warshall(stn1))
dist_mat = stn1.get_dist_mat()

test_node = "X"

print(to_string(stn1))
print("==========================\n")
print(dist_mat)
print("==========================\n")

#test bf
dist = bellman_ford(stn1, 0)
print("dist: ", dist)

#actual test
update_dist = update_potential(stn1, dist, test_node)
print("updated dist: ", update_dist)
#stn1.update_distances(update_dist)

