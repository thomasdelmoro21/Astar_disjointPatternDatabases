'''
@author Thomas Del Moro
'''

from queue import Queue
import Puzzle


def generateDatabases(n):
    if n == 15:
        length = 4
        database1 = BFS([0, 1, 0, 0, 4, 5, 0, 0, 8, 9, 0, 0, 12, 13, 0, 0], length)
        print("Finito primo database")
        database2 = BFS([0, 0, 2, 3, 0, 0, 6, 7, 0, 0, 10, 11, 0, 0, 14, 15], length)
        print("Finito secondo database")

    elif n == 8:
        length = 3
        database1 = BFS([0, 1, 2, 3, 4, 0, 0, 0, 0], length)
        print("Finito primo database")
        database2 = BFS([0, 0, 0, 0, 0, 5, 6, 7, 8], length)
        print("Finito secondo database")

    return database1, database2


def BFS(start, length):
    node = Puzzle.Node(start, 0)
    frontier = Queue()
    frontier.put(node)
    reached = dict()
    reached[tuple(start)] = 0
    while frontier.qsize() > 0:
        node = frontier.get()
        neighbors = explore(node, length)
        print(len(reached))
        for child in neighbors:
            s = tuple(child.state)
            if s not in reached.keys() or child.pathCost < reached[s]:
                reached[s] = child.pathCost
                frontier.put(child)
    return reached


def explore(node, length):
    neighbors = []
    for index in range(len(node.state)):
        i = index // length
        j = index % length
        if node.state[index] != 0:

            if i != 0 and node.state[index - length] == 0:
                newState = node.state[:]
                newState[index - length], newState[index] = newState[index], newState[index - length]
                neighbors.append(Puzzle.Node(newState, node.pathCost + 1))

            if i != length - 1 and node.state[index + length] == 0:
                newState = node.state[:]
                newState[index + length], newState[index] = newState[index], newState[index + length]
                neighbors.append(Puzzle.Node(newState, node.pathCost + 1))

            if j != 0 and node.state[index - 1] == 0:
                newState = node.state[:]
                newState[index - 1], newState[index] = newState[index], newState[index - 1]
                neighbors.append(Puzzle.Node(newState, node.pathCost + 1))

            if j != length - 1 and node.state[index + 1] == 0:
                newState = node.state[:]
                newState[index + 1], newState[index] = newState[index], newState[index + 1]
                neighbors.append(Puzzle.Node(newState, node.pathCost + 1))

    return neighbors


def disjointCost(database1, database2, node, length):
    node1 = node[:]
    node2 = node[:]

    if length == 4:
        for i in range(len(node1)):
            value = node1[i]
            if value != 1 and value != 4 and value != 5 and value != 8 and value != 9 and value != 12 and value != 13:
                node1[i] = 0
        for i in range(len(node2)):
            value = node2[i]
            if value != 2 and value != 3 and value != 6 and value != 7 and value != 10 and value != 11 and value != 14 and value != 15:
                node2[i] = 0

    elif length == 3:
        for i in range(len(node1)):
            value = node1[i]
            if value != 1 and value != 2 and value != 3 and value != 4:
                node1[i] = 0
        for i in range(len(node2)):
            value = node2[i]
            if value != 5 and value != 6 and value != 7 and value != 8:
                node2[i] = 0

    cost1 = 0
    node1 = tuple(node1)
    for s in database1.keys():
        if node1 == s:
            cost1 = database1[s]
        if cost1 != 0:
            break

    cost2 = 0
    node2 = tuple(node2)
    for s in database2.keys():
        if node2 == s:
            cost2 = database2[s]
        if cost2 != 0:
            break

    return cost1 + cost2
