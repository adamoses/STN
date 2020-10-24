import numpy as np
import copy


####################################################################################
# STN.py
# This file contains the class STN and methods associated with the class STN
#
# STN objects have instance variables representing 
#
#  [int]                               - number of time points 
#  [int]                               - number of edges 
#  [np.array(to_names)]                - names of the time points 
#  [dict]                              - a hash table for lookup of time points
#  [np.array(dicts)                    - predecessor and 
#  [np.array(dicts)                    - successor hash tables for each node
#  [np.matrix(shape=(num_tp, num_tp))] - a distance matrix
#  [bool]                              - a flag to indicate if the distance matrix is updated
#
#  This file depends on numpy and copy
#
####################################################################################

class STN():


############################################################################################################
# - STN(num_tp, num_edges, tp_names, ord_edges, name_list=False, edge_list=False) : 
#
#         num_tp - an int representing the number of time points in the STN
#
#
#         num_edges - an int representing the number of edges in the STN
#
#
#         tp_names - a list of strings representing the names of time points (['A' 'B' 'C'])
#  
#                                   or when name_list = False
#
#                    a string representing the names of time points ('A B C')
#
#
#         ord_edges - an array of lists representing edges (['from_tp' cost 'to_tp']) where from_tp and 
#                     to_tp are the strings representing the time points
#
#                                   or when edge_list = False
#
#                     an array of strings representing edges ('from_tp cost to_tp') where from_tp and 
#                     to_tp are the strings representing the time points
#         
#
#    Initializes the STN object
#
#    Returns: nothing
############################################################################################################

    def __init__(self, num_tp, num_edges, tp_names, ord_edges, name_list=False, edge_list=False):

        self.__num_tp = num_tp         
        self.__num_edges = num_edges
        if not name_list and (not tp_names == ''):
            self.__tp_names = tp_names.split(' ')  
        elif not tp_names == '':
            self.__tp_names = tp_names
        else:
            self.__tp_names = None   

        self.__tp_hash = {}          
        self.__succs = np.array([])  
        self.__preds = np.array([])
        self.__dist_matrix = np.zeros(shape=(self.__num_tp, self.__num_tp)) + np.inf
        self.__dist_mat_updated = False
        self.__ordered_edges = []

        for i in np.arange(num_tp):
            self.__succs = np.append(self.__succs, {})
            self.__preds = np.append(self.__preds, {})
            self.__tp_hash[i] = self.__tp_names[i]

         
        for i in np.arange(num_edges):
            string = ord_edges[i]
            if not edge_list:
                self.insert_edge(string.split(' '))
            else: 
                self.insert_edge(string)


############################################################################################################
# - STN.insert_tp(name) : 
#
#         name - a string representing the new time point's name ('A')
#
#   inserts the new time point into the STN object, updating necessary fields of the object
#
#   Returns: nothing
############################################################################################################

    def insert_tp(self,name):
        self.__num_tp += 1
        self.__tp_names = np.append(self.__tp_names, name)
        self.__tp_hash[self.__num_tp-1] = name
        self.__preds = np.append(self.__preds, {})
        self.__succs = np.append(self.__succs, {})

        dist = self.get_dist_mat()
        newDist = np.zeros(shape=(self.__num_tp, self.__num_tp)) + np.inf

        mybool = np.logical_not(dist == np.inf)

        newDist[mybool] = dist[mybool]
        self.update_distances(newDist)
        self.__dist_mat_updated = False


############################################################################################################
# - STN.insert_edge(edge, string=True) :
#
#         edge - an array formatted as ['from_tp' cost 'to_tp']
#                where from_tp and to_tp are the strings representing the time points
#
#                                       or when string=False
#
#                an array formatted as ['from_tp_int' cost 'to_tp_int']
#                which uses ints instead to reference the time points
#
#   inserts the new edge into the STN object if there doesn't already exist an edge with a smaller constraint, 
#   updating all necessary fields of the object
#
#   Returns: nothing  
############################################################################################################

    def insert_edge(self, edge, string=True):
        if string:
            from_tp = self.find_tp(edge[0])
            cost = int(edge[1])
            to_tp = self.find_tp(edge[2])
        else:
            from_tp = edge[0]
            cost = edge[1]
            to_tp = edge[2]

        if (not self.__succs[from_tp].get(to_tp)) or (self.__succs[from_tp][to_tp] > cost):
            self.__succs[from_tp][to_tp] = cost
            self.__preds[to_tp][from_tp] = cost
            self.__dist_mat_updated = False
            if string:
                self.__ordered_edges.append(edge)
            else:
                self.__ordered_edges.append([self.find_tp(from_tp, string=False),str(cost),self.find_tp(to_tp, string=False)])


