'''
@author Thomas Del Moro
'''

import math
import numpy as np
from queue import Queue
from LinearConflicts import linearConflicts
from DisjointDatabases import disjointCost
import Puzzle



def nonAdditive(): #FIX ME
    start = [0,1,1,3, 1,1,1,7, 1,1,1,11, 12,13,14,15]
    node = Puzzle.Node(start, 0)
    frontier = Queue()  # FIFO queue
    frontier.put(node)
    reached = []
    reached.append(node)
    while frontier.qsize() > 0:
        node = frontier.get()
        neighbors = explore(node)
        for child in neighbors:
            s = child.state
            if s not in reached:
                reached.append(child)
                frontier.put(child)
    return False

def explore(node): #FIX ME
    neighbors = []
    return neighbors
