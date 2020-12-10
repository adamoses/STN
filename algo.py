from STN import STN
import numpy as np
from queue import *
from util import *

####################################################################################
# algo.py
# This file contains algorithms to be run on STN objects
#
# floyd_warshall()         - runs Floyd Warshall's algorithm
#
# naive_update_distances() -
#
# dijkstra()               - runs Dijkstra's algorithm
#
# bellman_ford()           - runs Bellman Ford's algorithm
#
# dpc()                    - runs the Directed Path Consistency search

# prop_fwd_prop_bkwd()     - forward and then backward propagates new edge to update
#                            distance matrix

# update_potential()       - updated the potential function/distance matrix and adds tightened edges to the stn
#
#
# none of the methods called in this file make any changes to the STN object which they are passed
#
# this file depends on numpy and queue
#
####################################################################################


####################################################################################
# - floyd_warshall(STN) :
#
#           STN - an STN object
#
#       Returns: a fully computed distance matrix
####################################################################################

def floyd_warshall(STN):

    num_tp = STN.get_num_tp()
    distanceMatrix = np.zeros(shape=(num_tp, num_tp)) + np.inf
    successors = STN.get_succs()

    for succ_dict in np.arange(num_tp):
        distanceMatrix[succ_dict][succ_dict] = 0
        for key in successors[succ_dict].keys():
            distanceMatrix[succ_dict][key] = successors[succ_dict][key]

    for i in np.arange(num_tp):
        for j in np.arange(num_tp):
            for k in np.arange(num_tp):
                distanceMatrix[j][k] = min(distanceMatrix[j][k],
                                           distanceMatrix[j][i] + distanceMatrix[i][k])


    return distanceMatrix



####################################################################################
# - dijkstra(STN, node, string=False, sink=False) :
#
#           STN - an STN object
#
#           node - a string representing the node from which to calculate distances
#
#           string - a bool stating whether the node is specified using a string ('A') (string=True)
#                    or with the int that represents the time point (0) (string=False)
#
#           sink - a bool indicating whether to calculate the distances from the given
#                  node to all the others (sink=False) or to the given node from every other (sink=True)
#
#       Returns: an array describing the distance between the source (or sink) node to each other node
#                such that dijkstra(STN, 0)[i] equals the distance from node 0 to node i
####################################################################################

def dijkstra(STN, node, string=False, sink=False):

    distances = np.zeros(STN.get_num_tp())+np.inf
    visited = []

    if sink:
        nextNodes = STN.get_preds()
    else:
        nextNodes = STN.get_succs()

    if string:
        rnode = STN.find_tp(node)
    else:
        rnode = node

    distances[rnode] = 0

    p_queue = PriorityQueue()
    visited.append(rnode)
    p_queue.put((distances[rnode], rnode))

    while not p_queue.empty():
        node = p_queue.get()[1]
        visited.append(node)
        for succ in nextNodes[node].keys():
            if not succ in visited:
                distances[succ] = min(distances[succ], distances[node]+nextNodes[node][succ])
                p_queue.put((distances[succ], succ))
                if nextNodes[node][succ] < 0:
                    print('\nDijkstra\'s algorithm can not be used on networks with negative weight edges.\n')
                    return

    return distances

## Accepts sink and source nodes
## Sink nodes edge: 'node 0 node'
## Source: 'node 0 first_node'

####################################################################################
# - bellman_ford(stn, src) :
#
#           stn - an STN object
#
#           src - integer representing the time point being used as source node
#
#       Returns: distance array
####################################################################################

# bellman_ford
# only change loops to check all edges

def bellman_ford(stn, src):

    num_tp = stn.get_num_tp()
    dist = [float("Inf")] * (num_tp)
    dist[src] = 0

    for _ in range(num_tp -1):
        for u, s, v in stn.get_ordered_edges():
            u = stn.find_tp(u)
            s = int(s)
            v = stn.find_tp(v)
            #print("u, s, v: ", u, s, v)
            if dist[u] != float("Inf") and dist[u] + s < dist[v]:
                dist[v] = dist[u] + s

    for u, s, v in stn.get_ordered_edges():
        u = stn.find_tp(u)
        s = int(s)
        v = stn.find_tp(v)
        if dist[u] != float("Inf") and dist[u] + s < dist[v]:
            print("Graph contains negative weight cycle")
            return False

    return (dist)
    
####################################################################################
# - dpc(STN, node_ordering) :
#
#           stn - an STN object
#
#           node_ordering - an array of ints representing the time points of the given stn
#
#       Returns: False if there is a negative weight cycle and true otherwise
####################################################################################

