class Solution:
    """
    The solution is based on using a hash map (python dictionary)
    to store roman number and it's corresponding value
    """

    # Besides storing values incrementally
    # We also should have subtracted values separately
    VALUES = {
        "CM": 900,
        "M": 1000,
        "CD": 400,
        "D": 500,
        "C": 100,
        "XC": 90,
        "XL": 40,
        "L": 50,
        "IX": 9,
        "X": 10,
        "IV": 4,
        "V": 5,
        "I": 1
    }

    @staticmethod
    def roman_to_int(s: str, n: int = 0) -> int:
        """
        Solution

        :param s: roman numeral string
        :param n: current sum of values (needed for the method to be recursive)
        :return: integer value of the provided roman numeral string
        """

        # We only check string if it's not empty
        if s:
            # Than we iterate over the keys that are stored in the hash map
            for value in Solution.VALUES.keys():
                # if the value is present at the beginning of the string
                if s.startswith(value):
                    # We increment the converted number
                    n += Solution.VALUES[value]
                    # And call the method itself recursively
                    # supplying the string without the matched number
                    return Solution.roman_to_int(s[len(value):], n)
        # if the string is empty we are done
        # so we return the sum of the values
        else:
            return n
