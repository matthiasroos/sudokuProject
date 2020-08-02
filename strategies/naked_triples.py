
import itertools
from typing import Dict, List, Tuple

import strategies.abstractstrategy
import sudokuutils


class NakedTriples(strategies.abstractstrategy.AbstractStrategy):

    def __init__(self, sudoku, candidates, constraints, unit):
        super().__init__(sudoku=sudoku, candidates=candidates, constraints=constraints, unit=unit)
        self._strategy_name = 'Naked Triple'

    def analyze_candidates(self, unit_nr: int, cell_nr: int, cell: List, analysis_dict: Dict) -> Dict:
        if cell:
            if (len(cell) == 2) | (len(cell) == 3):
                tuple_ = tuple(nr for nr in cell)
                pos_row, pos_column = sudokuutils.get_pos_from_unit_nr(unit=self.unit,
                                                                       unit_nr=unit_nr,
                                                                       cell_nr=cell_nr)
                if analysis_dict.get(tuple_):
                    analysis_dict[tuple_].append((pos_row, pos_column))
                else:
                    analysis_dict[tuple_] = [(pos_row, pos_column)]
        return analysis_dict

    def evaluate_analysis_dict(self, analysis_dict: Dict, unit_nr: int) -> List:
        """
        Find naked triples, also the obvious ones.

        :param analysis_dict:
        :param unit_nr:
        :return:
        """
        found = []
        if (size := len(analysis_dict)) >= 3:
            analysis_list = list(analysis_dict.keys())
            # create all possible combinations of numbers
            combinations = itertools.combinations(range(size), 3)
            for combination in list(combinations):
                possible_triple = set()
                for nr in combination:
                    for item in analysis_list[nr]:
                        possible_triple.add(item)
                if len(possible_triple) == 3:
                    triple: Tuple[int] = tuple(number for number in sorted(list(possible_triple)))
                    self.print_found_strategy(numbers=triple, unit_nr=unit_nr)

                    found_entry = {analysis_list[nr]: analysis_dict[analysis_list[nr]] for nr in combination}
                    found.append([found_entry])

        return found
