from __future__ import annotations

from enum import Enum
from typing import List, Tuple


class Board:
    """
    Represents Sudoku board

    Attributes:
        matrix: two-dimensional list of values including blanks
        solved: bool representing the state of the board
        blanks: list of precomputed available blanks
    """

    BLANK = "."
    VALUES = ["9", "8", "7", "6", "5", "4", "3", "2", "1"]
    SIZE = 9

    def a(self, li=[]):
        pass

    def __init__(self, matrix: List[List[str]], initialization=True):
        """
        Instance initialization

        :param matrix: two-dimensional list of predefined values representing the board
        :param initialization:  whether should the blank list be precomputed
        """

        # faster way of copying the 2-d list that deepcopy
        self.matrix = [[*row] for row in matrix]

        self.solved = False
        if initialization:
            self.blanks = self.find_blanks()
        else:
            self.blanks = []

    def __str__(self):
        return "\n".join(["  ".join(row) for row in self.matrix])

    def set_value(self, y: int, x: int, value: str):
        """
        Sets the provided value on the board, preventing from using the matrix directly
        :param y:       y coordinate
        :param x:       x coordinate
        :param value:   value from 1 to 9
        :return:        None
        """
        self.matrix[y][x] = value

    def get_value(self, y: int, x: int):
        """
        Gets the value from the board, preventing from using the matrix directly

        :param y:       y coordinate
        :param x:       x coordinate
        :return:        value from 1 to 9 or blank
        """
        return self.matrix[y][x]

    def find_blanks(self) -> List[Tuple[int, int]]:
        """
        Precomputes list of blanks

        :return:    None
        """
        blanks = []

        # simply iterates over the 2d-list appending the coordinates
        # of the blank slot
        for y, row in enumerate(self.matrix):
            for x, slot in enumerate(row):
                if slot == Board.BLANK:
                    blanks.append((y, x))

        # if there are no available blanks
        # the board is finished
        if not blanks:
            self.solved = True
        return blanks

    @classmethod
    def branch_out(cls, init_board: Board, value: str) -> Tuple[Board, int, int]:
        """
        Copies the board with a specified changed value

        Inserts the provided value in the first precomputed blank

        :param init_board:  initial board that is copied
        :param value:       value that should be inserted in the blank
        :return:            new board, y and x coordinates of the inserted value
        """

        # we initialize a new instance without precomputed blank list
        new_board = cls(init_board.matrix, initialization=False)
        # we copy blank list from the initial board
        new_board.blanks = [*init_board.blanks]
        # pop returns the first element that we use
        # and removes it, as it will not be blank anymore
        blank = new_board.blanks.pop(0)

        # if there are no blanks, the board is finished
        new_board.solved = len(new_board.blanks) <= 0

        # we unpack coordinates and set the value
        y, x = blank
        new_board.set_value(y, x, value)

        return new_board, y, x


class Solution:
    """
    Solves a Sudoku puzzle by filling the empty cells
    """

    @staticmethod
    def check_validity(board: Board, y: int, x: int) -> bool:
        """
        Checks the validity of the provided value in the board

        :param board:   Board instance that is needed to be checked
        :param y:       y coordinate
        :param x:       x coordinate
        :return:        whether the value is correct
        """

        # dictionary is used to have a fast memory
        # we store a value as a key
        # we do not care about a value as the existence of the key is enough,
        # so we only store the bool
        history = {}

        # vertical line is checked by iterating over all y coordinates

        # basically we store the key if it is not in the memory
        # we return False if the key is in the memory
        # we skip the blank value as it does not matter
        for i in range(Board.SIZE):
            if board.get_value(i, x) == Board.BLANK:
                continue
            if history.get(board.get_value(i, x), False):
                return False
            else:
                history[board.get_value(i, x)] = True
        history = {}

        # vertical line is checked by iterating over all y coordinates
        for i in range(Board.SIZE):
            if board.get_value(y, i) == Board.BLANK:
                continue

            if history.get(board.get_value(y, i), False):
                return False
            else:
                history[board.get_value(y, i)] = True

        history = {}
        # inner square
        # `y // 3 * 3` is a fancy way of defining the start of the square
        # ` y // 3 * 3 + 3` is a fancy way of defining the end of the square

        # we do it both for ys and xs
        # and apply the previously defined actions with memory
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
        Solves the puzzle

        Utilizes Backtracking via stack data structure

        :param board:   the Board instance that should be solved
        :return:        the solved Board instance
        """

        # list that is used as a stack data structure
        board_stack = [board]

        # we cycle through the stack until it is not empty,
        # or we find the solved board
        while board_stack:
            # we take the last element
            # and remove it from the stack
            board_candidate = board_stack.pop()

            # we iterate over the all possible values
            for possible_value in Board.VALUES:
                # we create a new board with a new value
                new_board, y, x = Board.branch_out(board_candidate, possible_value)
                # if the value is possible
                if Solution.check_validity(new_board, y, x):
                    # and the board does not have any blanks
                    if new_board.solved:
                        # it is the solution
                        return new_board

                    # if there is blanks
                    else:
                        # we append the stack
                        board_stack.append(new_board)
