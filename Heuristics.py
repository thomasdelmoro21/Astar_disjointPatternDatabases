'''
@author Thomas Del Moro
'''

import math
import numpy as np
from queue import Queue
import Puzzle

def heuristic(node, h):
    #Manhattan distance
    if h == 1:
        d = 0
        for i in range(4):
            for j in range(4):
                if node[i, j] != 0:
                    x = node[i, j] % 4
                    y = math.floor(node[i, j] / 4)
                    d = d + abs(i-y) + abs(j-x)
        return d

    #Non-additive pattern databases
    #if h == 2:
        

def nonAdditive():
    start = np.array([0,1,1,3],[1,1,1,7],[1,1,1,11],[12,13,14,15])
    node = Puzzle.Node(start, 0)
    frontier = Queue()  #FIFO queue
    frontier.put(node)
    reached = []
    reached.append(tuple([tuple(e) for e in node.state]))
    while frontier.qsize() > 0:
        node = frontier.get()
        neighbors = Puzzle.expand(node)
        for child in neighbors:
            s = tuple([tuple(e) for e in child.state])
            if s not in reached:
                reached.append(s)
                frontier.put(child)
