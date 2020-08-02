
import itertools
from typing import Dict, List, Tuple

import strategies.naked_tuples.naked_abstract
import sudokuutils


class NakedQuartet(strategies.naked_tuples.naked_abstract.NakedAbstract):

    def __init__(self, sudoku, candidates, constraints, unit):
        super().__init__(sudoku=sudoku, candidates=candidates, constraints=constraints, unit=unit)
        self._strategy_name = 'Naked Quartet'

    def check_cell_length(self, cell: List) -> bool:
        if (len(cell) == 2) or (len(cell) == 3) or (len(cell) == 4):
            return True
        return False

    def evaluate_analysis_dict(self, analysis_dict: Dict, unit_nr: int) -> List:
        """
        Find naked quartet, also the obvious ones.

        :param analysis_dict:
        :param unit_nr:
        :return:
        """
        found = []
        analysis_list = self.make_keys_to_list(analysis_dict=analysis_dict)
        if (size := len(analysis_list)) >= 4:
            # create all possible combinations of numbers
            combinations = itertools.combinations(range(size), 4)
            for combination in list(combinations):
                possible_quartet = set()
                for nr in combination:
                    for item in analysis_list[nr]:
                        possible_quartet.add(item)
                if len(possible_quartet) == 4:
                    triple: Tuple[int] = tuple(number for number in sorted(list(possible_quartet)))
                    self.print_found_strategy(numbers=triple, unit_nr=unit_nr)

                    found_entry = {analysis_list[nr]: analysis_dict[analysis_list[nr]] for nr in combination}
                    found.append(found_entry)

        return found
