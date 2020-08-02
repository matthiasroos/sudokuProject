
from typing import Dict, List, Tuple

import strategies.naked_tuples.naked_abstract


class NakedQuadruples(strategies.naked_tuples.naked_abstract.NakedAbstract):

    def __init__(self, sudoku, candidates, constraints, unit):
        super().__init__(sudoku=sudoku, candidates=candidates, constraints=constraints, unit=unit)
        self._strategy_name = 'Naked Quadruple'

    def check_cell_length(self, cell: List) -> bool:
        if (len(cell) == 2) or (len(cell) == 3) or (len(cell) == 4):
            return True
        return False

    def evaluate_analysis_dict(self, analysis_dict: Dict, unit_nr: int) -> List:
        """
        Find naked quadruples, also the obvious ones.

        :param analysis_dict:
        :param unit_nr:
        :return:
        """
        found = self.evaluate_analysis_dict_for_higher_tuples(analysis_dict=analysis_dict,
                                                              unit_nr=unit_nr,
                                                              tuple_size=4)

        return found
