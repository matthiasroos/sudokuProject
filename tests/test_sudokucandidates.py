import pytest

import sudokucandidates
from tests.test_sudokuboard import mock_board


@pytest.fixture
def mock_candidates(mock_board):
    candidates = sudokucandidates.SudokuCandidates(sudoku=mock_board)
    return candidates


def test_find_candidates(mock_board):
    candidates = sudokucandidates.SudokuCandidates(sudoku=mock_board)

    assert candidates.candidates == [[{5, 6}, {4, 5, 6, 7}, {4, 5}, set(), {3, 5, 6, 7, 8}, {3, 4, 5, 8}, set(),
                                      {3, 6, 7, 8}, set()],
                                     [set(), {1, 6, 7}, set(), {1, 7, 8}, {1, 6, 7, 8}, set(), set(), set(), {8}],
                                     [set(), {1, 4, 5, 6, 7}, {1, 4, 5, 9}, {1, 4, 5, 7}, {1, 3, 5, 6, 7}, {1, 3, 4, 5},
                                      set(), {3, 6, 7}, {3}],
                                     [{1, 3, 5, 9}, set(), {1, 4, 5, 9}, {8, 1, 5, 9}, {8, 1, 5, 9}, set(), {8, 1},
                                      {8, 1, 5}, set()],
                                     [{1, 5, 9}, {8, 1, 5}, set(), {1, 5, 7, 8, 9}, set(), {8, 1, 2, 5}, set(),
                                      {8, 1, 2, 5}, {8, 5}],
                                     [set(), {8, 1, 4, 5}, {1, 4, 5}, set(), {8, 1, 2, 5}, {8, 1, 2, 5}, {8, 1, 6},
                                      set(), {8, 4, 5}],
                                     [{1, 3, 5}, {1, 3, 5}, set(), {1, 4, 5, 9}, {1, 2, 3, 5, 9}, {1, 2, 3, 4, 5},
                                      {1, 7}, {1, 3, 5, 7}, set()],
                                     [{1, 3, 5}, set(), set(), set(), {8, 1, 3, 5}, {8, 1, 3, 5}, set(), {8, 1, 3, 5},
                                      set()],
                                     [set(), {1, 3, 5, 6}, set(), {8, 1, 5, 9}, {1, 3, 5, 8, 9}, set(), {8, 1},
                                      {8, 1, 3, 5}, {8, 9, 3, 5}]]
