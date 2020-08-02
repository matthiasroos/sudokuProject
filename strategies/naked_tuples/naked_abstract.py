
import abc
import itertools
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

    def evaluate_analysis_dict_for_higher_tuples(self, analysis_dict: Dict, unit_nr: int, tuple_size: int) -> List:
        found = []
        analysis_list = self.make_keys_to_list(analysis_dict=analysis_dict)
        if (size := len(analysis_list)) >= tuple_size:
            # create all possible combinations of numbers
            combinations = itertools.combinations(range(size), tuple_size)
            for combination in list(combinations):
                possible_tuple = set()
                for nr in combination:
                    for item in analysis_list[nr]:
                        possible_tuple.add(item)
                if len(possible_tuple) == tuple_size:
                    triple: Tuple[int] = tuple(number for number in sorted(list(possible_tuple)))
                    self.print_found_strategy(numbers=triple, unit_nr=unit_nr)

                    found_entry = {analysis_list[nr]: analysis_dict[analysis_list[nr]] for nr in combination}
                    found.append(found_entry)

        return found
