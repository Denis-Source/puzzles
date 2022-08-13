import pytest
from TwoSums.solution import Solution

TEST_CASES = [
    ([2, 7, 11, 15],        9, [0, 1]),
    ([3, 2, 4],             6, [1, 2]),
    ([3, 3],                6, [0, 1]),
    ([1, 2, 2, 3],          4, [1, 2]),
    ([1, 2, 3, 4, 5],       8, [2, 4]),
    ([-1, -2, -3, -4, -5], -8, [2, 4]),
    ([2, 2],                3, []),
    ([],                    4, []),
    ([2, 3, 4, 7],          8, []),
    ([2, 4, 5, 5, 3],       4, [])
]


@pytest.mark.parametrize("nums, target, expected_result", TEST_CASES)
def test_solution(nums, target, expected_result):
    assert Solution.two_sum(nums, target) == expected_result
