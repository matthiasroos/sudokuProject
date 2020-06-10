
from typing import Iterable, List, Set, Tuple

import sudokuboard
import sudokucandidates
import sudokuconstraints
import sudokuutils
import solver.backtracking








class SudokuMain:

    def __init__(self, file_name):
        self.sudoku = sudokuboard.SudokuBoard()
        self.sudoku.read_sudoku(file=file_name)
        self.candidates = sudokucandidates.SudokuCandidates()
        self.constraints = sudokuconstraints.SudokuConstraints()

    def input_number(self, pos_row: int, pos_column: int, number: int):
        self.sudoku.enter_number(pos_row=pos_row, pos_column=pos_column, number=number)
        self.candidates.update_candidates(pos_row=pos_row, pos_column=pos_column, delete_num=number)

    def test_number(self, pos_row: int, pos_column: int, number: int):
        for constraint in self.constraints:
            pass

    def check_sudoku(self):
        return self.constraints.check_sudoku(board=self.sudoku)

    def find_naked_single(self):
        pass

    def run(self):
        pass






if __name__ == "__main__":
    main_sudoku = SudokuMain(file_name='sudoku.txt')
    # sudoku.print_sudoku()
    # solver.sudoku.print_sudoku()
    # main_sudoku.candidates.find_candidates()
    # main_sudoku.sudoku.enter_number(pos_row=1, pos_column=0, number=6)
    # main_sudoku.candidates.update_candidates(pos_row=1, pos_column=0, delete_num=6)
    # print(main_sudoku.candidates)
    main_sudoku.sudoku.print_sudoku()
    print(main_sudoku.sudoku.get_number_of_empty_cells())
    solver = solver.backtracking.BackTracking(main_sudoku.sudoku)
    solver.run()
    solver.solution.print_sudoku()




