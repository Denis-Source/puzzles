from typing import Tuple


class Solution:
    """
    Converts the non-negative integer to its English representation

    The main caveat is non-consistency of rules how the representation is formed
    """

    # as a start we store all the different words in a dictionary
    # key being integer representation and value English representation

    # from 1 to 9 is obvious ones
    # from 10 to 19 as there are no consistency on how they are formed
    # all the dozens
    # the rest is self-explanatory

    # the order is important and is needed for the `find_in_dictionary()` method
    VALUES = {
        1e9: "Billion",
        1e6: "Million",
        1e3: "Thousand",
        1e2: "Hundred",
        90: "Ninety",
        80: "Eighty",
        70: "Seventy",
        60: "Sixty",
        50: "Fifty",
        40: "Forty",
        30: "Thirty",
        20: "Twenty",
        19: "Nineteen",
        18: "Eighteen",
        17: "Seventeen",
        16: "Sixteen",
        15: "Fifteen",
        14: "Fourteen",
        13: "Thirteen",
        12: "Twelve",
        11: "Eleven",
        10: "Ten",
        9: "Nine",
        8: "Eight",
        7: "Seven",
        6: "Six",
        5: "Five",
        4: "Four",
        3: "Three",
        2: "Two",
        1: "One",
    }
    # The zero is unique as its value being subtracted does not mean anything
    ZERO = "Zero"

    # The "exceptions" is a misnomer as it is on the contrary –
    # gives an opportunity to have a recursive call
    EXCEPTIONS = [1e9, 1e6, 1e3, 1e2]

    @staticmethod
    def find_in_dictionary(num: int) -> Tuple[int, str]:
        """
        Searches the dictionary for the most suitable key-value pair

        For example providing 65-integer we should get 60, Sixty
        But providing 5 we should get Five

        :param num:     integer search is based on
        :return:        integer-English representation pair
        """

        # although we use dictionary we cannot utilize its O(K) power
        # as we need the most suitable and not the exact key-value pair
        for decimal, word in Solution.VALUES.items():
            if num >= decimal:
                return decimal, word

    @staticmethod
    def number_to_words(num: int, answer=None) -> str:
        """
        Converts integer to English representation

        Utilizes recursive call

        :param num:         integer form
        :param answer:      already stacked word formation that is used for the recursion
        :return:            English form
        """

        # for convenience, we use list to store words
        # if it is not supplied, we initialize it

        # it is important we do it here and not in the default argument section
        if answer is None:
            answer = []

        # 0 being the unique case and is only used if the supplied value is exactly that
        if num == 0:
            return Solution.ZERO

        # firstly we iterate the "exceptions"
        # given the example of "205 320"
        # there we sort out the "205" part by adding word "Thousand" and the quantity of them (205)
        # than we sort out the "5" part by adding word "Hundred" and the quantity of them (2)

        # the "320" resolves the same principle
        for exc in Solution.EXCEPTIONS:
            if num >= exc:
                # we append the list by the "Thousand" or etc
                # recursively calling to find their values
                answer.append(Solution.number_to_words(num // exc))
                # we subtract those values from the supplied number
                num %= exc
                # num -= num // exc * exc
                answer.append(Solution.VALUES[exc])

        # after the "exceptions", the "regular" numbers are sorted out:
        # the "5" and "20" parts
        while num > 0:
            # we search the most suited value, add it to the list and subtract it
            decimal, word = Solution.find_in_dictionary(num)
            answer.append(word)
            num -= decimal

        # when the value is exhausted we return the glue it together
        # and return it
        return " ".join(answer)
