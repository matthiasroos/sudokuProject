
from typing import Dict, List, Optional

import strategies.abstractstrategy
import sudokuutils


class HiddenSingles(strategies.abstractstrategy.AbstractStrategy):

    def __init__(self, sudoku, candidates, constraints, unit):
        super().__init__(sudoku=sudoku, candidates=candidates, constraints=constraints, unit=unit)

    @staticmethod
    def initialize_analysis_dict() -> Dict:
        return {j: {'nr_entries': 0, 'loc_entries': []} for j in range(1, 10)}

    def analyze_candidates(self, unit_nr: int, cell_nr: int, cell: List, analysis_dict: Dict) -> Dict:
        if cell:
            for entry in cell:
                analysis_dict[entry]['nr_entries'] = analysis_dict[entry]['nr_entries'] + 1
                pos_row, pos_column = sudokuutils.get_pos_from_unit_nr(unit=self.unit,
                                                                       unit_nr=unit_nr,
                                                                       cell_nr=cell_nr)
                analysis_dict[entry]['loc_entries'].append((pos_row, pos_column))
        return analysis_dict
        self._strategy_name = 'Hidden Single'

    def evaluate_analysis_dict(self, analysis_dict: Dict, unit_nr: int) -> Optional[List]:
        found = []
        for number, sub_dict in analysis_dict.items():
            if sub_dict['nr_entries'] == 1:
                found.append({number: sub_dict['loc_entries'][0]})
                self.print_found_strategy(numbers=number, unit_nr=unit_nr)
        return found
