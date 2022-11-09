from __future__ import annotations

from enum import Enum
from typing import List, Tuple


class Board:
    """
    Represent SudokuSolver board.

    Attributes:
        matrix: two-dimensional list of values including blanks
        solved: bool representing the state of the board
        blanks: list of precomputed available blanks.
    """

    BLANK = "."
    VALUES = ["9", "8", "7", "6", "5", "4", "3", "2", "1"]
    SIZE = 9

    def __init__(self, matrix: List[List[str]], precompute_blanks=True):
        """
        Instance initialization.

        :param matrix: two-dimensional list of predefined values representing the board
        :param precompute_blanks:  whether should the blank list be precomputed.
        """

        # Faster way of copying the 2-d list that deepcopy.
        self.matrix = [[*row] for row in matrix]

        self.solved = False
        if precompute_blanks:
            self.blanks = self.find_blanks()
        else:
            self.blanks = []

    def __str__(self):
        return "\n".join(["  ".join(row) for row in self.matrix])

    def set_value(self, y: int, x: int, value: str):
        """
        Set the provided value on the board, preventing from using the matrix directly.
        :param y:       y coordinate
        :param x:       x coordinate
        :param value:   value from 1 to 9
        :return:        None.
        """
        self.matrix[y][x] = value

    def get_value(self, y: int, x: int):
        """
        Get the value from the board, preventing from using the matrix directly.

        :param y:       y coordinate
        :param x:       x coordinate
        :return:        value from 1 to 9 or blank.
        """
        return self.matrix[y][x]

    def find_blanks(self) -> List[Tuple[int, int]]:
        """
        Precompute list of blanks.

        :return:    None.
        """
        blanks = []

        # Simply iterates over the 2d-list appending the coordinates
        # of the blank slot.
        for y, row in enumerate(self.matrix):
            for x, slot in enumerate(row):
                if slot == Board.BLANK:
                    blanks.append((y, x))

        # If there are no available blanks
        # the board is finished.
        if not blanks:
            self.solved = True
        return blanks

    @classmethod
    def branch_out(cls, init_board: Board, value: str) -> Tuple[Board, int, int]:
        """
        Copy the board with a specified changed value.

        Insert the provided value in the first precomputed blank.

        :param init_board:  initial board that is copied
        :param value:       value that should be inserted in the blank
        :return:            new board, y and x coordinates of the inserted value.
        """

        # Initialize a new instance without precomputed blank list.
        new_board = cls(init_board.matrix, precompute_blanks=False)
        # Copy blank list from the initial board.
        new_board.blanks = [*init_board.blanks]

        blank = new_board.blanks.pop(0)

        # If there are no blanks left, the board is finished.
        new_board.solved = len(new_board.blanks) <= 0

        # Unpack coordinates and set the value.
        y, x = blank
        new_board.set_value(y, x, value)

        return new_board, y, x


class Solution:
    """
    Solves a SudokuSolver puzzle by filling the empty cells.
    """

    @staticmethod
    def check_validity(board: Board, y: int, x: int) -> bool:
        """
        Checks the validity of the provided value in the board.

        :param board:   Board instance that is needed to be checked
        :param y:       y coordinate
        :param x:       x coordinate
        :return:        whether the value is correct.
        """

        # Dictionary is used to have a fast memory
        # it stores a value as a key,
        # but does not care about a value, as the existence of the key is enough,
        # so stores only a bool
        history = {}

        # Vertical line is checked by iterating over all y coordinates.

        # Basically store the key if it is not in the memory,
        # return False if the key is in the memory and
        # skip the blank value as it does not matter.
        for i in range(Board.SIZE):
            if board.get_value(i, x) == Board.BLANK:
                continue
            if history.get(board.get_value(i, x), False):
                return False
            else:
                history[board.get_value(i, x)] = True
        history = {}

        # Vertical line is checked by iterating over all y coordinates.
        for i in range(Board.SIZE):
            if board.get_value(y, i) == Board.BLANK:
                continue

            if history.get(board.get_value(y, i), False):
                return False
            else:
                history[board.get_value(y, i)] = True

        history = {}
        # Inner square.
        # `y // 3 * 3` is a fancy way of defining the start of the square,
        # ` y // 3 * 3 + 3` is a fancy way of defining the end of the square.

        # We do it both for ys and xs
        # and apply the previously defined actions with memory.
        for i in range(y // 3 * 3, y // 3 * 3 + 3):
            for j in range(x // 3 * 3, x // 3 * 3 + 3):
                if board.get_value(i, j) == Board.BLANK:
                    continue

                if history.get(board.get_value(i, j), False):
                    return False
                else:
                    history[board.get_value(i, j)] = True
        return True

    @staticmethod
    def solve(board: Board) -> Board:
        """
        Solves the puzzle.

        Utilizes Backtracking via stack data structure.

        :param board:   the Board instance that should be solved
        :return:        the solved Board instance.
        """

        # List that is used as a stack data structure.
        board_stack = [board]

        # Cycle through the stack until it is not empty,
        # or find the solved board.
        while board_stack:
            # Take the first element
            # and remove it from the stack.
            board_candidate = board_stack.pop()

            # Iterate over the all possible values.
            for possible_value in Board.VALUES:
                # Create a new board with a new value.
                new_board, y, x = Board.branch_out(board_candidate, possible_value)
                # If the value is possible
                if Solution.check_validity(new_board, y, x):
                    # and the board does not have any blanks –
                    if new_board.solved:
                        # it is the solution.
                        return new_board

                    # If there are blanks –
                    else:
                        # append the stack.
                        board_stack.append(new_board)
