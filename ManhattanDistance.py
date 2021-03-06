'''
@author Thomas Del Moro
'''


def manhattanDistance(node, length):
    d = 0
    for i in range(len(node)):
        value = node[i]
        if value != 0:
            dx = abs((value % length) - (i % length))
            dy = abs((value // length) - (i // length))
            d += dx + dy
    return d
