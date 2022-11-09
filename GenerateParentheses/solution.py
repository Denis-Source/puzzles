from typing import List


class Solution:
    """
    Generate all well-formed parentheses' combination of given amount.

    All well-formed parentheses should be properly opened and closed.
    """

    # To avoid hard-coding define parentheses as class values.
    OPEN = "("
    CLOSED = ")"

    @staticmethod
    def correctness_function(combination: str, n: int) -> bool:
        """
        Define whether the given combination could be or is correct.

        :param combination:     combination of closed and opened parentheses
        :param n:               amount of possible parentheses
        :return:                whether the combination could be or is correct.
        """

        # If amount of opened parentheses is bigger than possible.
        if combination.count(Solution.OPEN) > n:
            return False

        # If amount of closed is bigger than possible.
        if combination.count(Solution.CLOSED) > combination.count(Solution.OPEN):
            return False

        return True

    @staticmethod
    def generate_parenthesis(n: int) -> List[str]:
        """
        Generate all the possible combinations.

        Utilize an iterative approach, backtracking and stack data structure.
        :param n:       amount of open/closed pairs
        :return:        list of combinations.
        """

        # Stack to store possible correct combinations.
        possibilities = []
        # List to store correct combinations.
        answer = []

        # First possible combination is always an opening parenthesis.
        possibilities.append("(")

        # Continue until the stack is empty.
        while possibilities:
            # The candidate is popped from the stack.
            candidate = possibilities.pop()

            # The actions are the same for closed and opened parentheses.
            for p in (Solution.OPEN, Solution.CLOSED):
                if Solution.correctness_function(candidate + p, n):
                    # If the combination is correct – store it as an answer.
                    if len(candidate + p) == n * 2:
                        answer.append(candidate + p)
                    # if not – append the stack
                    else:
                        possibilities.append(candidate + p)
        return answer
