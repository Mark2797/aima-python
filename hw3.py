import sys
sys.path.append('aima-python')
from games import *
import math

def c4_eval(state):
    '''Example of an odd function: 
    It likes states where an O has an X to the right of it. 
    Nothing else counts.
    '''
    ev = 0
    for col in range(1,6):
        for row in range(1,8):
            if state.board.get((row,col)) == 'O' and state.board.get((row, col+1)) == 'X':
                ev += 10
    return ev 

def ab_cutoff_player(game, state):
    return alpha_beta_cutoff_search(state, game, d=2, eval_fn=c4_eval)

def check_direction(state, col, row, direction, player):
    left_blocked = False
    right_blocked = False
    check_left = True
    original_col = col
    original_row = row
    if (state.board.get((row,col)) == None): return 0
    current = state.board.get((row, col))
    sum = 1
    for i in range(3):
        if check_left:
            col -= direction[0]
            row -= direction[1]
            if col == 0 or col == 7 or row == 0 or row == 8:
                check_left = False
                left_blocked = True
                col = original_col + direction[0]
                row = original_row + direction[1]
                if state.board.get((row, col)) == current:
                    sum += 1
                elif state.board.get((row, col)) == None:
                    break
                else:
                    right_blocked = True
            else:
                if state.board.get((row, col)) == current:
                    sum += 1
                elif state.board.get((row, col)) == None:
                    check_left = False
                else:
                    left_blocked = True
                    check_left = False
        else:
            col += direction[0]
            row += direction[1]
            if col == 0 or col == 7 or row == 0 or row == 8:
                right_blocked = True
                break
            else:
                if state.board.get((row, col)) == current:
                    sum += 1
                elif state.board.get((row, col)) == None:
                    break
                else:
                    right_blocked = True
                    break
    if left_blocked:
        sum -= 1
    else:
        sum += 1
    if right_blocked:
        sum -= 1
    else:
        sum += 1
    if left_blocked and right_blocked:
        return 0
    elif current == player:
        return sum
    else:
        return -sum
            

# state.to_move returns the opponent's move (O or X)
def connect4_eval(state):
    ev = 0
    opponent = state.to_move
    # direction = (col, row) = (x, y)
    diagonal_up = (1, 1)
    diagonal_down = (1, -1)
    horizontal = (1, 0)
    perpendicular = (0, 1)
    if opponent == 'O': player = 'X'
    else : player = 'O'
    for col in range(1, 7):
        for row in range(1, 8):
            ev += check_direction(state, col, row, diagonal_up, player)
            ev += check_direction(state, col, row, diagonal_down, player)
            ev += check_direction(state, col, row, perpendicular, player)
            ev += check_direction(state, col, row, horizontal, player)
    return ev

def ab_cutoff_new_player(game, state):
    return alpha_beta_cutoff_search(state, game, d=4, eval_fn=connect4_eval)

class HW3:
    def __init__(self):
        pass

    def example_problem_1a(self):
        tt = TicTacToe()
        tt.play_game(alpha_beta_player, query_player)

    def example_problem_1b(self):
        c4 = ConnectFour()
        c4.play_game(ab_cutoff_player, query_player)

    def problem_1d(self):
        c4 = ConnectFour()
        # play as X, if win then return 1
        x = 0
        for i in range(5):
         if c4.play_game(ab_cutoff_new_player, random_player) == 1: x += 1
        # play as O, if win then return -1
        o = 0
        for i in range(5):
         if c4.play_game(random_player, ab_cutoff_new_player) == -1: o += 1
        return (x, o)
    
def main():
    hw3 = HW3()
    # An example for you to follow to get you started on Games
    print('Example Problem, playing Tic Tac Toe:')
    print('=====================================')
    # hw3.example_problem_1a()

    print('Example Problem, playing Connect 4 against my odd eval:')
    print('=======================================================')
    # uncomment to get it to run problem 1b
    # hw3.example_problem_1b()

    # Add code below to test and run problem 1d
    hw3.problem_1d()
    
if __name__ == '__main__':
    main()
