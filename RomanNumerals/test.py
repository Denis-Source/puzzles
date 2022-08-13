import pytest

from RomanNumerals.solution import Solution

TEST_CASES = [
    ("III",         3),
    ("LVIII",       58),
    ("MCMXCIV",     1994),
    ("IX",          9),
    ("XXI",         21),
    ("MMMDCCXXIV",  3724),
    ("CXXIII",      123),
    ("CMXCIX",      999)
]


@pytest.mark.parametrize("s, expected_result", TEST_CASES)
def test_solution(s, expected_result):
    assert Solution.roman_to_int(s) == expected_result
