#!/usr/bin/python3
"""this is the N-queens puzzle solution.

Specifies all feasible methods for putting NN non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an int >= 4.

Attributes:
    board (list): list of lists representing chessboard.
    solutions (list): list of lists containing solutions.

Solutions are represented in this format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent row and column, respectively, where a
queen must be on chessboard.
"""
import sys


def init_board(n):
    """this initialize `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """this return deepcopy of chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """A list of lists that represent the solved chessboard is returned."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def xout(board, row, col):
    """X out spots on chessboard.

    Non-attacking queens are no longer allowed to play in the spots that are X-ed out.

    Args:
        board (list): current working chessboard.
        row (int): row where queen was last played.
        col (int): column where queen was last played.
    """
    
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """this recursively solves N-queens puzzle.

    Args:
        board (list): current working chessboard.
        row (int): current working row.
        queens (int): current number of placed queens.
        solutions (list): list of lists of solutions.
    Returns:
        the solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a num")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