# For testing random node_orderings
# import random
# random.shuffle(array)
# also takes in node ordering input
# consistency check (test on consistent and non-consistent STN)
# node ordering is an array of numbers representing the time points of the given STN
def dpc(stn, node_ordering):
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
                            # print(dist)
                            return False
    # print("DPC: \n", dist)
    print ("Consistent!")
    return True

def prop_fwd_prop_bkwd(STN, edge, string=True):
    if string:
        x = STN.find_tp(edge[0])
        delta = int(edge[1])
        y = STN.find_tp(edge[2])
    else:
        x = edge[0]
        delta = edge[1]
        y = edge[2]

    if not STN.get_dist_mat_upd():
        print('\nDistance Matrix Must be Updated to run prop_fwd_prop_bkwd()\n')

    dist_mat = STN.get_dist_mat()
    successors = STN.get_succs()
    predecessors = STN.get_preds()

    if dist_mat[x][y] <= delta:
        return dist_mat

    successors[x][y] = delta
    predecessors[y][x] = delta
    dist_mat[x][y] = delta

    encountered = [y]
    changed = [y]
    to_do = [y]

    if delta < -dist_mat[y][x]:
        return False

    while to_do:
        v = to_do[0]
        to_do.remove(v)
        v_succs = successors[v]

        for w in v_succs.keys():
            d = v_succs[w]
            if (not w in encountered) and (dist_mat[y][w] == d + dist_mat[y][v]):
                encountered.append(w)

                if delta+dist_mat[y][w] < dist_mat[x][w]:
                    dist_mat[x][w] = delta+dist_mat[y][w]
                    changed.append(w)
                    to_do.append(w)


    for w in changed:

        encountered = [x]
        to_do = [x]

        while to_do:
            f = to_do[0]
            to_do.remove(f)

            f_preds = predecessors[f]

            for e in f_preds.keys():

                a = f_preds[e]

                if (not e in encountered) and (dist_mat[e][x] == a + dist_mat[f][x]):

                    encountered.append(e)

                    if dist_mat[e][x] + dist_mat[x][w] < dist_mat[e][w]:
                        dist_mat[e][w] = dist_mat[e][x] + dist_mat[x][w]
                        to_do.append(e)
    return dist_mat


def Morris_2014(STNU):

    # identify negative nodes
    negative_nodes = []

    # get * nodes from normal form
    for node in STNU.contingent_tp:
        if not np.isnan(node):
            negative_nodes.append(int(node))

    # get predecessor arrays to find negative nodes from ord edges
    preds = STNU.get_preds()

    # for each node
    for node in np.arange(len(preds)):
        neg = False

        # check if it has a negative edge leading to it
        for value in preds[node].values():
            if value < 0:
                neg = True

        if neg:
            negative_nodes.append(node)

    unstarted = negative_nodes
    started = []
    finished = []


    for node in negative_nodes:
        if not morris_helper(STNU, node, unstarted, started, finished):
            return False
        

    return True


def morris_helper(STNU, node, unstarted, started, finished):
    if node in started:
        return False
    if node in finished:
        return True

    unstarted.remove(node)
    started.append(node)

    distances = np.zeros(STNU.get_num_tp())
    distances[:] = np.inf
    distances[node] = 0

    activation_nodes = []

    # get * nodes from normal form
    for n in STNU.contingent_tp:
        if not np.isnan(n):
            activation_nodes.append(int(n))

    priorityQ = PriorityQueue()

    if (node in activation_nodes):
        priorityQ.put((STNU.get_upper_case_edge(node), STNU.activation_tp[node]))
        index = int(STNU.activation_tp[node])
        distances[index] = STNU.get_upper_case_edge(node)
    else:
        preds = STNU.get_preds()
        for p in np.arange(len(preds)):
            keys = preds[p].keys()

            for key in keys:
                if preds[p][key] < 0:
                    priorityQ.put((preds[p][key], key))
                    distances[key] = preds[p][key]

    while not priorityQ.empty():
        print(priorityQ.qsize())
        u = priorityQ.get()

        if distances[int(u[1])] >= 0:
            STNU.insert_edge([int(u[1]), u[0], node], string=False)
        else:
            if (int(u[1]) in unstarted) and (morris_helper(STNU, int(u[1]), unstarted, started, finished) == False):
                return False
            preds = STNU.get_preds()
            preds_u = preds[int(u[1])]
            preds_u_keys = preds_u.keys()


            for v in preds_u_keys:
                if preds_u[v] >= 0:
                    newKey = distances[u[1]] + preds_u[v]
                    priorityQ.put((newKey, v))
                    distances[v] = newKey

    started.remove(node)
    finished.append(node)
    return True
