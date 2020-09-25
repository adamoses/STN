import numpy as np

#will change this so user can choose
user_input = ("C:\\Users\gptacekLaptop\Downloads\Vassar\Sem5\cmpu382\code\sample_stn.txt")

def stringToArray(input):
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
    
    return arr


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

our_array = stringToArray(user_input)
our_string = arrayToString(our_array)
print(our_string)