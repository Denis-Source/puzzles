import pytest

from TrappingRainWater.solution import Solution

TEST_CASES = [
    ([3, 1, 2],                                                         1),
    ([1, 2, 3, 4, 5],                                                   0),
    ([4, 2, 0, 3, 2, 5],                                                9),
    ([1, 0, 2, 1, 0, 1, 3],                                             5),
    ([4, 1, 0, 0, 1, 4, 6, 5, 5, 3],                                    14),
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],                              6),
    ([1, 4, 3, 2, 5, 9, 4, 3, 3, 10, 5, 10, 2, 0, 7, 5, 9, 10, 6, 4],   52)
]


@pytest.mark.parametrize("heights_list, expected_result", TEST_CASES)
def test_recursive_solution(heights_list, expected_result):
    assert Solution.trap_recursively(heights_list) == expected_result


@pytest.mark.parametrize("heights_list, expected_result", TEST_CASES)
def test_scanning_solution(heights_list, expected_result):
    assert Solution.trap_scanning(heights_list) == expected_result
