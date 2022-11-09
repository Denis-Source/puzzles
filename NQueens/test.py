import pytest

from NQueens.solution import Solution

TEST_CASES = [
    (1, [[["Q"]]]),
    (2, []),
    (4, [[['.', 'Q', '.', '.'],
          ['.', '.', '.', 'Q'],
          ['Q', '.', '.', '.'],
          ['.', '.', 'Q', '.']],
         [['.', '.', 'Q', '.'],
          ['Q', '.', '.', '.'],
          ['.', '.', '.', 'Q'],
          ['.', 'Q', '.', '.']]]
     ),
    (6, [
        [['.', '.', '.', '.', 'Q', '.'],
         ['.', '.', 'Q', '.', '.', '.'],
         ['Q', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', 'Q'],
         ['.', '.', '.', 'Q', '.', '.'],
         ['.', 'Q', '.', '.', '.', '.']],

        [['.', '.', 'Q', '.', '.', '.'],
         ['.', '.', '.', '.', '.', 'Q'],
         ['.', 'Q', '.', '.', '.', '.'],
         ['.', '.', '.', '.', 'Q', '.'],
         ['Q', '.', '.', '.', '.', '.'],
         ['.', '.', '.', 'Q', '.', '.']],

        [['.', '.', '.', 'Q', '.', '.'],
         ['Q', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', 'Q', '.'],
         ['.', 'Q', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', 'Q'],
         ['.', '.', 'Q', '.', '.', '.']],

        [['.', 'Q', '.', '.', '.', '.'],
         ['.', '.', '.', 'Q', '.', '.'],
         ['.', '.', '.', '.', '.', 'Q'],
         ['Q', '.', '.', '.', '.', '.'],
         ['.', '.', 'Q', '.', '.', '.'],
         ['.', '.', '.', '.', 'Q', '.']]]
     )
]


@pytest.mark.parametrize("n, expected_result", TEST_CASES)
def test_solution(n, expected_result):
    assert set(
        ["\n".join(["".join(row) for row in board.matrix]) for board in Solution.solve(n)]
    ) == set(
        ["\n".join(["".join(row) for row in board]) for board in expected_result]
    )
