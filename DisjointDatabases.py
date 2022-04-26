'''
@author Thomas Del Moro
'''

from queue import Queue
import Puzzle


def generateDatabases():
    database1 = BFS([0, 1, 0, 0, 4, 5, 0, 0, 8, 9, 0, 0, 12, 13, 0, 0])
    print("Finito primo database")
    database2 = BFS([0, 0, 2, 3, 0, 0, 6, 7, 0, 0, 10, 11, 0, 0, 14, 15])
    print("Finito secondo database")
    return database1, database2


def BFS(start):
    node = Puzzle.Node(start, 0)
    frontier = Queue()
    frontier.put(node)
    reached = dict()
    reached[tuple(start)] = 0
    while frontier.qsize() > 0:
        node = frontier.get()
        neighbors = explore(node)
        print(len(reached))
        for child in neighbors:
            s = tuple(child.state)
            if s not in reached.keys() or child.pathCost < reached[s]:
                reached[s] = child.pathCost
                frontier.put(child)
    return reached


def explore(node):
    neighbors = []
    for index in range(len(node.state)):
        i = index // 4
        j = index % 4
        if node.state[index] != 0:

            if i != 0 and node.state[index - 4] == 0:
                newState = node.state[:]
                newState[index - 4], newState[index] = newState[index], newState[index - 4]
                neighbors.append(Puzzle.Node(newState, node.pathCost + 1))

            if i != 3 and node.state[index + 4] == 0:
                newState = node.state[:]
                newState[index + 4], newState[index] = newState[index], newState[index + 4]
                neighbors.append(Puzzle.Node(newState, node.pathCost + 1))

            if j != 0 and node.state[index - 1] == 0:
                newState = node.state[:]
                newState[index - 1], newState[index] = newState[index], newState[index - 1]
                neighbors.append(Puzzle.Node(newState, node.pathCost + 1))

            if j != 3 and node.state[index + 1] == 0:
                newState = node.state[:]
                newState[index + 1], newState[index] = newState[index], newState[index + 1]
                neighbors.append(Puzzle.Node(newState, node.pathCost + 1))

    return neighbors


def disjointCost(database1, database2, node):
    node1 = node[:]
    node2 = node[:]

    for i in range(len(node1)):
        value = node1[i]
        if value != 1 and value != 4 and value != 5 and value != 8 and value != 9 and value != 12 and value != 13:
            node1[i] = 0
    for i in range(len(node2)):
        value = node2[i]
        if value != 2 and value != 3 and value != 6 and value != 7 and value != 10 and value != 11 and value != 14 and value != 15:
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
