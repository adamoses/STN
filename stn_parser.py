import numpy as np
import sys
from STN import *


#will change this so user can choose
# if(len(sys.argv)!= 2):
#     print('\n\nUsage: python parser.py input_file.txt\n\n')
#     quit(0)
# else:
#     user_input = sys.argv[1]

def stringToSTN(input):
    path = "C:\\Users\\Cameron\\Desktop\\STN\\STN\\sample_STNs\\" + input

    with open(path, "r") as f:
        stn_string = f.read()
    
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