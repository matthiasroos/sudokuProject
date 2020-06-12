
from typing import List

import sudokuboard
import sudokuconstraints


class BackTrackingAbstract:

    def __init__(self, board: sudokuboard.SudokuBoard):
        self.board = board
        self.constraints = sudokuconstraints.SudokuConstraints()
        self.solution = None
        self.max_trial_entries = self.board.get_number_of_empty_cells()

    def run(self):
        solution_vector = []
        status = self.backtracking(step=0, solution_vector=solution_vector)
        if status:
            self.solution.print_sudoku()

    def backtracking(self, step: int, solution_vector: List) -> bool:
        pass

