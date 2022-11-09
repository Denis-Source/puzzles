class Solution:
    """
    Convert integer to roman numeral.
    """

    # The solution is based on using a hash map (python dictionary)
    # to store roman number, and it's corresponding value.

    # Besides storing values incrementally
    # The subtracted values (IV, IX etc.) should be stored as well.
    VALUES = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }

    @staticmethod
    def int_to_roman(num: int) -> str:
        """
        Convert roman numeral to its integer representation.

        Use iterative approach.
        :param num:     integer representation
        :return:        roman numeral in a form of a string.
        """
        # The result is stored as a string.
        representation = ""

        # Cycle through the numbers, defined in the class dictionary
        # searching the best suited candidate and subtracting it from the provided number
        # Continue the cycle until the number is zero.
        while num > 0:
            for roman, decimal in Solution.VALUES.items():
                if num >= decimal:
                    num -= decimal
                    # Concatenate the best suited number to the result.
                    representation += roman
                    break
        return representation
