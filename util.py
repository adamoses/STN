import numpy as np

class PriorityQueue:

    def __init__(self):

        self.__p_queue = []

    # push() pushes a value onto the priority queue with 
    # some associated value
    def push(self, val, priority):
        self.__p_queue.append((val, priority))

    # pop() pops the lowest value of priority off the queue
    def pop(self):
        minimum = (None, np.inf)
        for val, priority in self.__p_queue:
            if priority < minimum[1]:
                minimum = (val, priority)
        self.__p_queue.remove(minimum)
        return minimum[0]

    def update(self, val, priority):
        last = None

        for val1, prior in self.__p_queue:
            if val1 == val:
                last = (val1, prior)

        if (not last is None) and priority < last[1]:
            self.__p_queue.remove(last)
            self.push(val, priority)
        elif last is None:
            self.push(val, priority)

    def isEmpty(self):
        return len(self.__p_queue) == 0
