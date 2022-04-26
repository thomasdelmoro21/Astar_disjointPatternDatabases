'''
@author Thomas Del Moro
'''

import cProfile
from timeit import default_timer as timer
import numpy as np
from queue import PriorityQueue
import Puzzle
from DisjointDatabases import generateDatabases
from ReflectedDatabases import generateReflected


# N = 15 : 15puzzle
# N = 8 : 8puzzle
N = 8

# H = 1 : Manhattan Distance
# H = 2 : Linear Conflicts
# H = 3 : Disjoint Pattern Databases
# H = 4 : Disjoint Pattern Databases + Reflected
H = 4

def main():
    #start = [1,2,3,7, 8,4,5,6, 12,0,10,15, 9,11,13,14]
    start = [3,0,4, 6,8,5, 1,7,2]
    if N == 15:
        goal = [0,1,2,3, 4,5,6,7, 8,9,10,11, 12,13,14,15]
    elif N == 8:
        goal = [0,1,2, 3,4,5, 6,7,8]

    print(start)
    puzzle = Puzzle.Puzzle(start, goal, N)
    pr = cProfile.Profile()
    pr.enable()
    result = None

    if H == 1:
        result = puzzle.solve(H)
    elif H == 2:
        result = puzzle.solve(H)
    elif H == 3:
        db1, db2 = generateDatabases(N)
        puzzle.database1 = db1
        puzzle.database2 = db2
        result = puzzle.solve(H)
    elif H == 4:
        db1, db2 = generateDatabases(N)
        rdb1, rdb2 = generateReflected(N)
        puzzle.database1 = db1
        puzzle.database2 = db2
        puzzle.reflected1 = rdb1
        puzzle.reflected2 = rdb2
        result = puzzle.solve(H)

    pr.disable()
    print(result.state)
    pr.print_stats()

'''
    start2 = np.array([[1,3,0,7],[4,5,2,11],[13,9,6,15],[8,12,14,10]])
    startTime = timer()
    startRepr = str(start)
    start2Repr = str(start2)
    stringhe = startRepr == start2Repr
    endTime = timer()
    print(endTime - startTime)

    start2 = np.array([[1,3,0,7],[4,5,2,11],[13,9,6,15],[8,12,14,10]])
    startTime = timer()
    startTuple = tuple([tuple(e) for e in start])
    start2Tuple = tuple([tuple(e) for e in start2])
    tupless = startTuple == start2Tuple
    endTime = timer()
    print(endTime - startTime)
'''
    #reached = {}
    #reached[start] = 5
    #print(reached[start])



if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
