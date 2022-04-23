'''
@author Thomas Del Moro
'''

from queue import Queue
import Puzzle


class Database:
    def __init__(self, db1, db2):
        self.database1 = db1
        self.database2 = db2


def generateDatabases():
    database1 = BFS([0, 1, 0, 0, 4, 5, 0, 0, 8, 9, 0, 0, 12, 13, 0, 0])
    print("Finito primo database")
    database2 = BFS([0, 0, 2, 3, 0, 0, 6, 7, 0, 0, 10, 11, 0, 0, 14, 15])
    print("Finito secondo database")
    return Database(database1, database2)


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
        if value != 1 or value != 4 or value != 5 or value != 8 or value != 9 or value != 12 or value != 13:
            value = 0
    for i in range(len(node2)):
        value = node2[i]
        if value != 2 or value != 3 or value != 6 or value != 7 or value != 10 or value != 11 or value != 14 or value != 15:
            value = 0

    cost1 = 0
    node1 = tuple(node1)
    s = 0
    while cost1 == 0:
        if node1 == s:
            cost1 = database1[s]
        s += 1

    cost2 = 0
    node2 = tuple(node2)
    s = 0
    while cost2 == 0:
        if node2 == s:
            cost2 = database2[s]
        s += 1

    return cost1 + cost2
