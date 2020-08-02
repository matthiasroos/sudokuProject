
from typing import Dict, List, Set

import strategies.naked_tuples.naked_abstract


class NakedPairs(strategies.naked_tuples.naked_abstract.NakedAbstract):

    def __init__(self, sudoku, candidates, constraints, unit):
        super().__init__(sudoku=sudoku, candidates=candidates, constraints=constraints, unit=unit)
        self._strategy_name = 'Naked Pair'

    def check_cell_length(self, cell: List) -> bool:
        if len(cell) == 2:
            return True
        return False

    def evaluate_analysis_dict(self, analysis_dict: Dict, unit_nr: int) -> List:
        found = []
        for pair, locs in analysis_dict.items():
            if len(locs) == 2:
                self.print_found_strategy(numbers=pair, unit_nr=unit_nr)
                found.append({pair: locs})
        return found
