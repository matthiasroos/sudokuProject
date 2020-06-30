import io
import sys
import unittest.mock

import pytest

import solver.backtracking.backtracking
import solver.backtracking.backtracking2
import strategies.collectionstrategy
import strategies.hidden_singles
import strategies.naked_pairs
import strategies.naked_singles
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


@pytest.fixture
def mock_sudoku_load(request):
    mock_main = sudokumain.SudokuMain(file_name='strategies/examples/{}'.format(request.param['file_name']))
    return mock_main


def test_integrationtest_print_sudoku(mock_sudoku_main):
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


def test_integrationtest_backtracking(mock_sudoku_main):
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    sudoku_solver = solver.backtracking.backtracking.BackTracking(board=mock_sudoku_main.sudoku)
    sudoku_solver.run()
    sys.stdout = sys.__stdout__
    assert sudoku_solver.solution.board == SOLUTION


def test_integrationtest_backtracking2(mock_sudoku_main):
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    sudoku_solver = solver.backtracking.backtracking2.BackTracking2(board=mock_sudoku_main.sudoku)
    sudoku_solver.run()
    sys.stdout = sys.__stdout__
    assert sudoku_solver.solution.board == SOLUTION


@pytest.mark.parametrize('mock_sudoku_load', [dict(file_name='naked_singles.txt')], indirect=True)
def test_integrationtest_naked_singles(mock_sudoku_load):
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    sudoku_strategy = strategies.naked_singles.NakedSingles(sudoku=mock_sudoku_load.sudoku,
                                                            candidates=mock_sudoku_load.candidates,
                                                            constraints=mock_sudoku_load.constraints,
                                                            unit='box')
    output_found = sudoku_strategy.detect()
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == 'Naked Single 8 found in box 0\n' \
                                        'Naked Single 7 found in box 3\n' \
                                        'Naked Single 3 found in box 6\n'
    assert output_found == [{8: (0, 0)}, {7: (5, 2)}, {3: (6, 1)}]


@pytest.mark.parametrize('mock_sudoku_load', [dict(file_name='hidden_singles.txt')], indirect=True)
def test_integrationtest_hidden_singles_box(mock_sudoku_load):
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    sudoku_strategy = strategies.hidden_singles.HiddenSingles(sudoku=mock_sudoku_load.sudoku,
                                                              candidates=mock_sudoku_load.candidates,
                                                              constraints=mock_sudoku_load.constraints,
                                                              unit='box')
    output_found = sudoku_strategy.detect()
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == 'Hidden Single 6 found in box 4\n' \
                                        'Hidden Single 7 found in box 8\n'
    assert output_found == [{6: (4, 3)}, {7: (6, 8)}]


@pytest.mark.parametrize('mock_sudoku_load', [dict(file_name='hidden_singles.txt')], indirect=True)
def test_integrationtest_hidden_singles_column(mock_sudoku_load):
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    sudoku_strategy = strategies.hidden_singles.HiddenSingles(sudoku=mock_sudoku_load.sudoku,
                                                              candidates=mock_sudoku_load.candidates,
                                                              constraints=mock_sudoku_load.constraints,
                                                              unit='column')
    output_found = sudoku_strategy.detect()
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == 'Hidden Single 6 found in column 3\n'
    assert output_found == [{6: (4, 3)}]


@pytest.mark.parametrize('mock_sudoku_load', [dict(file_name='naked_pairs.txt')], indirect=True)
def test_integrationtest_naked_pairs_box(mock_sudoku_load):
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    sudoku_strategy = strategies.naked_pairs.NakedPairs(sudoku=mock_sudoku_load.sudoku,
                                                        candidates=mock_sudoku_load.candidates,
                                                        constraints=mock_sudoku_load.constraints,
                                                        unit='box')
    output_found = sudoku_strategy.detect()
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == 'Naked Pair (2, 4) found in box 1\n'
    assert output_found == [{(2, 4): [(2, 3), (2, 5)]}]


@pytest.mark.parametrize('mock_sudoku_load', [dict(file_name='naked_pairs.txt')], indirect=True)
def test_integrationtest_naked_pairs_collection(mock_sudoku_load):
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    sudoku_strategy = strategies.collectionstrategy.CollectionStrategy(sudoku=mock_sudoku_load.sudoku,
                                                                       candidates=mock_sudoku_load.candidates,
                                                                       constraints=mock_sudoku_load.constraints,
                                                                       strategy='naked_pairs',
                                                                       units=['row', 'column', 'box'])
    output_found = sudoku_strategy.detect()
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == 'Naked Pair (2, 4) found in row 2\n' \
                                        'Naked Pair (2, 4) found in box 1\n'
    assert output_found == [{(2, 4): [(2, 3), (2, 5)]}]