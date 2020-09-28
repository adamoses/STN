import numpy as np
from STN import *

#will change this so user can choose
user_input = ("sample.txt")

def stringToSTN(input):
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



def arrayToString(input):
    s = ""
    counter = 0
    for x in input:
        if counter == 0:
            s += "# KIND OF NETWORK\n"
        elif counter == 1:
            s += "# Num Time-Points\n"
        elif counter == 2:
            s += "# Num Ordinary Edges\n"
        elif counter == 3:
            s += "# Time-Point Names\n"
        elif counter == 4:
            s += "# Ordinary Edges\n"
        s += x + "\n"
        counter += 1
    return s

our_STN = stringToSTN(user_input)
#our_string = arrayToString(our_array)
print(our_STN.get_preds())