
from typing import Iterable, List, Set, Tuple


def invert_entries(input_: Iterable[int]):
    return {number for number in range(1, 10) if number not in input_}


def get_box_number_for_pos(pos_row: int, pos_column: int) -> int:
    return pos_column // 3 + (pos_row // 3) * 3


def get_box_dimensions(box_num: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    start_row = box_num // 3 * 3
    end_row = start_row + 2
    start_column = box_num % 3 * 3
    end_column = start_column + 2
    return (start_row, end_row), (start_column, end_column)


def get_box_dimensions2(pos_row: int, pos_column: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    start_row = pos_row - pos_row % 3
    end_row = start_row + 3
    start_column = pos_column - pos_column % 3
    end_column = start_column + 3
    return (start_row, end_row), (start_column, end_column)