import sys
sys.path.append('aima-python')
from search import *
import math
import time

def mhd(node):
    '''
    Define your manhattan-distance heuristic for the 8-puzzle here
    It should take in the current node, and return a numerical value.
    '''
    # Default goal is (1, 2, 3, 4, 5, 6, 7, 8, 0)
    #   which represents:   1 2 3
    #                       4 5 6
    #                       7 8 _
    sum = 0
    for i in range(9):
        if node.state[i] != 0:
            (x1, y1) = divmod(i, 3)
            (x2, y2) = divmod(node.state[i] - 1, 3)
            sum += abs(x1 - x2) + abs(y1 - y2)
    return sum

class HW2:

    def __init__(self):
        pass

    def example_problem_1(self):
        #EightPuzzle example with A*
        # Default goal is (1, 2, 3, 4, 5, 6, 7, 8, 0)
        #   which represents:   1 2 3
        #                       4 5 6
        #                       7 8 _
        #

        # In this example, we'll construct a puzzle with initial state
        #               1 2 3
        #               4 5 6
        #               _ 7 8
        #
        init = (1, 2, 3, 4, 5, 6, 0, 7, 8)
        puzzle = EightPuzzle(init)

        # Checks whether the initialized configuration is solvable or not
        # this is not a required step, but may be useful in saving you 
        # from impossible configurations
        print("Is the puzzle solvable from this initial state?")
        print(puzzle.check_solvability(init))

        print("A* with default heuristic")
        return astar_search(puzzle).solution()

    def problem_1a(self):
        '''
        1. instantiate the 8 puzzle problem as described in the writeup
        2. return the solution from the Iterative Deepening Search algorithm
        '''
        init = (0, 3, 6, 2, 5, 8, 1, 4, 7)
        puzzle = EightPuzzle(init)
        return iterative_deepening_search(puzzle).solution()
    
    def problem_1b(self):
        '''
        1. instantiate the 8 puzzle problem as described in the writeup
        2. return the solution from the A* search algorithm
        '''
        init = (0, 3, 6, 2, 5, 8, 1, 4, 7)
        puzzle = EightPuzzle(init)
        return astar_search(puzzle).solution()

    def problem_1c(self):
        '''
        1. instantiate 8 puzzle problem as described in the writeup
        2. return the solution from the A* search algorithm
        '''
        init = (6, 0, 2, 5, 1, 3, 4, 8, 7)
        puzzle = EightPuzzle(init)
        return astar_search(puzzle).solution()

    def problem_1d(self):
        '''
        0. Complete the mhd function (defined above class HW2)
        Then,
        1. instantiate the 8 puzzle problem as described in the writeup
        2. write code that will create and use a different heuristic
        3. return the solution from the A* search algorithm
        '''
        init = (6, 0, 2, 5, 1, 3, 4, 8, 7)
        puzzle = EightPuzzle(init)
        return astar_search(puzzle, mhd).solution()

    def problem_2(self):
        '''
        1. find initial states with optimal solutions of lengths 15, 17, 19 and 21
        2. for each of those, for each heuristic, measure the time it takes to 
            find a solution
        Note: It is not required that your code for this be done specifically in 
        this function. It can be elsewhere in the file if you want to structure the 
        code differently. The autograder will not test this code, but we will look 
        at it during manual grading, so if it is not all in this function, leave a 
        comment letting us know where to look.
        '''
        init15 = (1, 2, 3, 0, 4, 5, 6, 7, 8) # 15
        puzzle15 = EightPuzzle(init15)
        puzzle15mhd = EightPuzzle(init15)
        tic = time.perf_counter()
        astar_search(puzzle15).solution()
        toc = time.perf_counter()
        print(f"Puzzle 15: {toc - tic:0.4f} seconds")
        tic = time.perf_counter()
        astar_search(puzzle15mhd, mhd).solution()
        toc = time.perf_counter()
        print(f"Puzzle 15 mhd: {toc - tic:0.4f} seconds")
        init17 = (4, 0, 3, 2, 7, 8, 5, 6, 1) # 17
        puzzle17 = EightPuzzle(init17)
        puzzle17mhd = EightPuzzle(init17)
        tic = time.perf_counter()
        astar_search(puzzle17).solution()
        toc = time.perf_counter()
        print(f"Puzzle 17: {toc - tic:0.4f} seconds")
        tic = time.perf_counter()
        astar_search(puzzle17mhd, mhd).solution()
        toc = time.perf_counter()
        print(f"Puzzle 17 mhd: {toc - tic:0.4f} seconds")
        init19 = (1, 0, 2, 3, 4, 8, 7, 6, 5) # 19
        puzzle19 = EightPuzzle(init19)
        puzzle19mhd = EightPuzzle(init19)
        tic = time.perf_counter()
        astar_search(puzzle19).solution()
        toc = time.perf_counter()
        print(f"Puzzle 19: {toc - tic:0.4f} seconds")
        tic = time.perf_counter()
        astar_search(puzzle19mhd, mhd).solution()
        toc = time.perf_counter()
        print(f"Puzzle 19 mhd: {toc - tic:0.4f} seconds")
        init21 = (1, 0, 2, 3, 4, 5, 6, 7, 8) # 21
        puzzle21 = EightPuzzle(init21)
        puzzle21mhd = EightPuzzle(init21)
        tic = time.perf_counter()
        astar_search(puzzle21).solution()
        toc = time.perf_counter()
        print(f"Puzzle 21: {toc - tic:0.4f} seconds")
        tic = time.perf_counter()
        astar_search(puzzle21mhd, mhd).solution()
        toc = time.perf_counter()
        print(f"Puzzle 21 mhd: {toc - tic:0.4f} seconds")

    def example_problem_3(self):
        '''Use the InstrumentedProblem class to track stats about 
        a breadth-first search and iterative deepening  search 
        on the Romania Map problem.  Returns a tuple of the number 
        of goal tests completed, as stored in the stat tracking object.
        '''
        print("Su: Successor States created")
        print("Go: Number of Goal State checks")
        print("St: States created")
        print("   Su   Go   St")
        g = InstrumentedProblem(GraphProblem('Craiova', 'Zerind', romania_map))
        result = breadth_first_graph_search(g)
        print(g)
        g2 = InstrumentedProblem(GraphProblem('Craiova', 'Zerind', romania_map))
        result2 = iterative_deepening_search(g2)
        print(g2)
        return (g.goal_tests, g2.goal_tests)

    def problem_3a(self):
        '''Use the InstrumentedProblem class to track stats about 
        different searches on the Romania Map problem, according 
        to the specifics given in the writeup. Return a tuple 
        containing each of the entire objects that contain the final 
        stats for each search algorithm.
        '''
        print("Su: Successor States created")
        print("Go: Number of Goal State checks")
        print("St: States created")
        print("   Su   Go   St")
        g = InstrumentedProblem(GraphProblem('Timisoara', 'Pitesti', romania_map))
        result = breadth_first_graph_search(g)
        print(g)
        g2 = InstrumentedProblem(GraphProblem('Timisoara', 'Pitesti', romania_map))
        result2 = depth_first_graph_search(g2)
        print(g2)
        g3 = InstrumentedProblem(GraphProblem('Timisoara', 'Pitesti', romania_map))
        result3 = iterative_deepening_search(g3)
        print(g3)
        g4 = InstrumentedProblem(GraphProblem('Timisoara', 'Pitesti', romania_map))
        result4 = recursive_best_first_search(g4)
        print(g4)
        return (g, g2, g3, g4)

    def problem_3b(self):
        '''Use the InstrumentedProblem class to track stats about 
        different searches on the Romania Map problem, according 
        to the specifics given in the writeup. Return a tuple 
        containing each of the entire objects that contain the final 
        stats for each search algorithm.
        '''
        print("Su: Successor States created")
        print("Go: Number of Goal State checks")
        print("St: States created")
        print("   Su   Go   St")
        g = InstrumentedProblem(GraphProblem('Timisoara', 'Eforie', romania_map))
        result = breadth_first_graph_search(g)
        print(g)
        g2 = InstrumentedProblem(GraphProblem('Timisoara', 'Eforie', romania_map))
        result2 = depth_first_graph_search(g2)
        print(g2)
        g3 = InstrumentedProblem(GraphProblem('Timisoara', 'Eforie', romania_map))
        result3 = iterative_deepening_search(g3)
        print(g3)
        g4 = InstrumentedProblem(GraphProblem('Timisoara', 'Eforie', romania_map))
        result4 = recursive_best_first_search(g4)
        print(g4)
        return (g, g2, g3, g4)


def main():
    
    # Create object, hw2, of datatype HW2.
    hw2 = HW2()
 
    #=======================
    # A* with 8-Puzzle 
    # An example for you to follow to get you started on the EightPuzzle
    print('Example Problem result:')
    print('=======================')
    print(hw2.example_problem_1())
    
    print('Problem 1a result:')
    print('==================')
    print(hw2.problem_1a())

    print('Problem 1b result:')
    print('==================')
    print(hw2.problem_1b())

    print('Problem 1c result:')
    print('==================')
    print(hw2.problem_1c())

    print('Problem 1d result:')
    print('==================')
    print(hw2.problem_1d())

    hw2.problem_2()
    
    print(hw2.example_problem_3())

    print('Problem 3a result:')
    print('==================')
    print(hw2.problem_3a())

    print('Problem 3b result:')
    print('==================')
    print(hw2.problem_3b())
    
if __name__ == '__main__':
    main()
