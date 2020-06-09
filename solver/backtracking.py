
import copy
import dataclasses
from typing import List, Optional, Tuple

import sudokuboard


class BackTracking:
    @dataclasses.dataclass()
    class Trials:
        number = None
        row = None
        column = None

    def __init__(self, board: sudokuboard.SudokuBoard):
        self.board = board
        self.max_trial_entries = self.board.get_number_of_empty_cells()

    def run(self):
        trials = []
        status = self._find_solution()


    def backtracking(self, candidate):
        if self._reject(...):
            return False
        if self._accept(...):
            self._output(...)
        start = self._first(...)
        while start:
            self.backtracking(candidate=start)
            start = self.next(...)

    def _root(self, instance):
        pass

    def _reject(self, instance, candidate):
        pass

    def _accept(self, instance, candidate):
        pass

    def _first(self, instance, candidate):
        pass

    def _next(self, instance, candidate):
        pass

    def _output(self, instance, candidate):
        pass

    def _find_solution(self, level: int, trials: Trials):
        pass

    def _get_next_empty_cell(self) -> Optional[Trials]:
        if self.trials:
            reached_row = self.trials[-1].row
            reached_column = self.trials[-1].column
        else:
            reached_row = 0
            reached_column = 0
        new_trial = self.Trials()
        for index_row in range(reached_row, 9):
            for index_column in range(reached_column, 9):
                if self.board.board[index_row][index_column] == 0:
                    new_trial.row = index_row
                    new_trial.column = index_column
                    return new_trial
        return None

    def insert_trials_in_board(self, trials: List[Trials], board: sudokuboard.SudokuBoard) -> sudokuboard.SudokuBoard:
        board_new = copy.deepcopy(board)
        for trial in trials:
            board_new.enter_number(pos_row=trial.row, pos_column=trial.column, number=trial.column)
        return board_new



