import numpy as np

class STN():

    def __init__(self, num_tp, num_edges, tp_names, ord_edges):

        ''' 
        Constructor for STN
        Inputs:
        num_tp        -       num of time points (int)
        num_edges     -       num of edges (int)
        tp_names      -       array of time point names (string array)
        ord_edges     -       array of arrays 
                                fmt = [from_tp cost to_tp]

        '''

        # Example of calling STN()
        # STN(5, 8, [A0, C0, A1, C1, X], [[X, 12, C0], [C1, 11, C0], ...])

        self.__num_tp = num_tp         
        self.__num_edges = 0  
        self.__tp_names = tp_names     
        self.__tp_hash = {}            # initilizing empty dictionary
                                     # for STN data structure
        self.__succs = np.array([])    # initializing empty array
                                     # each index will hold succ dict for 
                                     # each time point

        for i in np.arange(num_tp):
            self.__tp_hash[i] = self.__tp_names[i]

        # example succs array for X
        # {'C0': -7, 'C1':  }

        #for edge in ord_edges:
            #print(str(edge)+'\n\n')
            #self.__insert_edge(ord_edges[i])

        self.__insert_edge(ord_edges[0])

    def __insert_edge(edge): #fmt = [from_tp (tp - not the name) cost to_tp (tp - not the name)]:

        from_tp = self.__find_tp(edge[0])
        cost = edge[1]
        to_tp = self.__find_tp(edge[2])

        __succs[from_tp][to_tp] = cost

    def __find_tp(name):

        for tp in np.arange(num_tp):
            if(__tp_hash[tp] == name ):
                return tp

        return None


names = np.array(['A0', 'C0', 'A1', 'C1', 'X'])

edge1 = np.array(['X', 12, 'C0'])
edge2 = np.array(['C1', 11, 'C0'])
edge3 = np.array(['C0', -7, 'X'])
edge4 = np.array(['C0', -1, 'C1'])
edge5 = np.array(['A0', 3, 'C0'])
edge6 = np.array(['C0', -1, 'A0'])
edge7 = np.array(['A1', 10, 'C1'])
edge8 = np.array(['C1', -1, 'A1'])

edges = np.array([edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8])
STN(5, 8, names, edges)
