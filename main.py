'''
@author Thomas Del Moro
'''

import cProfile
import numpy as np
import random
import statistics
import matplotlib.pyplot as plt
from tabulate import tabulate
from queue import PriorityQueue
from Puzzle import Puzzle
from NonAdditive import generateNonAdditiveDatabase
from DisjointDatabases import generateDisjointDatabases
from ReflectedDatabases import generateReflectedDatabases


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
    for i in range(random.randint(100, 10000)):
        neighbors = expand(node)
        node = random.choice(neighbors)
    return node


# N = 15 : 15puzzle
# N = 8 : 8puzzle
N = 8
numOfTests = 5


def main():
    # start = [1,2,3,7, 8,4,5,6, 12,0,10,15, 9,11,13,14]
    # start = [3,0,4, 6,8,5, 1,7,2]
    # start = shuffle(start)
    # goal = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    manhattanValue = []
    conflictsValue = []
    disjointValue = []
    reflectedValue = []
    nonAdditiveValue = []

    manhattanNodes = []
    conflictsNodes = []
    disjointNodes = []
    reflectedNodes = []
    nonAdditiveNodes = []

    manhattanTimes = []
    conflictsTimes = []
    disjointTimes = []
    reflectedTimes = []
    nonAdditiveTimes = []

    manhattanAllNodes = []
    conflictsAllNodes = []
    disjointAllNodes = []
    reflectedAllNodes = []
    nonAdditiveAllNodes = []

    if N == 15:
        goal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    elif N == 8:
        goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    #pr = cProfile.Profile()
    #pr.enable()

    ndb = generateNonAdditiveDatabase(N)
    db1, db2 = generateDisjointDatabases(N)
    rdb1, rdb2 = generateReflectedDatabases(N)

    startStates = []

    for i in range(numOfTests):
        node = shuffle(goal)
        startStates.append(node)

    for start in startStates:
        puzzle = Puzzle(start, goal, N)


        H = 1 #ManhattanDistance
        value, time, reached, allReached = puzzle.solve(H)
        manhattanValue.append(value)
        manhattanTimes.append(time)
        manhattanNodes.append(reached)
        manhattanAllNodes.append(allReached)

        H = 2 #LinearConflicts
        value, time, reached, allReached = puzzle.solve(H)
        conflictsValue.append(value)
        conflictsTimes.append(time)
        conflictsNodes.append(reached)
        conflictsAllNodes.append(allReached)

        H = 3 #DisjointDatabases
        puzzle.database1 = db1
        puzzle.database2 = db2
        value, time, reached, allReached = puzzle.solve(H)
        disjointValue.append(value)
        disjointTimes.append(time)
        disjointNodes.append(reached)
        disjointAllNodes.append(allReached)

        H = 4 #ReflectedDatabases
        puzzle.reflected1 = rdb1
        puzzle.reflected2 = rdb2
        value, time, reached, allReached = puzzle.solve(H)
        reflectedValue.append(value)
        reflectedTimes.append(time)
        reflectedNodes.append(reached)
        reflectedAllNodes.append(allReached)

        H = 5 #NonAdditiveDatabases
        puzzle.nonAdditiveDatabase = ndb
        value, time, reached, allReached = puzzle.solve(H)
        nonAdditiveValue.append(value)
        nonAdditiveTimes.append(time)
        nonAdditiveNodes.append(reached)
        nonAdditiveAllNodes.append(allReached)
        

        print(len(manhattanValue))

    #pr.disable()
    #pr.print_stats()

    manhattanValueAvg = statistics.mean(manhattanValue)
    manhattanTimesAvg = statistics.mean(manhattanTimes)
    manhattanNodesAvg = statistics.mean(manhattanNodes)
    manhattanAllNodesAvg = statistics.mean(manhattanAllNodes)
    manhattanNodesPerSecond = manhattanNodesAvg / manhattanTimesAvg

    conflictsValueAvg = statistics.mean(conflictsValue)
    conflictsTimesAvg = statistics.mean(conflictsTimes)
    conflictsNodesAvg = statistics.mean(conflictsNodes)
    conflictsAllNodesAvg = statistics.mean(conflictsAllNodes)
    conflictsNodesPerSecond = conflictsNodesAvg / conflictsTimesAvg

    disjointValueAvg = statistics.mean(disjointValue)
    disjointTimesAvg = statistics.mean(disjointTimes)
    disjointNodesAvg = statistics.mean(disjointNodes)
    disjointAllNodesAvg = statistics.mean(disjointAllNodes)
    disjointNodesPerSecond = disjointNodesAvg / disjointTimesAvg

    reflectedValueAvg = statistics.mean(reflectedValue)
    reflectedTimesAvg = statistics.mean(reflectedTimes)
    reflectedNodesAvg = statistics.mean(reflectedNodes)
    reflectedAllNodesAvg = statistics.mean(reflectedAllNodes)
    reflectedNodesPerSecond = reflectedNodesAvg / reflectedTimesAvg

    nonAdditiveValueAvg = statistics.mean(nonAdditiveValue)
    nonAdditiveTimesAvg = statistics.mean(nonAdditiveTimes)
    nonAdditiveNodesAvg = statistics.mean(nonAdditiveNodes)
    nonAdditiveAllNodesAvg = statistics.mean(nonAdditiveAllNodes)
    nonAdditiveNodesPerSecond = nonAdditiveNodesAvg / nonAdditiveTimesAvg

    plt.figure(1)
    plt.bar('Manhattan', manhattanNodesAvg, width=0.50, color='c', label='Manhattan Distance')
    plt.bar('Conflicts', conflictsNodesAvg, width=0.50, color='m', label='Linear Conflicts')
    plt.bar('Disjoint', disjointNodesAvg, width=0.50, color='r', label='Disjoint Databases')
    plt.bar('Reflected', reflectedNodesAvg, width=0.50, color='b', label='Disjoint + Reflected')
    plt.bar('Non Additive', nonAdditiveNodesAvg, width=0.50, color='g', label='Non Additive')
    plt.xlabel('Funzione euristica')
    plt.ylabel('Media dei nodi generati')
    plt.title('Grafico 1')
    plt.legend()

    plt.figure(2)
    plt.bar('Manhattan', manhattanTimesAvg, width=0.50, color='c', label='Manhattan Distance')
    plt.bar('Conflicts', conflictsTimesAvg, width=0.50, color='m', label='Linear Conflicts')
    plt.bar('Disjoint', disjointTimesAvg, width=0.50, color='r', label='Disjoint Databases')
    plt.bar('Reflected', reflectedTimesAvg, width=0.50, color='b', label='Disjoint + Reflected')
    plt.bar('Non Additive', nonAdditiveTimesAvg, width=0.50, color='g', label='Non Additive')
    plt.xlabel('Funzione euristica')
    plt.ylabel('Media dei tempi di risoluzione')
    plt.title('Grafico 2')
    plt.legend()

    plt.figure(3)
    plt.bar('Manhattan', manhattanNodesPerSecond, width=0.50, color='c', label='Manhattan Distance')
    plt.bar('Conflicts', conflictsNodesPerSecond, width=0.50, color='m', label='Linear Conflicts')
    plt.bar('Disjoint', disjointNodesPerSecond, width=0.50, color='r', label='Disjoint Databases')
    plt.bar('Reflected', reflectedNodesPerSecond, width=0.50, color='b', label='Disjoint + Reflected')
    plt.bar('Non Additive', reflectedNodesPerSecond, width=0.50, color='g', label='Non Additive')
    plt.xlabel('Funzione euristica')
    plt.ylabel('Nodi generati al secondo')
    plt.title('Grafico 3')
    plt.legend()
    plt.show()

    manhattanResults = {"Funzione euristica": "Manhattan Distance", "Valore euristica": manhattanValueAvg,
                        "Nodi generati": manhattanNodesAvg, "Nodi al secondo": manhattanNodesPerSecond,
                        "Secondi": manhattanTimesAvg, "Tutte le soluzioni": manhattanAllNodesAvg}

    conflictsResults = {"Funzione euristica": "Linear Conflicts", "Valore euristica": conflictsValueAvg,
                        "Nodi generati": conflictsNodesAvg, "Nodi al secondo": conflictsNodesPerSecond,
                        "Secondi": conflictsTimesAvg, "Tutte le soluzioni": conflictsAllNodesAvg}

    disjointResults = {"Funzione euristica": "Disjoint Databases", "Valore euristica": disjointValueAvg,
                        "Nodi generati": disjointNodesAvg, "Nodi al secondo": disjointNodesPerSecond,
                        "Secondi": disjointTimesAvg, "Tutte le soluzioni": disjointAllNodesAvg}

    reflectedResults = {"Funzione euristica": "Reflected Databases", "Valore euristica": reflectedValueAvg,
                        "Nodi generati": reflectedNodesAvg, "Nodi al secondo": reflectedNodesPerSecond,
                        "Secondi": reflectedTimesAvg, "Tutte le soluzioni": reflectedAllNodesAvg}

    nonAdditiveResults = {"Funzione euristica": "Non Additive", "Valore euristica": nonAdditiveValueAvg,
                        "Nodi generati": nonAdditiveNodesAvg, "Nodi al secondo": nonAdditiveNodesPerSecond,
                        "Secondi": nonAdditiveTimesAvg, "Tutte le soluzioni": nonAdditiveAllNodesAvg}

    print(manhattanResults)
    print(conflictsResults)
    print(disjointResults)
    print(reflectedResults)
    print(nonAdditiveResults)

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
