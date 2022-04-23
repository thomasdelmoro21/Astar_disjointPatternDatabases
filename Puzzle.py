'''
@author Thomas Del Moro
'''

from queue import PriorityQueue
import math
import numpy as np
from ManhattanDistance import manhattanDistance
from LinearConflicts import linearConflicts
from DisjointDatabases import disjointCost


class Node:
    def __init__(self, state, pathCost):
        self.state = state
        self.pathCost = pathCost

    def __lt__(self, other):
        return True


def expand(node):
    neighbors = []
    index = node.state.index(0)
    i = index // 4
    j = index % 4

    if i != 0:
        newState = node.state[:]
        newState[index - 4], newState[index] = newState[index], newState[index - 4]
        neighbors.append(Node(newState, node.pathCost + 1))

    if i != 3:
        newState = node.state[:]
        newState[index], newState[index + 4] = newState[index + 4], newState[index]
        neighbors.append(Node(newState, node.pathCost + 1))

    if j != 0:
        newState = node.state[:]
        newState[index - 1], newState[index] = newState[index], newState[index - 1]
        neighbors.append(Node(newState, node.pathCost + 1))

    if j != 3:
        newState = node.state[:]
        newState[index], newState[index + 1] = newState[index + 1], newState[index]
        neighbors.append(Node(newState, node.pathCost + 1))

    return neighbors


class Puzzle:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.currentNode = None
        self.database1 = None
        self.database2 = None

    def evaluationFunction(self, node, h):
        f = node.pathCost + self.heuristic(node.state, h)
        return f

    def heuristic(self, node, h):
        if h == 1:
            result = manhattanDistance(node)

        elif h == 2:
            result = linearConflicts(node)

        elif h == 3:
            result = disjointCost(self.database1, self.database2, node)

        return result

    def solve(self, h):
        node = Node(self.start, 0)
        frontier = PriorityQueue()
        frontier.put((self.evaluationFunction(node, h), node))
        reached = dict()
        reached[tuple(self.start)] = node

        while frontier.qsize() > 0:
            f, node = frontier.get()
            if node.state == self.goal:
                return node
            print(len(reached))
            neighbors = expand(node)
            for child in neighbors:
                s = tuple(child.state)
                if s not in reached.keys() or child.pathCost < reached[s].pathCost:
                    reached[s] = child
                    frontier.put((self.evaluationFunction(child, h), child))
        return False
