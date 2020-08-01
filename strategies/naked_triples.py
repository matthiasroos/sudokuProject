
import itertools
from typing import Dict, List, Set

import strategies.abstractstrategy
import sudokuutils


class NakedTriples(strategies.abstractstrategy.AbstractStrategy):

    def __init__(self, sudoku, candidates, constraints, unit):
        super().__init__(sudoku=sudoku, candidates=candidates, constraints=constraints, unit=unit)

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
        result = []
        if (size := len(analysis_dict)) >= 3:
            analysis_list = list(analysis_dict.keys())
            combinations = itertools.combinations(range(size), 3)
            for combination in list(combinations):
                possible_triple_set = set()
                for nr in combination:
                    for item in analysis_list[nr]:
                        possible_triple_set.add(item)
                if len(possible_triple_set) == 3:
                    possible_triple = tuple(number for number in sorted(list(possible_triple_set)))
                    print('Naked triple {triple} found in {unit_name} {unit_nr}'.format(triple=possible_triple,
                                                                                        unit_name=self.unit,
                                                                                        unit_nr=unit_nr))

                    result_entry = [{analysis_list[nr]: analysis_dict[analysis_list[nr]]} for nr in combination]
                    result.append(result_entry)

        return result
