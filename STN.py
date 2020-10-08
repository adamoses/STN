import numpy as np

class STN():

    def __init__(self, num_tp, num_edges, tp_names, ord_edges):

        ''' 
        Constructor for STN
        Inputs:
        num_tp        -       num of time points (int)
        num_edges     -       num of edges (int)
        tp_names      -       string of time point names 
        ord_edges     -       numpy array of strings
                              fmt = "from_tp cost to_tp"
        '''

        self.__num_tp = num_tp         
        self.__num_edges = num_edges
        self.__tp_names = tp_names.split(' ')     
        self.__tp_hash = {}          # initilizing empty dictionary
                                     # for STN data structure
        self.__succs = np.array([])  # initializing empty array
                                     # each index will hold succ dict for 
                                     # each time point
        self.__preds = np.array([])
        self.__dist_matrix = np.zeros(shape=(self.__num_tp, self.__num_tp)) + np.inf
        self.__dist_mat_updated = False

        for i in np.arange(num_tp):
            self.__succs = np.append(self.__succs, {})
            self.__preds = np.append(self.__preds, {})
            self.__tp_hash[i] = self.__tp_names[i]

         
        for i in np.arange(num_edges):
            string = ord_edges[i]
            self.insert_edge(string.split(' '))


    def update_distances(self, distances):
        self.__dist_matrix = distances
        self.__dist_mat_updated = True

    def update_succs(self, succsessors):
        self.__succs = succsessors

    def update_preds(self, predescessors):
        self.__preds = predescessors

    def find_tp(self, name):

        for tp in np.arange(self.__num_tp):
            if(self.__tp_hash[tp] == name ):
                return tp

        return None

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


    def get_num_tp(self):
        return self.__num_tp+0

    def get_num_edges(self):
        return self.__num_edges+0

    def get_succs(self):
        return self.__succs.copy()

    def get_preds(self):
        return self.__preds.copy()

    def get_names(self):
        return self.__tp_names[:]

    def get_hash(self):
        return self.__tp_hash.copy()

    def get_dist_mat(self):
        return self.__dist_matrix.copy()

    def get_dist_mat_upd(self):
        return self.__dist_mat_updated

    
