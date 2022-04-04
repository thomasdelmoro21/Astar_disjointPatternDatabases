'''
@author Thomas Del Moro
'''

import math
import numpy as np
from queue import Queue
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
        if node[i] != 0:
            dx = ((node[i] % 4) - (i % 4))
            dy = ((math.floor(node[i] / 4)) - (math.floor(i / 4)))
            d += dx + dy
    return d


def linearConflicts(node): #FIX ME
    d = 0
    for i in range(len(node)):
        if node[i] != 0:
            dx = ((node[i] % 4) - (i % 4))
            dy = ((math.floor(node[i] / 4)) - (math.floor(i / 4)))
            d += dx + dy
    return d


def nonAdditive():
    start = np.array([0, 1, 1, 3], [1, 1, 1, 7], [1, 1, 1, 11], [12, 13, 14, 15])
    node = Puzzle.Node(start, 0)
    frontier = Queue()  # FIFO queue
    frontier.put(node)
    reached = dict()
    reached[tuple([tuple(e) for e in node.state])] = node
    while frontier.qsize() > 0:
        node = frontier.get()
        neighbors = Puzzle.expand(node)
        for child in neighbors:
            s = tuple([tuple(e) for e in child.state])
            if s not in reached:
                reached[s] = child
                frontier.put(child)
