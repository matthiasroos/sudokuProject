
import abc
from typing import Dict, List, Tuple

import strategies.abstractstrategy
import sudokuutils


class NakedAbstract(strategies.abstractstrategy.AbstractStrategy):
    def __init__(self, sudoku, candidates, constraints, unit):
        super().__init__(sudoku=sudoku, candidates=candidates, constraints=constraints, unit=unit)

    def analyze_candidates(self, unit_nr: int, cell_nr: int, cell: List, analysis_dict: Dict) -> Dict:
        if self.check_cell_length(cell=cell):
            tuple_ = tuple(nr for nr in cell)
            pos_row, pos_column = sudokuutils.get_pos_from_unit_nr(unit=self.unit,
                                                                   unit_nr=unit_nr,
                                                                   cell_nr=cell_nr)
            if analysis_dict.get(tuple_):
                analysis_dict[tuple_].append((pos_row, pos_column))
            else:
                analysis_dict[tuple_] = [(pos_row, pos_column)]

        return analysis_dict

    @abc.abstractmethod
    def check_cell_length(self, cell: List) -> bool:
        pass
