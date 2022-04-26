'''
#@author Thomas Del Moro
'''

from DisjointDatabases import BFS

def generateReflected():
    reflected1 = BFS([0, 1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
    print("Finito primo database")
    reflected2 = BFS([0, 0, 0, 0, 0, 0, 0, 0, 8, 9, 10, 11, 12, 13, 14, 15])
    print("Finito secondo database")
    return reflected1, reflected2

def reflectedCost(reflected1, reflected2, node):
    node1 = node[:]
    node2 = node[:]

    for i in range(len(node1)):
        value = node1[i]
        if value != 1 and value != 2 and value != 3 and value != 4 and value != 5 and value != 6 and value != 7:
            node1[i] = 0
    for i in range(len(node2)):
        value = node2[i]
        if value != 8 and value != 9 and value != 10 and value != 11 and value != 12 and value != 13 and value != 14 and value != 15:
            node2[i] = 0

    cost1 = 0
    node1 = tuple(node1)
    for s in reflected1.keys():
        if node1 == s:
            cost1 = reflected1[s]
        if cost1 != 0:
            break

    cost2 = 0
    node2 = tuple(node2)
    for s in reflected2.keys():
        if node2 == s:
            cost2 = reflected2[s]
        if cost2 != 0:
            break

    return cost1 + cost2
