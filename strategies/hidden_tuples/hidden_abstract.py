
from typing import Dict, List, Optional

import strategies.abstractstrategy


class HiddenAbstract(strategies.abstractstrategy.AbstractStrategy):

    def __init__(self, sudoku, candidates, constraints, unit):
        super().__init__(sudoku=sudoku, candidates=candidates, constraints=constraints, unit=unit)

    def analyze_candidates(self, unit_nr: int, cell_nr: int, cell: List, analysis_dict: Dict) -> Dict:
        if cell:
            for number in cell:
                if analysis_dict.get(number):
                    analysis_dict[number].append(cell_nr)
                else:
                    analysis_dict[number] = [cell_nr]
        return analysis_dict

    def evaluate_analysis_dict(self, analysis_dict: Dict, unit_nr: int) -> List:
        pass
