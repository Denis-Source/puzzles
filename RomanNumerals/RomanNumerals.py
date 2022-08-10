class Solution:
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

    def romanToInt(self, s: str, n: int = 0) -> int:
        if s:
            for value in self.VALUES.keys():
                if s.startswith(value):
                    n += self.VALUES[value]
                    return self.romanToInt(s[len(value):], n)
        else:
            return n


if __name__ == '__main__':
    print(Solution().romanToInt("MCMXCIV"))
