from __future__ import annotations
import time
from typing import List, Tuple


class Board:
    """
    Represents board containing queens

    Attributes:
        queens: number of queens on the board
        size:   size of the board (can only be in a form of a square)
        matrix: two-dimensional list representing the contents of the board
        blanks: list of blanks in a form of x-y tuples
    """
    QUEEN = "Q"
    BLANK = " "
    BLANK_CHECKED = "."

    def __init__(self, size: int, precompute: bool = True):
        """
        Instance initialization

        :param size: dimensions of the board
        :param precompute:  whether should the blank list and matrix be precomputed
        """

        self.queens = 0
        self.size = size

        if precompute:
            self.matrix = [[self.BLANK] * size for y in range(size)]
            self.blanks = [(y, x) for x in range(size) for y in range(size)]
        else:
            self.matrix = None
            self.blanks = None

    def __str__(self):
        return "\n".join(
            (["".join([f" {c} " for c in r]) for r in self.matrix])
        )

    def __hash__(self) -> int:
        """
        Defines hash method for the class

        Is needed to store a board instance in the set
        Uses string representation

        :return:    hash representation in an integer form
        """
        return hash(str(self))

    def __eq__(self, other) -> bool:
        """
        Defines equality operation for the class

        Is needed to store a board instance in the set as it uses this method as well
        Uses defined earlier __hash__ magic method

        :param other:   another Board instance to be compared to
        :return:        equality of the boards
        """
        return hash(self) == hash(other)

    @classmethod
    def copy(cls, other_board: Board) -> Board:
        """
        Copies the board
        :param other_board:     a Board instance the copy is based on
        :return:                new board instance
        """

        # we create a new instance without precomputed values
        board = cls(other_board.size, precompute=False)
        # we copy 2d list and blanks (faster than deepcopy)
        board.matrix = [[*r] for r in other_board.matrix]
        board.blanks = [*other_board.blanks]
        board.queens = other_board.queens

        return board

    def get_blank(self) -> Tuple[int, int]:
        """
        Returns first available blank if one available
        :return:
        """
        try:
            return self.blanks.pop()
        except IndexError:
            return None

    def insert_value(self, y: int, x: int, value: str, pop=False) -> None:
        """
        Inserts the value in the specified coordinates

        Is expensive if used with pop set to True
        As it uses `list.remove()` method

        :param y:       y coordinate
        :param x:       x coordinate
        :param value:   new value
        :param pop:     should the blank with specified coordinates be removed
        :return:        None
        """
        if pop:
            self.blanks.remove((y, x))
        if value == self.QUEEN:
            self.queens += 1
        self.matrix[y][x] = value

    def check_position(self, y: int, x: int) -> bool:
        """
        Checks the specified coordinates are suitable for the queen

        By the rules of Chess, Queens can go vertically, horizontally and diagonally.

        :param y:   y coordinate
        :param x:   x coordinate
        :return:    whether the queen can be placed
        """

        # Firstly we check vertical and horizontal lines
        for i in range(self.size):
            if self.matrix[i][x] == self.QUEEN:
                return False

            if self.matrix[y][i] == self.QUEEN:
                return False

        # Secondly we check left to right diagonal
        # We generate offset which defines how diagonal (pool of y-x coordinate pairs)
        # is moved to the right from the centered diagonal (0,0; 1,1; 2,2; etc)
        offset = y - x
        for i in range(self.size):
            try:
                if i + offset >= 0:
                    if self.matrix[i + offset][i] == self.QUEEN:
                        return False

            except IndexError:
                break

        # Right to left diagonal is basically the same thing
        # only the majority of its values are reverted
        # The centered right to left diagonal for size of 3 being 0, 2; 1, 1; 0, 2.
        offset = y - (self.size - x - 1)
        for i in range(self.size):
            new_y = self.size - 1 - i
            new_x = self.size - 1 - (self.size - 1 - i - offset)
            if new_y < 0 or new_x < 0:
                continue

            try:
                if self.matrix[new_y][new_x] == self.QUEEN:
                    return False
            except IndexError:
                break

        return True


class Solution:
    """
    Solves a NQueens
    """
    @staticmethod
    def solve(n: int) -> List[Board]:
        """
        Solves the puzzle by utilizing backtracking.

        :param n:   dimensions of the board and the amount of queens
        :return:    list of possible boards
        """

        # list that is used as a stack data structure
        board_stack = [Board(n)]
        # We store the list of answers in a form of a set() to filter out duplicates
        answer = set()

        # We cycle through the stack until it is not empty
        # adding the suitable board to the set
        while board_stack:
            # we take the first element
            # and remove it from the stack
            curr_board = board_stack.pop()

            # we iterate over the board available blanks inserting the queens
            # or mark the blank with the checked value
            blank = curr_board.get_blank()
            while blank:
                y, x = blank
                # if the queen is possible
                if curr_board.check_position(y, x):
                    # we simultaneously copy the board inserting the blank checked value and appending the stack
                    # and queen value to progress further
                    new_board = Board.copy(curr_board)
                    new_board.insert_value(y, x, Board.BLANK_CHECKED)
                    board_stack.append(new_board)

                    curr_board.insert_value(y, x, Board.QUEEN)
                else:
                    curr_board.insert_value(y, x, Board.BLANK_CHECKED)

                blank = curr_board.get_blank()

            # if the board is suitable
            # we append the answer
            if curr_board.queens == n:
                answer.add(curr_board)

        return list(answer)
