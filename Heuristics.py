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
        value = node[i]
        if value != 0:
            dx = abs((value % 4) - (i % 4))
            dy = abs((value // 4) - (i // 4))
            d += dx + dy
    return d


def linearConflicts(node): #FIX ME
    d = 0
    conflictRows = []
    for i in range(len(node)):
        value = node[i]
        if value != 0:
            dx = abs((value % 4) - (i % 4))
            if dx == 0:
                row = i // 4
                if row not in conflictRows:
                    conflictRows.append(row)
    row = []
    column = []
    conflicts = 0

    for i in range(0, 4):
        for j in range(0, 4):
            row.append(node[i*4+j])
        conflicts += searchConflicts(row)
        row.clear()

    for j in range(0, 4):
        for i in range(0, 4):
            column.append(node[i*4+j])
        conflicts += searchConflicts(column)
        column.clear()

    d -= conflicts * 2
    return d

def searchConflicts(list):
    conflicts = 0
    for i in range(len(list) - 1):
        value = list[i]
        if value != 0:
            for j in range(i + 1, len(list)):
                if list[i] > list[j]:
                    conflicts += 1
                    break
    return conflicts



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
