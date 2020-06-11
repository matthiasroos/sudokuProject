
from typing import List, Optional, Tuple

import sudokuboard
import sudokuconstraints


class BackTracking:

    def __init__(self, board: sudokuboard.SudokuBoard):
        self.board = board
        self.constraints = sudokuconstraints.SudokuConstraints()
        self.solution = None
        self._solved = False
        self.max_trial_entries = self.board.get_number_of_empty_cells()

    def run(self):
        solution_vector = []
        self.backtracking(solution_vector=solution_vector)
        self.solution.print_sudoku()

    def backtracking(self, solution_vector: List):
        if self._reject(solution_vector):
            return None
        if self._accept(solution_vector):
            self._output(solution_vector=solution_vector)
        future_solution = self._first(solution_vector=solution_vector)
        while future_solution:
            print(future_solution)
            self.backtracking(solution_vector=future_solution)
            future_solution = self._next(solution_vector=solution_vector)

    def _reject(self, solution_vector: List) -> bool:
        board = sudokuboard.insert_solution_vector_into_board(solution_vector=solution_vector, board=self.board)
        return not self.constraints.check_sudoku(board=board)

    def _accept(self, solution_vector: List) -> bool:
        board = sudokuboard.insert_solution_vector_into_board(solution_vector=solution_vector, board=self.board)
        if board.is_complete():
            return True
        return False

    def _first(self, solution_vector: List) -> Optional[List]:
        if not self._solved:
            solution_vector.append(1)
            return solution_vector
        return None

    def _next(self, solution_vector: List) -> Optional[List]:
        if self._solved:
            return None
        last_element = solution_vector.pop(-1)
        if last_element < 9:
            solution_vector.append(last_element + 1)
            return solution_vector
        return None

    def _output(self, solution_vector: List):
        self.solution = sudokuboard.insert_solution_vector_into_board(solution_vector=solution_vector, board=self.board)
        self._solved = True





