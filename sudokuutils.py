
from typing import Iterable, List, Optional, Set, Tuple


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


def get_pos_from_unit_nr(unit: str, unit_nr: int, cell_nr: int) -> Tuple[Optional[int], Optional[int]]:
    """
    Return the position depending on the unit
    :param unit: type of unit 'row', 'column', 'box'
    :param unit_nr: first iterator (over the units)
    :param cell_nr: second iterator (over the cells in one unit)
    :return: tuple of pos_row and pos_column
    """
    if unit == 'row':
        return unit_nr, cell_nr
    if unit == 'column':
        return cell_nr, unit_nr
    if unit == 'box':
        pos_row = (unit_nr // 3) * 3 + cell_nr // 3
        pos_column = (unit_nr % 3) * 3 + cell_nr % 3
        return pos_row, pos_column
    return None, None
