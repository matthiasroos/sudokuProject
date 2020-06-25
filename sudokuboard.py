
import copy
from typing import Iterable, List, Set, Tuple

import sudokuabstract
import sudokuutils


class SudokuBoard(sudokuabstract.SudokuAbstract):

    def __init__(self, constraints: List[str] = None):
        super().__init__()
        self._abstract = self._init_board()

    def _init_board(self) -> List[List[int]]:
        board = self._init_abstract(element=0)
        return board

    @property
    def board(self) -> List[List[int]]:
        return self._abstract

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


def insert_solution_vector_into_board(solution_vector: List, board: SudokuBoard):
    board_new = copy.deepcopy(board)
    generator_vector = (entry for entry in solution_vector)
    for index_row in range(0, 9):
        for index_column in range(0, 9):
            if board_new.board[index_row][index_column] == 0:
                try:
                    next_number = next(generator_vector)
                    board_new.enter_number(pos_row=index_row, pos_column=index_column, number=next_number)
                except StopIteration:
                    return board_new
    return board_new
