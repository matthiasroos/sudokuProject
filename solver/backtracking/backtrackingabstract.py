
import abc
from typing import List

import sudokuboard
import sudokuconstraints


class BackTrackingAbstract(metaclass=abc.ABCMeta):

    def __init__(self, board: sudokuboard.SudokuBoard, constraints: sudokuconstraints.SudokuConstraints = None):
        self.board = board

        self.solution = None
        self.max_trial_entries = self.board.get_number_of_empty_cells()

        if constraints is None:
            self.constraints = sudokuconstraints.SudokuConstraints()
        else:
            self.constraints = constraints

    def run(self):
        solution_vector = []
        status = self.backtracking(step=0, solution_vector=solution_vector)
        if status:
            self.solution.print_sudoku()

    @abc.abstractmethod
    def backtracking(self, step: int, solution_vector: List) -> bool:
        pass
