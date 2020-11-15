import numpy as np
import copy


####################################################################################
# STNU.py
# This file contains the class STNU and methods associated with the class STNU
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

class STNU():


    def __init__(self, num_tp, num_edges, num_cont_links, tp_names, ord_edges, contingent_links, name_list=False, edge_list=False):
    
        self.__num_tp = num_tp         
        self.__num_edges = num_edges
        self.__num_cont_links = num_cont_links
        if not name_list and (not tp_names == ''):
            self.__tp_names = tp_names.split(' ')  
        elif not tp_names == '':
            self.__tp_names = tp_names
        else:
            self.__tp_names = None   

        self.__tp_hash = {}          
        self.__succs = np.array([])  
        self.__preds = np.array([])
        self.__cont_succs = np.array([])
        self.__cont_preds = np.array([])
        self.__dist_matrix = np.zeros(shape=(self.__num_tp, self.__num_tp)) + np.inf
        self.__dist_mat_updated = False
        self.__ordered_edges = []
        self.__cont_links = []

        for i in np.arange(num_tp):
            self.__succs = np.append(self.__succs, {})
            self.__preds = np.append(self.__preds, {})
            self.__cont_succs = np.append(self.__succs, {})
            self.__cont_preds = np.append(self.__preds, {})
            self.__tp_hash[i] = self.__tp_names[i]

         
        for i in np.arange(num_edges):
            string = ord_edges[i]
            if not edge_list:
                self.insert_edge(string.split(' '))
            else: 
                self.insert_edge(string)

        for i in np.arange(num_cont_links):
            string = contingent_links[i]
            if not edge_list:
                self.insert_cont_link(string.split(' '))
            else: 
                self.insert_cont_link(string)

    def insert_tp(self,name):
        self.__num_tp += 1
        self.__tp_names = np.append(self.__tp_names, name)
        self.__tp_hash[self.__num_tp-1] = name
        self.__preds = np.append(self.__preds, {})
        self.__succs = np.append(self.__succs, {})
        self.__cont_preds = np.append(self.__preds, {})
        self.__cont_succs = np.append(self.__succs, {})

        dist = self.get_dist_mat()
        newDist = np.zeros(shape=(self.__num_tp, self.__num_tp)) + np.inf

        mybool = np.logical_not(dist == np.inf)

        newDist[mybool] = dist[mybool]
        self.update_distances(newDist)
        self.__dist_mat_updated = False

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

    def insert_cont_link(self, edge, string=True):
        if string:
            from_tp = self.find_tp(edge[0])
            x = int(edge[1])
            y = int(edge[2])
            to_tp = self.find_tp(edge[3])
        else:
            from_tp = edge[0]
            x = edge[1]
            y = edge[2]
            to_tp = edge[3]

        if (not self.__succs[from_tp].get(to_tp)) or (self.__succs[from_tp][to_tp] > x):
            self.__cont_succs[from_tp][to_tp] = (x, y)
            self.__cont_preds[to_tp][from_tp] = (x, y)
            self.__dist_mat_updated = False
            if string:
                self.__cont_links.append(edge)
            else:
                self.__cont_edges.append([self.find_tp(from_tp, string=False),str(x), str(y),self.find_tp(to_tp, string=False)])

    def find_tp(self, name, string=True):

        if string:
            for tp in np.arange(self.__num_tp):
                if(self.__tp_hash[tp] == name ):
                    return tp
        else:
            return self.__tp_hash[tp]

        return None

    def update_distances(self, distances):
        self.__dist_matrix = distances
        self.__dist_mat_updated = True

    def update_succs(self, succsessors):
        self.__succs = succsessors
        
    def update_preds(self, predescessors):
        self.__preds = predescessors

############################################################################################################
# - STNU retrieval functions :
#
#   The following methods simply return a COPY for each  
############################################################################################################
    def get_num_tp(self):
        return self.__num_tp+0

    def get_num_edges(self):
        return self.__num_edges+0

    def get_num_cont_links(self):
        return self.__num_cont_links+0

    def get_ordered_edges(self):
        return copy.deepcopy(self.__ordered_edges)

    def get_cont_links(self):
        return copy.deepcopy(self.__cont_links)

    def get_succs(self):
        return copy.deepcopy(self.__succs)

    def get_preds(self):
        return copy.deepcopy(self.__preds)

    def get_cont_succs(self):
        return copy.deepcopy(self.__cont_succs)

    def get_cont_preds(self):
        return copy.deepcopy(self.__cont_preds)

    def get_names(self):
        return copy.copy(self.__tp_names)

    def get_hash(self):
        return self.__tp_hash.copy()

    def get_dist_mat(self):
        return copy.deepcopy(self.__dist_matrix)

    def get_dist_mat_upd(self):
        return self.__dist_mat_updated and True

    def copy(self):
        return STNU(self.get_num_tp(), self.get_num_edges(), self.get_num_cont_links(), \
            self.get_names(), self.get_ordered_edges(), self.get_cont_links(), name_list=True, edge_list=True)

