
from typing import List

import sudokuboard


class SudokuConstraints:

    def __init__(self, constraints: str = 'standard'):
        self._constraints = self._init_constraints(constraints=constraints)

    @staticmethod
    def _init_constraints(constraints: str) -> List:
        if constraints == 'standard':
            return ['row', 'column', 'box']
        return []

    def check_sudoku(self, board: sudokuboard.SudokuBoard) -> bool:
        def check_unit(unit: List) -> bool:
            unit = [entry for entry in unit if entry > 0]
            if len(unit) > len(set(unit)):
                return False
            return True
        for constraint in self._constraints:
            for i in range(0, 9):
                ac_unit = board.get_unit(unit=constraint, num=i)
                if not ac_unit:
                    return False
                result = check_unit(unit=ac_unit)
                if not result:
                    return False
        return True
