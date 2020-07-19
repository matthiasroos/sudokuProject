
from typing import Dict, List

import strategies.abstractstrategy
import sudokuutils


class NakedSingles(strategies.abstractstrategy.AbstractStrategy):

    def __init__(self, sudoku, candidates, constraints, unit):
        super().__init__(sudoku=sudoku, candidates=candidates, constraints=constraints, unit=unit)

    def analyze_candidates(self, unit_nr: int, cell_nr: int, cell: List, analysis_dict: Dict) -> Dict:
        if len(cell) == 1:
            num = next(iter(cell))
            pos_row, pos_column = sudokuutils.get_pos_from_unit_nr(unit=self.unit,
                                                                   unit_nr=unit_nr,
                                                                   cell_nr=cell_nr)
            analysis_dict[num] = (pos_row, pos_column)
        return analysis_dict

    def evaluate_analysis_dict(self, analysis_dict: Dict, unit_nr: int) -> List:
        found = []
        for number, loc in analysis_dict.items():
            print('Naked Single {number} found in {unit_name} {unit_nr}'.format(number=number,
                                                                                unit_name=self.unit,
                                                                                unit_nr=unit_nr))
            found.append({number: loc})
        return found
