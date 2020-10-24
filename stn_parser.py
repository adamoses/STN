import numpy as np
import sys
from STN import *
from algo import *


#will change this so user can choose
# if(len(sys.argv)!= 2):
#     print('\n\nUsage: python parser.py input_file.txt\n\n')
#     quit(0)
# else:
#     user_input = sys.argv[1]

def stringToSTN(input):
    path = "./sample_STNs/" + input

    with open(path, "r") as f:
        stn_string = f.read()

####################################################################################
# - string_to_stn(input) :
#
#           input - an standardized text input of an STN of the form:
#                       # KIND OF NETWORK
#                       STN
#                       # Num Time-Points
#                       (number of time points, eg. 5)
#                       # Num Ordinary Edges
#                       (number of ordinary edges, eg. 8)
#                       # Time-Point Names
#                       (a single line of the names of the time-points, eg. A0 C0 A1 C1 X)
#                       # Ordinary Edges
#                       (one or more lines representing the edges. These edges are represented as
#                           "from_time_point value_of_edge to_time_point", eg. X 12 C0)
#   
#       Returns: an stn object with all the values from the text file
####################################################################################

def string_to_stn(input):
    stn = open(input, "r")
    stn_string = stn.read()
    stn.close()

    
    lines_list = stn_string.splitlines()
    
    arr = np.array(lines_list)

    counter = 0
    idx = []
    for x in arr:
        if x.startswith('#'):
            idx.append(counter)
        counter+=1 
    arr = np.delete(arr,idx,axis = 0)

    num_tp = int(arr[1])
    num_edges = int(arr[2])

    strings = arr[3]

    edges = arr[4:]

    return STN(num_tp, num_edges, strings, edges)



def to_string(input):
    string = ''
    succ = input.get_succs()
    edges = np.array([])
    names = input.get_names()

    for i in np.arange(input.get_num_tp()):
        for key,val in succ[i].items():
            new_edge = names[i]+' '+str(val)+' '+names[key]
            edges = np.append(edges, new_edge)

    string += "# KIND OF NETWORK\nSTN\n# Num Time-Points\n"+str(input.get_num_tp())
    string += "\n# Num Ordinary Edges\n"+str(input.get_num_edges())+"\n"
    string += "# Time-Point Names\n"+ " ".join(names) +"\n# Ordinary Edges\n"
    string += '\n'.join(edges)

    return string

