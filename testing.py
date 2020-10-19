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
    floyd_warshall(stn)

def dijkstra_test(file):
    stn = stringToSTN(file)
    dijkstra(stn, 0, False, False)

def bellman_ford_test(file):
    stn = stringToSTN(file)
    bellman_ford(stn, 0)

def dpc_test(file):
    stn = stringToSTN(file)
    node_ordering = stn.get_names()
    counter = 0
    for x in node_ordering:
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
    return np.all(prop_fwd_prop_bkwd(STN1, edge) == fw2)

def test_all_sample_stns():
    while(True):
        user_input = input("\nEnter algorithm to test (case sensitive):\n\nfloyd_warshall\nnaive_update_distances\ndijkstra\nbellman_ford\ndpc\nprop\nexit\n")
        if user_input == "exit":
            print("\nExiting...")
            break
        else:
            print("\nRunning " + user_input +":")
            for file in os.listdir(directory):
                if user_input == 'bellman_ford':
                    bellman_ford_test(file)
                elif user_input == 'dpc':
                    dpc_test(file)
                elif user_input == 'prop':
                    prop_test(file)
                else:
                    print("Error, try again!")

def test_sample_stns():
    while(True):
        user_input0 = input("\nEnter algorithm to test (case sensitive):\n\nfloyd_warshall\nnaive_update_distances\ndijkstra\nbellman_ford\ndpc\nprop\nexit\n")
        if user_input0 == "exit":
            print("\nExiting...")
            break
        else:
            print("\nRunning " + user_input0 +":\nPick an stn:\n")
            for file in os.listdir(directory):
                print(file)
            user_input1 = input("\n")

        if user_input0 == 'floyd_warshall':
            floyd_warshall_test(user_input1)
        elif user_input0 == 'dijkstra':
            dijkstra_test(user_input1)
        elif user_input0 == 'bellman_ford':
            bellman_ford_test(user_input1)
        elif user_input0 == 'dpc':
            dpc_test(user_input1)
        elif user_input0 == 'prop':
            prop_test(user_input1)
        else:
            print("Error, try again!")
        
user_input = input("\n\'one\' or \'all\' sample stns\n")
if user_input == 'one':
    test_sample_stns()
else:
    test_all_sample_stns()



