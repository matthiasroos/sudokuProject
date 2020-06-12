
import pytest

import solver.backtracking.backtracking
import solver.backtracking.backtracking2
import sudokumain


@pytest.fixture
def mock_sudoku_main():
    mock_main = sudokumain.SudokuMain(file_name='../sudoku.txt')
    return mock_main


def test_smoketest_print_sudoku(mock_sudoku_main):
    mock_sudoku_main.sudoku.print_sudoku()


def test_smoketest_backtracking(mock_sudoku_main):
    sudoku_solver = solver.backtracking.backtracking.BackTracking(board=mock_sudoku_main.sudoku)
    sudoku_solver.run()


def test_smoketest_backtracking2(mock_sudoku_main):
    sudoku_solver = solver.backtracking.backtracking2.BackTracking2(board=mock_sudoku_main.sudoku)
    sudoku_solver.run()
