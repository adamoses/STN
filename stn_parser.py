import numpy as np
import sys
from STN import *
from algo import *
from STNU import *
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

def string_to_stnu(input):
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
    num_cont_edges = int(arr[3])

    strings = arr[4]

    edges = []
    contingent_links = []

    for line in arr[5:]:
        if len(line.split()) == 4:
            contingent_links.append(line)
        else:
            edges.append(line)
        

    return STNU(num_tp, num_edges, num_cont_edges, strings, edges, contingent_links)

def stnu_to_string(input):
    string = ''
    edges = input.get_ordered_edges() 
    edges = [' '.join(edge) for edge in edges]
    cont_edges = input.get_cont_links()
    cont_edges = [' '.join(edge) for edge in cont_edges]
    names = ' ' 
    names = names.join(input.get_names())

    string += "# KIND OF NETWORK\nSTN\n# Num Time-Points\n"+str(input.get_num_tp())
    string += "\n# Num Ordinary Edges\n"+str(input.get_num_edges())+"\n"
    string += "# Num Contingent Links\n"+str(input.get_num_cont_links())+'\n'
    string += "# Time-Point Names\n"+ names +"\n# Ordinary Edges\n"
    string += '\n'.join(edges)+'\n'+'# Contingent Links\n'+"\n".join(cont_edges)

    return string

def stn_to_string(input):
    string = ''
    edges = input.get_ordered_edges() 
    edges = [' '.join(edge) for edge in edges]
    names = ' ' 
    names = names.join(input.get_names())

    string += "# KIND OF NETWORK\nSTNU\n# Num Time-Points\n"+str(input.get_num_tp())
    string += "\n# Num Ordinary Edges\n"+str(input.get_num_edges())+"\n"
    string += "# Time-Point Names\n"+ names +"\n# Ordinary Edges\n"
    string += '\n'.join(edges)

    return string

test = string_to_stnu('sample_STNs/dc-1.stnu')

print(stnu_to_string(test), '\n\n\n')

test.to_normal()

print(stnu_to_string(test))

print(Morris_2014(test))


# print(stnu_to_string(test), '\n\n')

# print(test.get_cont_preds())
