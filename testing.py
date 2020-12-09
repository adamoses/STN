import numpy as np
import random
from STN import *
from algo import *
from stn_parser import *
import os

## May need to update the directory string for your computer!
## Note double slashes are needed
directory = 'C:\\Users\\Cameron\\Desktop\\STN\\STN\\sample_STNs'
user_input = ""



def floyd_warshall_test(file):
    stn = stringToSTN(file)
    print("\n", floyd_warshall(stn))
    

def naive_test(file):
    stn1 = stringToSTN(file)
    #rand_tp_1 = random.choice(stn1.get_names) 
    #rand_tp_2 = random.choice(stn1.get_names)
    edge = 'D 4 E'
    #edge = rand_tp_1 + random.randint(0,5) + rand_tp_2
    print("edge: ", edge)
    fw1 = floyd_warshall(stn1)
    stn1.update_distances(fw1)
    print("dist mat after naive: ", stn1.naive_update_distances(edge))

def dijkstra_test(file):
    stn = stringToSTN(file)
    print("\n", dijkstra(stn, 0, False, False))

def bellman_ford_test(file):
    stn = stringToSTN(file)
    print("\n", bellman_ford(stn, 0))

def dpc_test(file):
    stn = stringToSTN(file)
    node_ordering = stn.get_names()
    counter = 0
    for _ in node_ordering:
        node_ordering[counter] = counter
        counter = counter + 1
    random.shuffle(node_ordering)
    dpc(stn, node_ordering)

def prop_test(file):
    STN1 = stringToSTN(file)
    STN2 = STN1.copy()
    fw1 = floyd_warshall(STN1)
    STN1.update_distances(fw1)
    edge = ['D',4,'E']
    STN2.insert_edge(edge)
    fw2 = floyd_warshall(STN2)
    print("\n", np.all(prop_fwd_prop_bkwd(STN1, edge) == fw2))
    return np.all(prop_fwd_prop_bkwd(STN1, edge) == fw2)

def update_potential_test(file):
    stn = stringToSTN(file)
    dist = bellman_ford(stn, 0)
    a = stn.get_ordered_edges()
    print("\nupdated dist: ", stn.update_potential(dist, 'A'), "\n")
    b = stn.get_ordered_edges()
    print(a == b)

algo_strings = ["floyd_warshall", "naive_update_distances", " dijkstra", "bellman_ford", "dpc", "nprop", "update_potential"]
algo_funcs = [floyd_warshall_test, naive_test, dijkstra_test, bellman_ford_test, dpc_test, prop_test, update_potential_test]

def test_all_sample_stns():
    
    print("\nEnter algorithm (or number) to test (case sensitive): \n")
    for i, label in enumerate(algo_strings):
        print("\n",i, ") ", label)
    print("\n exit")
    user_input = input()

    if user_input == "exit":
        print("\nExiting...")
        exit(0)
    else:
        print("\nRunning", user_input, ":")

        label = user_input
        if user_input not in algo_strings:
            index = int(user_input)
            label = algo_strings[index]
        else:
            index = algo_strings.index(user_input)

        for file in os.listdir(directory):
            print("____________________________________________________________________________________________")
            print("\nFile", file, "run on", label, ":\n")
            algo_funcs[index](file)
            print("____________________________________________________________________________________________")
    

test_all_sample_stns()
        


