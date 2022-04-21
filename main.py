'''
@author Thomas Del Moro
'''

import cProfile
from timeit import default_timer as timer
import numpy as np
import Puzzle
from queue import PriorityQueue

N = 1

def main():
    start = [1,2,3,7, 0,5,10,6, 4,8,11,15, 12,9,13,14]
    goal = [0,1,2,3, 4,5,6,7, 8,9,10,11, 12,13,14,15]

    print(start)
    puzzle = Puzzle.Puzzle(start, goal)
    pr = cProfile.Profile()
    pr.enable()
    result = puzzle.solve(N)
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
