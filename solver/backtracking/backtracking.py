
from typing import List, Optional, Tuple

import solver.backtracking.backtrackingabstract
import sudokuboard


class BackTracking(solver.backtracking.backtrackingabstract.BackTrackingAbstract):

    def backtracking(self, step: int, solution_vector: List) -> bool:
        if self._reject(solution_vector):
            return False
        if self._accept(solution_vector):
            self._output(solution_vector=solution_vector)
            return True
        future_solution = self._first(solution_vector=solution_vector)
        while future_solution:
            print(future_solution)
            if self.backtracking(step=step + 1, solution_vector=future_solution):
                return True
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
        solution_vector.append(1)
        return solution_vector

    def _next(self, solution_vector: List) -> Optional[List]:
        last_element = solution_vector.pop(-1)
        if last_element < 9:
            solution_vector.append(last_element + 1)
            return solution_vector
        return None

    def _output(self, solution_vector: List):
        self.solution = sudokuboard.insert_solution_vector_into_board(solution_vector=solution_vector, board=self.board)






