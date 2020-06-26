
from typing import Dict, List

import sudokuboard
import sudokucandidates
import sudokuconstraints
import sudokuutils


class HiddenSingles:

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
            candidates_statistic = {j: {'nr_entries': 0, 'loc_entries': []} for j in range(1, 10)}
            unit = self.candidates.get_unit(unit=self.unit, num=unit_nr)
            for cell_nr, cell in enumerate(unit):
                if cell:
                    for entry in cell:
                        candidates_statistic[entry]['nr_entries'] = candidates_statistic[entry]['nr_entries'] + 1
                        pos_row, pos_column = sudokuutils.get_pos_from_unit_nr(unit=self.unit,
                                                                               unit_nr=unit_nr,
                                                                               cell_nr=cell_nr)
                        candidates_statistic[entry]['loc_entries'].append((pos_row, pos_column))
            for number, sub_dict in candidates_statistic.items():
                if sub_dict['nr_entries'] == 1:
                    print('Hidden Single {num} found in {unit_name} {unit_nr}'.format(num=number, unit_name=self.unit,
                                                                                      unit_nr=unit_nr))
                    found.append({number: sub_dict['loc_entries'][0]})
        return found
