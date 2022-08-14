import pytest

from LongestCommonPrefix.solution import Solution

TEST_CASES = [
    (["flower", "flow", "flight"],  "fl"),
    (["dog", "racecar", "car"],     ""),
    (["car", "carrot", "caramel"],  "car"),
    (["center", "cout", "cin"],     "c")
]


@pytest.mark.parametrize("strings, expected_result", TEST_CASES)
def test_solution(strings, expected_result):
    assert Solution.longest_commonPrefix(strings) == expected_result
