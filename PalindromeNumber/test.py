import pytest

from PalindromeNumber.solution import Solution

TEST_CASES = [
    (121,   10, True),
    (-121,  10, False),
    (10,    10, False),
    (122,   10, False),
    (12321, 10, True),
    (1111,  10, True),
    (0,     10, True),
    (94738, 10, False),
    (43690, 16, True),
    (4641,  16, True),
    (43691, 16, False),
    (231,   2,  True),
    (471,   2,  True),
    (407,   2,  False),
    (1,     2,  True)
]


@pytest.mark.parametrize("x, notation, expected_result", TEST_CASES)
def test_solution(x, notation, expected_result):
    assert Solution.is_palindrome(x, notation) == expected_result
