'''
@author Thomas Del Moro
'''


def manhattanDistance(node):
    d = 0
    for i in range(len(node)):
        value = node[i]
        if value != 0:
            dx = abs((value % 4) - (i % 4))
            dy = abs((value // 4) - (i // 4))
            d += dx + dy
    return d
