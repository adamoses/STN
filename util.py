from queue import *

class PriorityQueueSTN():

# Adding new methods to PriorityQueue
# 
# Operator Output/Side Effect
# Q.state(x) returns the state of x, one of notYetInQ, inQ or alreadyPopped
# Q.key(x) returns the key/priority of x (which must be in the queue)
# Q.empty() returns true if the queue is currently empty
# Q.extractMinNode() pop the datum with minimum priority off the queue
# Q.insert(x, p) insert datum x into the queue Q with priority/key p
# Q.decreaseKey(x, p) decrease the priority/key of x (which must be in the queue) to p
# Q.clear () clear the contents of the queue


    

    def __init__(self, p_queue): 
        self.p_queue = p_queue

        size = self.p_queue.qsize()
        counter = 0

        self.notYetinQ = 0
        self.inQ = 1
        self.alreadyPopped = 2

        self.queue = []
        self.popped = []
        
        while counter < size:
            #
            val = self.p_queue.get()
            self.queue.append(val)

            counter = counter + 1

    def state(self, x):
        # in popped
        for val, index in self.popped:
            if x == val:
                return self.alreadyPopped
        # Not yet in Q
        if x not in self.queue:
            return self.notYetinQ
        # in Q    
        elif x in self.queue:
                return self.inQ

    def key(self, x):
        if self.state(x) == self.alreadyPopped:
            for val, index in self.popped:            
                if x == val:
                    return index
        else:
            for i, val in enumerate(self.queue):            
                if x == val:
                    return i

    def empty(self):
        return len(self.queue) == 0

    def extractMinNode(self):
        index = len(self.queue) - 1
        val = self.queue.pop()
        self.popped.append((val, index))
        return val

    def insert(self, x, p):
        self.queue.insert(p,x)

    def decreaseKey(self, x, p):
        self.queue.remove(x)
        self.queue.insert(p,x)

    def clear(self):
        self.queue = []

    def insertOrDecreaseKeyIfSmaller(self, x, p):
        state = self.state(x)
        if state == self.notYetinQ:
            self.insert(x,p)
        elif state == self.inQ:
            if p < self.key(x):
                self.decreaseKey(x,p)
        elif state == self.alreadyPopped:
            if p < self.key(x):
                return False
        return True

    def setp_queue(self):
        p_queue = PriorityQueue()
        for i, val in enumerate(self.queue):
            p_queue.put((i, val))
        return p_queue


