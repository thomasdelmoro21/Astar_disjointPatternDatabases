'''
@author Thomas Del Moro
'''

import cProfile
import numpy as np
import Puzzle
from queue import PriorityQueue

N = 1

def main():
    start = np.array([[1,3,0,7],[4,5,2,11],[13,9,6,15],[8,12,14,10]])
    goal = np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]])

    print(start)
    puzzle = Puzzle.Puzzle(start, goal)
    pr = cProfile.Profile()
    pr.enable()
    result = puzzle.solve(N)
    pr.disable()
    print(result.state)
    pr.print_stats()

    #reached = {}
    #reached[start] = 5
    #print(reached[start])



if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
