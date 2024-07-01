#!/usr/bin/python3


"""
    N-Queens problem.

    Usage: nqueens N:
        where N is an integer greater or equal to 4.
        Print every possible solution to the problem.
"""


import sys


def print_board(board):
    """
    Print the board.

    Args:
        board - list of list with length sys.argv[1]
    """
    for row in board:
        print(row)


def is_safe(board, row, col, n):
    """
    Check if it is safe to place a queen in the given position.

    Args:
        board - list of list with length sys.argv[1]
        row - row to check if is safe doing a movement in this position
        col - col to check if is safe doing a movement in this position
        n: size of the board

    Return:
        True of False
    """

    # Check this row in the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, col, n):
    """
    Find all the possibilities of answer.

    Args:
        board - Board to resolve
        col - Number of column
        n - size of the board

    Returns:
        All the possibilities to solve the problem
    """

    if (col == n):
        print_board(board)
        return True
    res = False
    for i in range(n):

        if (is_safe(board, i, col, n)):

            # Place this queen in board[i][col]
            board[i][col] = 1

            # Make result true if any placement
            # is possible
            res = solve_n_queens(board, col + 1, n) or res

            board[i][col] = 0  # BACKTRACK

    return res


def is_solve(n):
    """
    Find all the possibilities if exists.

    Args:
        n - size of the board
    """
    board = [[0 for i in range(n)] for i in range(n)]

    if not solve_n_queens(board, 0, n):
        return False

    return True


def check_validation(args):
    """
    Validate the input data to verify if the size to answer is posible.

    Args:
        args - sys.argv
    """
    if (len(args) == 2):
        # Validate data
        try:
            n = int(args[1])
        except Exception:
            print("N must be a number")
            exit(1)
        if n < 4:
            print("N must be at least 4")
            exit(1)
        return n
    else:
        print("Usage: nqueens N")
        exit(1)


if __name__ == "__main__":
    """
    Main method to execute the application
    """

    n = check_validation(sys.argv)
    is_solve(n)
