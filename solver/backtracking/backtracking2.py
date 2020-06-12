
from typing import List, Optional, Tuple

import solver.backtracking.backtrackingabstract
import sudokuboard


class BackTracking2(solver.backtracking.backtrackingabstract.BackTrackingAbstract):

    def backtracking(self, step: int, solution_vector: List) -> bool:

        def increase_number_if_possible(sol_vec: List):
            curr = sol_vec.pop(-1)
            if curr == 9:
                increase_number_if_possible(sol_vec=sol_vec)
            else:
                sol_vec.append(curr + 1)
            return sol_vec

        while True:
            print(f'{solution_vector} {len(solution_vector)}')
            # Append 1 at the beginning and for each new step
            if (not solution_vector) or \
                    ((step > (len(solution_vector) - 1)) and (len(solution_vector) < self.max_trial_entries)):
                solution_vector.append(1)
            else:
                solution_vector = increase_number_if_possible(sol_vec=solution_vector)
            if solution := self.check_for_solution(solution_vector=solution_vector):
                if len(solution_vector) == self.max_trial_entries:
                    self.solution = solution
                    return True
                else:
                    if self.backtracking(step=step + 1, solution_vector=solution_vector):
                        return True
                    else:
                        solution_vector.pop(-1)

    def check_for_solution(self, solution_vector: List) -> Optional[sudokuboard.SudokuBoard]:
        board = sudokuboard.insert_solution_vector_into_board(solution_vector=solution_vector, board=self.board)
        if self.constraints.check_sudoku(board=board):
            return board
        else:
            return None

