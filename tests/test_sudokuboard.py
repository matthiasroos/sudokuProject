import pytest

import sudokuboard


@pytest.fixture
def mock_board():
    sudoku = sudokuboard.SudokuBoard()
    sudoku.board = [
        [0, 0, 0, 2, 0, 0, 9, 0, 1],
        [2, 0, 3, 0, 0, 9, 5, 4, 0],
        [8, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 2, 0, 0, 0, 6, 0, 0, 7],
        [0, 0, 6, 0, 4, 0, 3, 0, 0],
        [7, 0, 0, 3, 0, 0, 0, 9, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 6],
        [0, 9, 7, 6, 0, 0, 4, 0, 2],
        [4, 0, 2, 0, 0, 7, 0, 0, 0]
    ]
    return sudoku


def test_get_row(mock_board):
    output_row = mock_board._get_row(pos_row=2)
    assert output_row == [8, 0, 0, 0, 0, 0, 2, 0, 0]


def test_get_column(mock_board):
    output_column = mock_board._get_column(pos_column=3)
    assert output_column == [2, 0, 0, 0, 0, 3, 0, 6, 0]


def test_get_box(mock_board):
    output_box = mock_board._get_box(box_num=0)
    assert output_box == [0, 0, 0, 2, 0, 3, 8, 0, 0]
