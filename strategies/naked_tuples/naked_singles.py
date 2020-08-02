
from typing import Dict, List

import strategies.naked_tuples.naked_abstract
import sudokuutils


class NakedSingles(strategies.naked_tuples.naked_abstract.NakedAbstract):

    def __init__(self, sudoku, candidates, constraints, unit):
        super().__init__(sudoku=sudoku, candidates=candidates, constraints=constraints, unit=unit)
        self._strategy_name = 'Naked Single'

    def check_cell_length(self, cell: List) -> bool:
        if len(cell) == 1:
            return True
        return False

    def evaluate_analysis_dict(self, analysis_dict: Dict, unit_nr: int) -> List:
        found = []
        for number, loc in analysis_dict.items():
            number = number[0]
            self.print_found_strategy(numbers=number, unit_nr=unit_nr)
            found.append({number: loc})
        return found
