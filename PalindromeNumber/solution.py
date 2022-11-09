import math


class Solution:
    """
    Given an integer `x`, return True if `x` is palindrome integer.
    """
    @staticmethod
    def is_palindrome_s(x: int) -> bool:
        """
        Return if number is a palindrome using sting conversion.

        :param x:   number to check
        :return:    whether the number is a palindrome.
        """

        # Convert the number to a string
        str_x = str(x)
        # Iterate over the half of the length of the string.
        for i in range(math.floor(len(str_x) / 2)):
            # If the first(i) and last (-i -1) are not the same
            # The number is not palindrome
            if str_x[i] != str_x[-i - 1]:
                return False
        # Otherwise the number is a palindrome
        return True

    @staticmethod
    def is_palindrome(x: int, notation=10) -> bool:
        """
        Return if number is a palindrome using integer arithmetic.

        Considering that the 'palindromnes' of the number is fixed to the notation,
        the solution based on the modulo and integer division with the value of the notation scale

        :param x:           number to check
        :param notation:    scale notation
        :return:            whether the number is a palindrome.
        """

        # Firstly check if the number is negative.
        # Palindrome can not be negative.
        if x < 0:
            return False

        # Then discover the number length
        # by ceiling the logarithm with a base of notation of the number.
        x_len = math.ceil(math.log(x + 1, notation))

        # Then iterate over the number half of the number length.
        for i in range(math.floor(x_len / 2)):
            # Iteratively discover the left and the right side of the number.

            left = x // pow(notation, i) % notation
            right = x // pow(notation, x_len - i - 1) % notation

            # If they are not equal the number is not a palindrome.
            if left != right:
                return False

        # Otherwise the number is a palindrome.
        return True
