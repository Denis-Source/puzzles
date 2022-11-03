import pytest

from IntegertoEnglishWords.solution import Solution

TEST_CASES = [
    (0,             "Zero"),
    (5,             "Five"),
    (65,            "Sixty Five"),
    (123,           "One Hundred Twenty Three"),
    (99999,         "Ninety Nine Thousand Nine Hundred Ninety Nine"),
    (1000000,       "One Million"),
    (54675435,      "Fifty Four Million Six Hundred Seventy Five Thousand Four Hundred Thirty Five"),
    (12345678910,   "Twelve Billion Three Hundred Forty Five Million Six Hundred Seventy Eight Thousand Nine Hundred Ten")
]


@pytest.mark.parametrize("num, expected_result", TEST_CASES)
def test_solution(num, expected_result):
    assert Solution.number_to_words(num) == expected_result
