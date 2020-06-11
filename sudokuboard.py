
from typing import Iterable, List, Set, Tuple

import sudokuutils


class SudokuBoard:

    def __init__(self, constraints: List[str] = None):
        self.board = self._init_board()

    def _init_board(self) -> List[List[int]]:
        row = [0 for _ in range(0, 9)]
        board = [row.copy() for _ in range(0, 9)]
        return board

    def get_number_of_empty_cells(self) -> int:
        empty_cells = 0
        for index_row in range(0, 9):
            for index_column in range(0, 9):
                if self.board[index_row][index_column] == 0:
                    empty_cells = empty_cells + 1
        return empty_cells

    def is_complete(self) -> bool:
        if self.get_number_of_empty_cells() == 0:
            return True
        return False

    def enter_number(self, pos_row: int, pos_column: int, number: int):
        self.board[pos_row][pos_column] = number

    def _get_row(self, pos_row: int) -> List[int]:
        return self.board[pos_row]

    def _get_column(self, pos_column: int) -> List[int]:
        return [self.board[row][pos_column] for row in range(0, 9)]

    def _get_box(self, box_num: int) -> List[int]:
        (start_row, end_row), (start_column, end_column) = sudokuutils.get_box_dimensions(box_num=box_num)
        box = []
        for row_index in range(start_row, end_row+1):
            for column_index in range(start_column, end_column+1):
                box.append(self.board[row_index][column_index])
        return box

    def _get_box2(self, pos_row: int, pos_column: int) -> List[int]:
        (start_row, end_row), (start_column, end_column) = sudokuutils.get_box_dimensions2(pos_row=pos_row,
                                                                                           pos_column=pos_column)
        box = []
        for row_index in range(start_row, end_row+1):
            for column_index in range(start_column, end_column+1):
                box.append(self.board[row_index][column_index])
        return box

    def get_unit(self, unit: str, num: int) -> List[int]:
        if unit == 'row':
            return self._get_row(pos_row=num)
        if unit == 'column':
            return self._get_column(pos_column=num)
        if unit == 'box':
            return self._get_box(box_num=num)

    def get_row_entries(self, pos_row) -> Set[int]:
        return {entry for entry in self.board[pos_row] if entry != 0}

    def get_column_entries(self, pos_column) -> Set[int]:
        return {self.board[row][pos_column] for row in range(0, 9) if self.board[row][pos_column] != 0}

    def get_box_entries(self, pos_row: int, pos_column: int) -> Set[int]:
        (start_row, end_row), (start_column, end_column) = sudokuutils.get_box_dimensions2(pos_row=pos_row,
                                                                                           pos_column=pos_column)
        entries = set()
        for row_index in range(start_row, end_row):
            for column_index in range(start_column, end_column):
                if self.board[row_index][column_index] != 0:
                    entries.add(self.board[row_index][column_index])
        return entries

    def read_sudoku(self, file: str):
        with open(file, 'r') as file_sudoku:
            for row_index, line in enumerate(file_sudoku):
                line = line.rstrip()
                entries = line.split(',')
                for column_index, entry in enumerate(entries):
                    self.enter_number(pos_row=row_index, pos_column=column_index, number=int(entry))

    def write_sudoku(self, file: str):
        with open(file, 'w+') as file_sudoku:
            for row_index in range(0, 9):
                file_sudoku.writelines(f"{','.join(str(number) for number in self.board[row_index])}\n")

    def print_sudoku(self):
        for row_index in range(0, 9):
            print(self.board[row_index])