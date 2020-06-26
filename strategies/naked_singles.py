
from typing import Dict, List

import sudokuboard
import sudokucandidates
import sudokuconstraints
import sudokuutils


class NakedSingles:

    def __init__(self,
                 sudoku: sudokuboard.SudokuBoard,
                 candidates: sudokucandidates.SudokuCandidates,
                 constraints: sudokuconstraints.SudokuConstraints,
                 unit: str):

        self.board = sudoku
        self.candidates = candidates
        self.constraints = constraints
        self.unit = unit

    def detect(self) -> List[Dict]:
        found = []
        for unit_nr in range(0, 9):
            unit = self.candidates.get_unit(unit=self.unit, num=unit_nr)
            for cell_nr, cell in enumerate(unit):
                if len(cell) == 1:
                    num = next(iter(cell))
                    print('Naked Single {num} found in {unit_name} {unit_nr}'.format(num=num,
                                                                                     unit_name=self.unit,
                                                                                     unit_nr=unit_nr))
                    pos_row, pos_column = sudokuutils.get_pos_from_unit_nr(unit=self.unit,
                                                                           unit_nr=unit_nr,
                                                                           cell_nr=cell_nr)
                    found.append({num: (pos_row, pos_column)})
        return found
