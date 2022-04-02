'''
@author Thomas Del Moro
'''

from queue import PriorityQueue
from copy import deepcopy
import math
import numpy as np
from Heuristics import heuristic


class Node:
    def __init__(self, state, pathCost):
        self.state = state
        self.pathCost = pathCost

    def __lt__(self, other):
        return True


def expand(node):
    neighbors = []
    arrayState = np.array(deepcopy(node.state))
    i = np.where(arrayState == 0)[0][0]
    j = np.where(arrayState == 0)[1][0]

    if i != 0:
        newState = deepcopy(node.state)
        newState[i - 1][j], newState[i][j] = newState[i][j], newState[i - 1][j]
        neighbors.append(Node(newState, node.pathCost + 1))

    if i != 3:
        newState = deepcopy(node.state)
        newState[i][j], newState[i + 1][j] = newState[i + 1][j], newState[i][j]
        neighbors.append(Node(newState, node.pathCost + 1))

    if j != 0:
        newState = deepcopy(node.state)
        newState[i][j - 1], newState[i][j] = newState[i][j], newState[i][j - 1]
        neighbors.append(Node(newState, node.pathCost + 1))

    if j != 3:
        newState = deepcopy(node.state)
        newState[i][j], newState[i][j + 1] = newState[i][j + 1], newState[i][j]
        neighbors.append(Node(newState, node.pathCost + 1))
    return neighbors


class Puzzle:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.currentNode = None

    def evaluationFunction(self, node, h):
        f = node.pathCost + heuristic(node.state, h)
        return f

    def solve(self, h):
        node = Node(self.start, 0)
        frontier = PriorityQueue()
        frontier.put((self.evaluationFunction(node, h), node))
        reached = dict()
        reached[tuple([tuple(e) for e in self.start])] = node

        while frontier.qsize() > 0:
            f, node = frontier.get()
            if node.state == self.goal:
                return node
            print(len(reached))
            neighbors = expand(node)
            for child in neighbors:
                s = tuple([tuple(e) for e in child.state])
                if s not in reached.keys() or child.pathCost < reached[s].pathCost:
                    reached[s] = child
                    frontier.put((self.evaluationFunction(child, h), child))
        print(node.state)
        return False
