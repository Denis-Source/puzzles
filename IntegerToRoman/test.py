import pytest

from IntegertoRoman.solution import Solution

TEST_CASES = [
    (3, "III"),
    (58, "LVIII"),
    (1994, "MCMXCIV"),
    (9, "IX"),
    (21, "XXI"),
    (3724, "MMMDCCXXIV"),
    (123, "CXXIII"),
    (999, "CMXCIX")
]


@pytest.mark.parametrize("n, expected_result", TEST_CASES)
def test_solution(n, expected_result):
    assert Solution.int_to_roman(n) == expected_result
