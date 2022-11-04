import pytest

from LetterCombinationsPhoneNumber.solution import Solution

TEST_CASES = [
    ("", []),
    ("2", ["a", "b", "c"]),
    ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    ("32", ['da', 'db', 'dc', 'ea', 'eb', 'ec', 'fa', 'fb', 'fc']),
    ("234",
     ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 'bdg', 'bdh', 'bdi', 'beg', 'beh', 'bei', 'bfg',
      'bfh', 'bfi', 'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi']),
]


@pytest.mark.parametrize("digits, expected_result", TEST_CASES)
def test_solution(digits, expected_result):
    assert set(Solution.letter_combinations(digits)) == set(expected_result)
