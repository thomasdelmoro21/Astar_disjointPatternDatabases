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
    for i in range(400):
    #for i in range(random.randint(10, 100)):
        neighbors = expand(node)
        node = random.choice(neighbors)
    return node


# N = 15 : 15puzzle
# N = 8 : 8puzzle
N = 15


def main():
    # start = [1,2,3,7, 8,4,5,6, 12,0,10,15, 9,11,13,14]
    start = [3,0,4, 6,8,5, 1,7,2]
    goal = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    manhattanValue = []
    conflictsValue = []
    disjointValue = []
    reflectedValue = []

    manhattanNodes = []
    conflictsNodes = []
    disjointNodes = []
    reflectedNodes = []

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


    pr = cProfile.Profile()
    pr.enable()

    db1, db2 = generateDatabases(N)
    rdb1, rdb2 = generateReflected(N)

    startStates = []

    for i in range(1):
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

        print(len(manhattanValue))

    pr.disable()
    pr.print_stats()

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

    plt.figure(1)
    plt.bar('Manhattan Distance', manhattanNodesAvg, width=0.50, color='r', label='Manhattan Distance')
    plt.bar('conflicts', conflictsNodesAvg, width=0.50, color='m', label='Linear Conflicts')
    plt.bar('disjoint', disjointNodesAvg, width=0.50, color='b', label='Disjoint Databases')
    plt.bar('reflected', reflectedNodesAvg, width=0.50, color='g', label='Disjoint + Reflected')
    plt.xlabel('Funzione euristica')
    plt.ylabel('Media dei nodi generati')
    plt.title('Grafico 1')
    plt.legend()

    plt.figure(2)
    plt.bar('Manhattan Distance', manhattanTimesAvg, width=0.50, color='r', label='Manhattan Distance')
    plt.bar('conflicts', conflictsTimesAvg, width=0.50, color='m', label='Linear Conflicts')
    plt.bar('disjoint', disjointTimesAvg, width=0.50, color='b', label='Disjoint Databases')
    plt.bar('reflected', reflectedTimesAvg, width=0.50, color='g', label='Disjoint + Reflected')
    plt.xlabel('Funzione euristica')
    plt.ylabel('Media dei tempi di risoluzione')
    plt.title('Grafico 2')
    plt.legend()

    plt.figure(3)
    plt.bar('Manhattan Distance', manhattanNodesPerSecond, width=0.50, color='r', label='Manhattan Distance')
    plt.bar('conflicts', conflictsNodesPerSecond, width=0.50, color='m', label='Linear Conflicts')
    plt.bar('disjoint', disjointNodesPerSecond, width=0.50, color='b', label='Disjoint Databases')
    plt.bar('reflected', reflectedNodesPerSecond, width=0.50, color='g', label='Disjoint + Reflected')
    plt.xlabel('Funzione euristica')
    plt.ylabel('Nodi generati al secondo')
    plt.title('Grafico 3')
    plt.legend()
    plt.show()

    manhattanResults = {"Funzione euristica": "Manhattan Distance", "Valore euristica": manhattanValueAvg,
                        "Nodi generati": manhattanNodesAvg, "Nodi al secondo": manhattanNodesPerSecond,
                        "Secondi": manhattanTimesAvg, "Tutte le soluzioni": manhattanAllNodesAvg}

    conflictsResults = {"Funzione euristica": "Manhattan Distance", "Valore euristica": conflictsValueAvg,
                        "Nodi generati": conflictsNodesAvg, "Nodi al secondo": conflictsNodesPerSecond,
                        "Secondi": conflictsTimesAvg, "Tutte le soluzioni": conflictsAllNodesAvg}

    disjointResults = {"Funzione euristica": "Manhattan Distance", "Valore euristica": disjointValueAvg,
                        "Nodi generati": disjointNodesAvg, "Nodi al secondo": disjointNodesPerSecond,
                        "Secondi": disjointTimesAvg, "Tutte le soluzioni": disjointAllNodesAvg}

    reflectedResults = {"Funzione euristica": "Manhattan Distance", "Valore euristica": reflectedValueAvg,
                        "Nodi generati": reflectedNodesAvg, "Nodi al secondo": reflectedNodesPerSecond,
                        "Secondi": reflectedTimesAvg, "Tutte le soluzioni": reflectedAllNodesAvg}

    print(manhattanResults)
    print(conflictsResults)
    print(disjointResults)
    print(reflectedResults)

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
