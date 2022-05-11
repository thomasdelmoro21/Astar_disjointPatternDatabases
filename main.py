'''
@author Thomas Del Moro
'''

import cProfile
from timeit import default_timer as timer
import numpy as np
import random
from queue import PriorityQueue
from Puzzle import Puzzle
from DisjointDatabases import generateDatabases
from ReflectedDatabases import generateReflected


def expand(node):
    neighbors = []
    index = node.index(0)
    length = 0
    if len(node) == 16:
        length = 4
    elif len(node) == 9:
        length = 3
    i = index // length
    j = index % length

    if i != 0:
        newState = node[:]
        newState[index - length], newState[index] = newState[index], newState[index - length]
        neighbors.append(newState)

    if i != length - 1:
        newState = node[:]
        newState[index], newState[index + length] = newState[index + length], newState[index]
        neighbors.append(newState)

    if j != 0:
        newState = node[:]
        newState[index - 1], newState[index] = newState[index], newState[index - 1]
        neighbors.append(newState)

    if j != length - 1:
        newState = node[:]
        newState[index], newState[index + 1] = newState[index + 1], newState[index]
        neighbors.append(newState)

    return neighbors


def shuffle(node):
    for i in range(random.randint(1, 100)):
        neighbors = expand(node)
        node = random.choice(neighbors)
    return node


# N = 15 : 15puzzle
# N = 8 : 8puzzle
N = 8

# H = 1 : Manhattan Distance
# H = 2 : Linear Conflicts
# H = 3 : Disjoint Pattern Databases
# H = 4 : Disjoint Pattern Databases + Reflected
H = 1


def main():
    # start = [1,2,3,7, 8,4,5,6, 12,0,10,15, 9,11,13,14]
    # start = [3,0,4, 6,8,5, 1,7,2]
    goal = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    manhattanValue = []
    conflictsValue = []
    disjointValue = []
    reflectedValue = []

    manhattanNodes = []
    conflictsNodes = []
    disjointNodes = []
    reflectedNode = []

    manhattanTimes = []
    conflictsTimes = []
    disjointTimes = []
    reflectedTimes = []

    manhattanAllNodes = []
    conflictsAllNodes = []
    disjointAllNodes = []
    reflectedAllNodes = []

    if N == 15:
        goal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    elif N == 8:
        goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    start = shuffle(goal)

    print(start)
    puzzle = Puzzle(start, goal, N)
    pr = cProfile.Profile()
    pr.enable()
    reached = 0
    allReached = 0

    if H == 1:
        reached, allReached = puzzle.solve(H)
    elif H == 2:
        reached, allReached = puzzle.solve(H)
    elif H == 3:
        db1, db2 = generateDatabases(N)
        puzzle.database1 = db1
        puzzle.database2 = db2
        reached, allReached = puzzle.solve(H)
    elif H == 4:
        db1, db2 = generateDatabases(N)
        rdb1, rdb2 = generateReflected(N)
        puzzle.database1 = db1
        puzzle.database2 = db2
        puzzle.reflected1 = rdb1
        puzzle.reflected2 = rdb2
        reached, allReached = puzzle.solve(H)

    pr.disable()
    print(reached)
    print(allReached)
    pr.print_stats()


'''
    start2 = np.array([[1,3,0,7],[4,5,2,11],[13,9,6,15],[8,12,14,10]])
    startTime = timer()
    startRepr = str(start)
    start2Repr = str(start2)
    stringhe = startRepr == start2Repr
    endTime = timer()
    print(endTime - startTime)

    start2 = np.array([[1,3,0,7],[4,5,2,11],[13,9,6,15],[8,12,14,10]])
    startTime = timer()
    startTuple = tuple([tuple(e) for e in start])
    start2Tuple = tuple([tuple(e) for e in start2])
    tupless = startTuple == start2Tuple
    endTime = timer()
    print(endTime - startTime)
'''
# reached = {}
# reached[start] = 5
# print(reached[start])


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
