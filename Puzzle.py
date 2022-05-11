'''
@author Thomas Del Moro
'''

from queue import PriorityQueue
import math
import numpy as np
from timeit import default_timer as timer
from ManhattanDistance import manhattanDistance
from LinearConflicts import linearConflicts
from DisjointDatabases import disjointCost
from ReflectedDatabases import reflectedCost


class Node:
    def __init__(self, state, pathCost):
        self.state = state
        self.pathCost = pathCost

    def __lt__(self, other):
        return True


class Puzzle:
    def __init__(self, start, goal, n):
        self.start = start
        self.goal = goal
        if n == 15:
            self.length = 4
        elif n == 8:
            self.length = 3
        self.currentNode = None
        self.database1 = None
        self.database2 = None
        self.reflected1 = None
        self.reflected2 = None

    def evaluationFunction(self, node, h):
        f = node.pathCost + self.heuristic(node.state, h)
        return f

    def heuristic(self, node, h):
        if h == 1:
            result = manhattanDistance(node, self.length)

        elif h == 2:
            result = linearConflicts(node, self.length)

        elif h == 3:
            result = disjointCost(self.database1, self.database2, node, self.length)

        elif h == 4:
            disjoint = disjointCost(self.database1, self.database2, node, self.length)
            reflected = reflectedCost(self.reflected1, self.reflected2, node, self.length)
            result = max(disjoint, reflected)
        return result

    def expand(self, node):
        neighbors = []
        index = node.state.index(0)
        i = index // self.length
        j = index % self.length

        if i != 0:
            newState = node.state[:]
            newState[index - self.length], newState[index] = newState[index], newState[index - self.length]
            neighbors.append(Node(newState, node.pathCost + 1))

        if i != self.length - 1:
            newState = node.state[:]
            newState[index], newState[index + self.length] = newState[index + self.length], newState[index]
            neighbors.append(Node(newState, node.pathCost + 1))

        if j != 0:
            newState = node.state[:]
            newState[index - 1], newState[index] = newState[index], newState[index - 1]
            neighbors.append(Node(newState, node.pathCost + 1))

        if j != self.length - 1:
            newState = node.state[:]
            newState[index], newState[index + 1] = newState[index + 1], newState[index]
            neighbors.append(Node(newState, node.pathCost + 1))

        return neighbors

    def solve(self, h):
        start = timer()
        optimalCost = math.inf
        numReached = 0
        node = Node(self.start, 0)
        frontier = PriorityQueue()
        value = self.evaluationFunction(node, h)
        frontier.put((value, node))
        reached = dict()
        reached[tuple(self.start)] = node

        while frontier.qsize() > 0:
            f, node = frontier.get()
            if node.pathCost < optimalCost:
                if node.state == self.goal:
                    end = timer()
                    time = end - start
                    optimalCost = node.pathCost
                    numReached = len(reached)
                    print(node.state)
                print(len(reached))
                neighbors = self.expand(node)
                for child in neighbors:
                    s = tuple(child.state)
                    if s not in reached.keys() or child.pathCost < reached[s].pathCost:
                        reached[s] = child
                        frontier.put((self.evaluationFunction(child, h), child))

        return value, time, numReached, len(reached)
