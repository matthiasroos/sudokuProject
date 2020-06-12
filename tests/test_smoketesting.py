
import io
import sys
import unittest.mock

import pytest

import solver.backtracking.backtracking
import solver.backtracking.backtracking2
import sudokumain

SUDOKU = '7,9,0,0,3,8,0,0,1\n\
0,5,3,1,2,4,8,0,9\n\
0,4,0,6,9,7,0,0,2\n\
3,7,0,4,0,9,1,2,8\n\
2,0,9,8,0,5,4,0,3\n\
4,6,8,3,0,2,0,5,7\n\
1,0,0,9,5,3,0,8,0\n\
5,0,4,7,8,1,2,9,0\n\
9,0,0,2,4,0,0,1,5'

SOLUTION = [[7, 9, 2, 5, 3, 8, 6, 4, 1],
            [6, 5, 3, 1, 2, 4, 8, 7, 9],
            [8, 4, 1, 6, 9, 7, 5, 3, 2],
            [3, 7, 5, 4, 6, 9, 1, 2, 8],
            [2, 1, 9, 8, 7, 5, 4, 6, 3],
            [4, 6, 8, 3, 1, 2, 9, 5, 7],
            [1, 2, 6, 9, 5, 3, 7, 8, 4],
            [5, 3, 4, 7, 8, 1, 2, 9, 6],
            [9, 8, 7, 2, 4, 6, 3, 1, 5]]


@pytest.fixture
def mock_sudoku_main():
    with unittest.mock.patch('builtins.open', unittest.mock.mock_open(read_data=SUDOKU), create=True) as mocked_open:
        mock_main = sudokumain.SudokuMain(file_name='test')
    return mock_main


def test_smoketest_print_sudoku(mock_sudoku_main):
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    mock_sudoku_main.sudoku.print_sudoku()
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == "[7, 9, 0, 0, 3, 8, 0, 0, 1]\n" \
                                        "[0, 5, 3, 1, 2, 4, 8, 0, 9]\n" \
                                        "[0, 4, 0, 6, 9, 7, 0, 0, 2]\n" \
                                        "[3, 7, 0, 4, 0, 9, 1, 2, 8]\n" \
                                        "[2, 0, 9, 8, 0, 5, 4, 0, 3]\n" \
                                        "[4, 6, 8, 3, 0, 2, 0, 5, 7]\n" \
                                        "[1, 0, 0, 9, 5, 3, 0, 8, 0]\n" \
                                        "[5, 0, 4, 7, 8, 1, 2, 9, 0]\n" \
                                        "[9, 0, 0, 2, 4, 0, 0, 1, 5]\n"


def test_smoketest_backtracking(mock_sudoku_main):
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    sudoku_solver = solver.backtracking.backtracking.BackTracking(board=mock_sudoku_main.sudoku)
    sudoku_solver.run()
    sys.stdout = sys.__stdout__
    assert sudoku_solver.solution.board == SOLUTION


def test_smoketest_backtracking2(mock_sudoku_main):
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    sudoku_solver = solver.backtracking.backtracking2.BackTracking2(board=mock_sudoku_main.sudoku)
    sudoku_solver.run()
    sys.stdout = sys.__stdout__
    assert sudoku_solver.solution.board == SOLUTION
