'''
@author Thomas Del Moro
'''

import math
import numpy as np
from queue import Queue
from LinearConflicts import linearConflicts
import Puzzle


def heuristic(node, h):
    if h == 1:
        result = manhattanDistance(node)

    elif h == 2:
        result = linearConflicts(node)

    return result


def manhattanDistance(node):
    d = 0
    for i in range(len(node)):
        value = node[i]
        if value != 0:
            dx = abs((value % 4) - (i % 4))
            dy = abs((value // 4) - (i // 4))
            d += dx + dy
    return d


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
