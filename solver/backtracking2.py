
import copy
import dataclasses
from typing import List, Optional, Tuple

import sudokuboard
import sudokuconstraints
import solver.backtracking


class BackTracking2:

    def __init__(self, board: sudokuboard.SudokuBoard):
        self.board = board
        self.solution = None
        self.constraints = sudokuconstraints.SudokuConstraints()
        self.max_trial_entries = self.board.get_number_of_empty_cells()

    def run(self):
        solution_vector = []
        status = self.backtracking(step=0, solution_vector=solution_vector)
        if status:
            self.solution.print_sudoku()

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
            # Add 1 at the beginning and for each new step
            if (not solution_vector) or \
                    ((step > (len(solution_vector) - 1)) and (len(solution_vector) < self.max_trial_entries)):
                solution_vector.append(1)
            else:
                solution_vector = increase_number_if_possible(sol_vec=solution_vector)
            if self.check_solution(solution_vector=solution_vector):
                if len(solution_vector) == self.max_trial_entries:
                    self.solution = solver.backtracking.BackTracking(board=self.board).\
                        insert_solution_vector_into_board(solution_vector=solution_vector)
                    return True
                else:
                    if self.backtracking(step=step + 1, solution_vector=solution_vector):
                        return True
                    else:
                        solution_vector.pop(-1)

    def check_solution(self, solution_vector: List) -> bool:
        board = solver.backtracking.BackTracking(board=self.board).insert_solution_vector_into_board(solution_vector=solution_vector)
        return self.constraints.check_sudoku(board=board)
