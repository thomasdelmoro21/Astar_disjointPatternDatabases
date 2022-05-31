'''
#@author Thomas Del Moro
'''

from DisjointDatabases import BFS

def generateReflectedDatabases(n):
    if n == 15:
        length = 4
        reflected1 = BFS([0, 1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0], length)
        print("Finito primo database")
        reflected2 = BFS([0, 0, 0, 0, 0, 0, 0, 0, 8, 9, 10, 11, 12, 13, 14, 15], length)
        print("Finito secondo database")

    elif n == 8:
        length = 3
        reflected1 = BFS([0, 1, 2, 0, 0, 5, 0, 0, 8], length)
        print("Finito primo database")
        reflected2 = BFS([0, 0, 0, 3, 4, 0, 6, 7, 0], length)
        print("Finito secondo database")

    return reflected1, reflected2

def reflectedCost(reflected1, reflected2, node, length):
    node1 = node[:]
    node2 = node[:]

    if length == 4:
        for i in range(len(node1)):
            value = node1[i]
            if value != 1 and value != 2 and value != 3 and value != 4 and value != 5 and value != 6 and value != 7:
                node1[i] = 0
        for i in range(len(node2)):
            value = node2[i]
            if value != 8 and value != 9 and value != 10 and value != 11 and value != 12 and value != 13 and value != 14 and value != 15:
                node2[i] = 0

    elif length == 3:
        for i in range(len(node1)):
            value = node1[i]
            if value != 1 and value != 2 and value != 5 and value != 8:
                node1[i] = 0
        for i in range(len(node2)):
            value = node2[i]
            if value != 3 and value != 4 and value != 6 and value != 7:
                node2[i] = 0

    cost1 = 0
    node1 = tuple(node1)
    for s in reflected1.keys():
        if node1 == s:
            cost1 = reflected1[s]
            break

    cost2 = 0
    node2 = tuple(node2)
    for s in reflected2.keys():
        if node2 == s:
            cost2 = reflected2[s]
            break

    return cost1 + cost2