############################################################################################################
# - STN.find_tp(name, string=True) :
#
#         name - the name of the time point as a string ('A'), will return the time point's int (0) 
#
#                                       or when string=False
#
#                the int representing the time point (0), will return the time point's string ('A')
#
#   used to reference equivalent representations of time points
#
#   Returns: either string or int representation of time point, or None if it doesn't exist
#                  ex: 'A' or 0
############################################################################################################

    def find_tp(self, name, string=True):

        if string:
            for tp in np.arange(self.__num_tp):
                if(self.__tp_hash[tp] == name ):
                    return tp
        else:
            return self.__tp_hash[tp]

        return None


############################################################################################################
# - STN.update_distances(distMat) :
#
#         distMat - the updated distance matrix for the STN object [np matrix with shape (num_tp, num_tp)]
#
#   updates the distance matrix for the STN, sets the flag for updated distance matrix to true
#
#   Returns: nothing
############################################################################################################

    def update_distances(self, distances):
        self.__dist_matrix = distances
        self.__dist_mat_updated = True


############################################################################################################
# - STN.update_succs(succs) :
#
#         succs - the updated successor array 
#         preds = np.array(len=num_tp) | succs[i] = {1:6, 4:2}. Time point i  
#                 has successors 1 and 4 with distances 6 and 2 respectively
#
#   updates the successor array for STN
#
#   Returns: nothing
############################################################################################################

    def update_succs(self, succsessors):
        self.__succs = succsessors


############################################################################################################
# - STN.update_preds(preds) :
#
#         preds - the updated predecessor array 
#         preds = np.array(len=num_tp) | preds[i] = {1:6, 4:2}. Time point i  
#                 has predecessors 1 and 4 with distances 6 and 2 respectively
#
#   updates the predecessor array for STN
#
#   Returns: nothing
############################################################################################################

    def update_preds(self, predescessors):
        self.__preds = predescessors


####################################################################################
# - naive_update_distances(STN, newEdge) :
#
#           STN - an STN object
#
#           newEdge - a string representing an edge 
#
#       Returns: an updated distance matrix after checking if adding the new edge creates a
#                   new shortest distance between each pair of two nodes
####################################################################################

    def naive_update_distances(self, newEdge):
        dist = self.get_dist_mat()
        num_tp = self.get_num_tp()
        edge = newEdge.split(' ')
        from_tp = self.find_tp(edge[0])
        cost = int(edge[1])
        to_tp = self.find_tp(edge[2])

        for u in np.arange(num_tp):
            for v in np.arange(num_tp):
                dist[u][v] = min(dist[u][v], dist[u][from_tp]+cost+dist[to_tp][v])
                #print(dist[u][v])

        self.insert_edge(newEdge.split(' '))
        self.update_distances(dist)

        

        return dist

############################################################################################################
# - STN retrieval functions :
#
#   The following methods simply return a COPY for each  
############################################################################################################
    def get_num_tp(self):
        return self.__num_tp+0

    def get_num_edges(self):
        return self.__num_edges+0

    def get_ordered_edges(self):
        return copy.deepcopy(self.__ordered_edges)

    def get_succs(self):
        return copy.deepcopy(self.__succs)

    def get_preds(self):
        return copy.deepcopy(self.__preds)

    def get_names(self):
        return copy.copy(self.__tp_names)

    def get_hash(self):
        return self.__tp_hash.copy()

    def get_dist_mat(self):
        return copy.deepcopy(self.__dist_matrix)

    def get_dist_mat_upd(self):
        return self.__dist_mat_updated

    def copy(self):
        return STN(self.get_num_tp(), self.get_num_edges(), self.get_names(), self.get_ordered_edges(), name_list=True, edge_list=True)

