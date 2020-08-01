
from typing import Dict, List, Set

import strategies.abstractstrategy
import sudokuutils


class HiddenPairs(strategies.abstractstrategy.AbstractStrategy):

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
        self._strategy_name = 'Hidden Pair'

    def evaluate_analysis_dict(self, analysis_dict: Dict, unit_nr: int) -> List:
        found = []
        for nr_1, loc_list_1 in analysis_dict.items():
            if len(loc_list_1) != 2:
                continue
            for nr_2, loc_list_2 in analysis_dict.items():
                if nr_1 < nr_2:
                    if loc_list_1 == loc_list_2:
                        pair = (nr_1, nr_2)
                        self.print_found_strategy(numbers=pair, unit_nr=unit_nr)
                        loc1 = sudokuutils.get_pos_from_unit_nr(unit=self.unit,
                                                                unit_nr=unit_nr,
                                                                cell_nr=loc_list_1[0])
                        loc2 = sudokuutils.get_pos_from_unit_nr(unit=self.unit,
                                                                unit_nr=unit_nr,
                                                                cell_nr=loc_list_1[1])
                        locs = sorted([loc1, loc2])
                        found.append({pair: locs})
        return found
