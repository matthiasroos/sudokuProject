
import pytest

import sudokuutils


@pytest.mark.parametrize(['input_', 'expected_set'],
                         [([1, 2, 3, 4], {5, 6, 7, 8, 9}), ({1}, {2, 3, 4, 5, 6, 7, 8, 9}),
                          ([], {1, 2, 3, 4, 5, 6, 7, 8, 9}), ((5, 6, 7), {1, 2, 3, 4, 8, 9})])
def test_invert_entries(input_, expected_set):
    output_set = sudokuutils.invert_entries(input_=input_)
    assert output_set == expected_set


@pytest.mark.parametrize(['pos_row', 'pos_column', 'expected'],
                         [(0, 1, 0), (1, 3, 1), (2, 6, 2), (1, 8, 2),
                          (3, 1, 3), (4, 4, 4), (5, 5, 4), (4, 8, 5),
                          (8, 0, 6), (7, 3, 7), (6, 6, 8), (8, 8, 8)])
def test_get_box_number_for_pos(pos_row, pos_column, expected):
    number = sudokuutils.get_box_number_for_pos(pos_row=pos_row, pos_column=pos_column)
    assert number == expected


@pytest.mark.parametrize(['box_num', 'expected_row', 'expected_column'],
                         [(0, (0, 2), (0, 2)), (1, (0, 2), (3, 5)), (2, (0, 2), (6, 8)),
                          (3, (3, 5), (0, 2)), (4, (3, 5), (3, 5)), (5, (3, 5), (6, 8)),
                          (6, (6, 8), (0, 2)), (7, (6, 8), (3, 5)), (8, (6, 8), (6, 8))])
def test_get_box_dimension(box_num, expected_row, expected_column):
    start_row, end_row = expected_row
    start_column, end_column = expected_column
    (out_start_row, out_end_row), (out_start_column, out_end_column) = sudokuutils.get_box_dimensions(box_num=box_num)
    assert out_start_row == start_row
    assert out_end_row == end_row
    assert out_start_column == start_column
    assert out_end_column == end_column
