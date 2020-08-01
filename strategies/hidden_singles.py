
from typing import Dict, List, Optional

import strategies.hidden_abstract
import sudokuutils


class HiddenSingles(strategies.hidden_abstract.HiddenAbstract):

    def __init__(self, sudoku, candidates, constraints, unit):
        super().__init__(sudoku=sudoku, candidates=candidates, constraints=constraints, unit=unit)
        self._strategy_name = 'Hidden Single'

    def evaluate_analysis_dict(self, analysis_dict: Dict, unit_nr: int) -> Optional[List]:
        found = []
        for number, loc_list in analysis_dict.items():
            if len(loc_list) == 1:
                self.print_found_strategy(numbers=number, unit_nr=unit_nr)
                loc = sudokuutils.get_pos_from_unit_nr(unit=self.unit,
                                                       unit_nr=unit_nr,
                                                       cell_nr=loc_list[0])
                found.append({number: loc})
        return found
