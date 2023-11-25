"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
       # Count the number of moves played so far
    count_moves = sum(row.count('X') + row.count('O') for row in board)

    # If the count is even, it's player X's turn; otherwise, it's player O's turn
    return 'X' if count_moves % 2 == 0 else 'O'

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_moves.add((i, j))

    return possible_moves

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

     # Ensure the action is within the valid range
    i, j = action
    if not (0 <= i < 3) or not (0 <= j < 3) or board[i][j] != EMPTY:
        raise ValueError("Invalid action")

    # Create a deep copy of the board to avoid modifying the original
    new_board = copy.deepcopy(board)

    # Determine whose turn it is (X or O)
    current_player = player(board)

    # Update the new board with the player's move
    new_board[i][j] = current_player

    return new_board


    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

     # Check rows
    for row in board:
        if row.count('X') == 3:
            return 'X'
        elif row.count('O') == 3:
            return 'O'

    # Check columns
    for col in range(3):
        if all(board[row][col] == 'X' for row in range(3)):
            return 'X'
        elif all(board[row][col] == 'O' for row in range(3)):
            return 'O'

    # Check diagonals
    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'X' for i in range(3)):
        return 'X'
    elif all(board[i][i] == 'O' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
        return 'O'

    # No winner
    return None
    

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

     # Check if there is a winner
    if winner(board) is not None:
        return True

    # Check if the board is full
    if all(cell != EMPTY for row in board for cell in row):
        return True

    # If neither condition is met, the game is still in progress
    return False

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_result = winner(board)

    if winner_result == 'X':
        return 1
    elif winner_result == 'O':
        return -1
    else:
        return 0

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    player_to_move = player(board)

    if player_to_move == 'X':
        _, move = max_value(board)
    else:
        _, move = min_value(board)

    return move

def max_value(board):
    """
    Returns the maximum utility value and corresponding move for the maximizing player.
    """
    if terminal(board):
        return utility(board), None

    max_utility = float('-inf')
    best_move = None

    for action in actions(board):
        new_utility, _ = min_value(result(board, action))
        if new_utility > max_utility:
            max_utility = new_utility
            best_move = action

    return max_utility, best_move

def min_value(board):
    """
    Returns the minimum utility value and corresponding move for the minimizing player.
    """
    if terminal(board):
        return utility(board), None

    min_utility = float('inf')
    best_move = None

    for action in actions(board):
        new_utility, _ = max_value(result(board, action))
        if new_utility < min_utility:
            min_utility = new_utility
            best_move = action

    return min_utility, best_move

    raise NotImplementedError
