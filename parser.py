import numpy as np

#will change this so user can choose
user_input = ("C:\\Users\gptacekLaptop\Downloads\Vassar\Sem5\cmpu382\code\sample_stn.txt")

def stringToArray(input):
    stn = open(input, "r")
    stn_string = stn.read()
    stn.close()
    
    lines_list = stn_string.splitlines()
    
    arr = np.array(lines_list)
    print(arr)

    counter = 0
    idx = []
    for x in arr:
        if x.startswith('#'):
            idx.append(counter)
        counter+=1 
    arr = np.delete(arr,idx,axis = 0)
    
    print(arr)

stringToArray(user_input)