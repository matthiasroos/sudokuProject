
from typing import Iterable, List, Set, Tuple

import sudokuabstract
import sudokuboard
import sudokuutils


class SudokuCandidates(sudokuabstract.SudokuAbstract):

    def __init__(self, sudoku: sudokuboard.SudokuBoard):
        super().__init__()
        self._abstract = self._init_candidates()
        self._find_candidates(sudoku=sudoku)

    def _init_candidates(self) -> List[List[Set[int]]]:
        candidates = self._init_abstract(element=set())
        return candidates

    @property
    def candidates(self) -> List[List[Set]]:
        return self._abstract

    def set_candidates(self, pos_row: int, pos_column: int, candidates: Set[int]):
        self.candidates[pos_row][pos_column] = candidates

    def _update_candidates_row(self, pos_row, delete_num: int):
        for candidate_set in self.candidates[pos_row]:
            candidate_set.discard(delete_num)

    def _update_candidates_column(self, pos_column, delete_num: int):
        for index in range(0, 9):
            self.candidates[index][pos_column].discard(delete_num)

    def _update_candidates_box(self, pos_row: int, pos_column: int, delete_num: int):
        (start_row, end_row), (start_column, end_column) = sudokuutils.get_box_dimensions2(pos_row=pos_row,
                                                                                           pos_column=pos_column)
        for row_index in range(start_row, end_row):
            for column_index in range(start_column, end_column):
                self.candidates[row_index][column_index].discard(delete_num)

    def update_candidates(self, pos_row: int, pos_column: int, delete_num: int):
        self._update_candidates_row(pos_row=pos_row, delete_num=delete_num)
        self._update_candidates_column(pos_column=pos_column, delete_num=delete_num)
        self._update_candidates_box(pos_row=pos_row, pos_column=pos_column, delete_num=delete_num)

    def _find_candidates(self, sudoku: sudokuboard.SudokuBoard):
        for index_row, row_list in enumerate(sudoku.board):
            for index_column, number in enumerate(row_list):
                if number == 0:
                    entries = set()
                    entries.update(sudoku.get_row_entries(pos_row=index_row))
                    entries.update(sudoku.get_column_entries(pos_column=index_column))
                    entries.update(sudoku.get_box_entries(pos_row=index_row, pos_column=index_column))
                    candidates = sudokuutils.invert_entries(input_=entries)
                    self.set_candidates(pos_row=index_row, pos_column=index_column, candidates=candidates)
