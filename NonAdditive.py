'''
@author Thomas Del Moro
'''

from queue import Queue
import Puzzle


def generateNonAdditiveDatabase(n):
    if n == 15:
        length = 4
        database = BFS([0, -1, -1, 3, -1, -1, -1, 7, -1, -1, -1, 11, 12, 13, 14, 15], length)
        print("Finito non-additive database")

    elif n == 8:
        length = 3
        database = BFS([0, -1, 2, -1, -1, 5, 6, 7, 8], length)
        print("Finito non-additive database")

    return database


def BFS(start, length):
    node = Puzzle.Node(start, 0)
    frontier = Queue()
    frontier.put(node)
    reached = dict()
    reached[tuple(start)] = 0
    while frontier.qsize() > 0:
        node = frontier.get()
        neighbors = explore(node, length)
        for child in neighbors:
            s = tuple(child.state)
            if s not in reached.keys() or child.pathCost < reached[s]:
                reached[s] = child.pathCost
                frontier.put(child)
    return reached

def explore(node, length):
    neighbors = []
    index = node.state.index(0)
    i = index // length
    j = index % length

    if i != 0:
        newState = node.state[:]
        newState[index - length], newState[index] = newState[index], newState[index - length]
        neighbors.append(Puzzle.Node(newState, node.pathCost + 1))

    if i != length - 1:
        newState = node.state[:]
        newState[index], newState[index + length] = newState[index + length], newState[index]
        neighbors.append(Puzzle.Node(newState, node.pathCost + 1))

    if j != 0:
        newState = node.state[:]
        newState[index - 1], newState[index] = newState[index], newState[index - 1]
        neighbors.append(Puzzle.Node(newState, node.pathCost + 1))

    if j != length - 1:
        newState = node.state[:]
        newState[index], newState[index + 1] = newState[index + 1], newState[index]
        neighbors.append(Puzzle.Node(newState, node.pathCost + 1))

    return neighbors

def nonAdditiveCost(database, state, length):
    node = state[:]

    if length == 4:
        for i in range(len(node)):
            value = node[i]
            if value != 0 and value != 3 and value != 7 and value != 11 and value != 12 and value != 13 and value != 14 and value != 15:
                node[i] = -1

    elif length == 3:
        for i in range(len(node)):
            value = node[i]
            if value != 0 and value != 2 and value != 5 and value != 6 and value != 7 and value != 8:
                node[i] = -1

    cost = 0
    node = tuple(node)
    for s in database.keys():
        if node == s:
            cost = database[s]
            break

    return cost
