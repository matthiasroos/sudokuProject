
from typing import List, Optional

import sudokuutils


class SudokuAbstract:

    def __init__(self):
        self._abstract = None

    @staticmethod
    def _init_abstract(element) -> List[List]:
        row = [element for _ in range(0, 9)]
        abstract = [row.copy() for _ in range(0, 9)]
        return abstract

    def _get_row(self, pos_row: int) -> List:
        return self._abstract[pos_row]

    def _get_column(self, pos_column: int) -> List:
        return [self._abstract[row][pos_column] for row in range(0, 9)]

    def _get_box(self, box_num: int) -> List:
        (start_row, end_row), (start_column, end_column) = sudokuutils.get_box_dimensions(box_num=box_num)
        box = []
        for row_index in range(start_row, end_row + 1):
            for column_index in range(start_column, end_column + 1):
                box.append(self._abstract[row_index][column_index])
        return box

    def _get_box2(self, pos_row: int, pos_column: int) -> List:
        (start_row, end_row), (start_column, end_column) = sudokuutils.get_box_dimensions2(pos_row=pos_row,
                                                                                           pos_column=pos_column)
        box = []
        for row_index in range(start_row, end_row+1):
            for column_index in range(start_column, end_column+1):
                box.append(self._abstract[row_index][column_index])
        return box

    def get_unit(self, unit: str, num: int) -> Optional[List]:
        if unit == 'row':
            return self._get_row(pos_row=num)
        if unit == 'column':
            return self._get_column(pos_column=num)
        if unit == 'box':
            return self._get_box(box_num=num)
        return None
