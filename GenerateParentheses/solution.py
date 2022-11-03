from typing import List


class Solution:
    """
    Generates all well-formed parentheses' combination of given amount

    All well-formed parentheses should be properly opened and closed
    """

    # To avoid hard-coding we can define parentheses as class values
    OPEN = "("
    CLOSED = ")"

    @staticmethod
    def correctness_function(combination: str, n: int) -> bool:
        """
        Defines whether the given combination could be or is correct

        :param combination:     combination of closed and opened parentheses
        :param n:               amount of possible parentheses
        :return:                whether the combination could be or is correct
        """

        # if amount of opened parentheses is bigger than possible
        if combination.count(Solution.OPEN) > n:
            return False

        # if amount of closed is bigger than possible
        if combination.count(Solution.CLOSED) > combination.count(Solution.OPEN):
            return False

        return True

    @staticmethod
    def generate_parenthesis(n: int) -> List[str]:
        """
        Generates all the possible combinations

        Utilizes an iterative approach, backtracking and stack data structure
        :param n:       amount of open/closed pairs
        :return:        list of combinations
        """

        # list to store possible correct combinations aka stack
        possibilities = []
        # list to store correct combinations
        answer = []

        # first possible combination is always an opening parenthesis
        possibilities.append("(")

        # we continue until the stack is empty
        while possibilities:
            # the candidate is popped from the stack
            candidate = possibilities.pop()

            # the actions are the same for closed and opened parentheses
            for p in (Solution.OPEN, Solution.CLOSED):
                if Solution.correctness_function(candidate + p, n):
                    # if the combination is correct we add store it as an answer
                    if len(candidate + p) == n * 2:
                        answer.append(candidate + p)
                    # if not, we append the stack
                    else:
                        possibilities.append(candidate + p)
        return answer


if __name__ == '__main__':
    print(Solution.generate_parenthesis(8))
