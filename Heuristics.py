'''
@author Thomas Del Moro
'''

import math


def heuristic(node, h):
    #Manhattan distance
    if h == 1:
        d = 0
        for i in range(4):
            for j in range(4):
                if node[i, j] != 0:
                    x = node[i, j] % 4
                    y = math.floor(node[i, j] / 4)
                    d = d + abs(i-y) + abs(j-x)
        return d

    #Non-additive pattern databases
    #if h == 2:
        
