from typing import List
from itertools import product


class Solution:
    """
    Returns all possible letter combinations that the numbers could represent
    """

    # Dictionary that represents digit-to-letters mappings
    key_dict = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    @staticmethod
    def letter_combinations(digits: str) -> List[str]:
        """
        Generates all possible combinations via recursion

        :param digits:  string containing digits
        :return:        list of possible combinations
        """

        # list to store the answer
        combinations = []

        # if the provided string is empty, return nothing
        if len(digits) == 0:
            return []

        # if the provided string contains 1 digit
        # we at the bottom of the recursion call
        # we return unpacked (list of) letters that mapped to the digit
        if len(digits) == 1:
            return [*Solution.key_dict[digits]]

        # we get the all the letters mapped to first digit in provided string
        # and iterate over them
        for letter in Solution.key_dict[digits[0]]:
            # we call method recursively providing remaining digits
            # iterate over that list of combinations
            for previous_combination in Solution.letter_combinations(digits[1:]):
                # sticking it together with the letter we get earlier
                combinations.append(letter + previous_combination)

        return combinations
