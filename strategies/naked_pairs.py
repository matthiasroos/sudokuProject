
from typing import Dict, List, Set

import strategies.abstractstrategy
import sudokuutils


class NakedPairs(strategies.abstractstrategy.AbstractStrategy):

    def __init__(self, sudoku, candidates, constraints, unit):
        super().__init__(sudoku=sudoku, candidates=candidates, constraints=constraints, unit=unit)

    def analyze_candidates(self, unit_nr: int, cell_nr: int, cell: List, analysis_dict: Dict) -> Dict:
        if len(cell) == 2:
            pair = tuple(nr for nr in cell)
            pos_row, pos_column = sudokuutils.get_pos_from_unit_nr(unit=self.unit,
                                                                   unit_nr=unit_nr,
                                                                   cell_nr=cell_nr)
            if analysis_dict.get(pair):
                analysis_dict[pair].append((pos_row, pos_column))
            else:
                analysis_dict[pair] = [(pos_row, pos_column)]
        return analysis_dict

    def evaluate_analysis_dict(self, analysis_dict: Dict, unit_nr: int) -> List:
        found = []
        for pair, locs in analysis_dict.items():
            if len(locs) == 2:
                print('Naked Pair {pair} found in {unit_name} {unit_nr}'.format(pair=pair, unit_name=self.unit,
                                                                                unit_nr=unit_nr))
                found.append({pair: locs})
        return found
