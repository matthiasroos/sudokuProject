
import itertools
from typing import Dict, List, Tuple

import strategies.hidden_tuples.hidden_abstract
import sudokuutils


class HiddenTriples(strategies.hidden_tuples.hidden_abstract.HiddenAbstract):

    def __init__(self, sudoku, candidates, constraints, unit):
        super().__init__(sudoku=sudoku, candidates=candidates, constraints=constraints, unit=unit)
        self._strategy_name = 'Hidden Triple'

    def evaluate_analysis_dict(self, analysis_dict: Dict, unit_nr: int) -> List:
        found = []
        triple_candidates = {}
        for nr, loc in analysis_dict.items():
            if len(loc) == 2 or len(loc) == 3:
                triple_candidates[nr] = loc
        combinations = itertools.combinations(triple_candidates.keys(), 3)
        for combination in list(combinations):
            possible_triple = set()
            for nr in combination:
                if triple_candidates.get(nr):
                    possible_triple.add(nr)
            if len(possible_triple) == 3:
                pos = set()
                for pos_entry in possible_triple:
                    for nr in analysis_dict[pos_entry]:
                        pos.add(nr)
                if len(pos) == 3:
                    triple: Tuple[int] = tuple(number for number in sorted(list(possible_triple)))
                    self.print_found_strategy(numbers=triple, unit_nr=unit_nr)

                    #
                    found_entry = {}
                    for pos_entry in sorted(list(pos)):
                        list_of_tuple_on_pos = []
                        for nr in triple:
                            if pos_entry in analysis_dict[nr]:
                                list_of_tuple_on_pos.append(nr)
                        tuple_on_pos = tuple(number for number in sorted(list(list_of_tuple_on_pos)))
                        loc = sudokuutils.get_pos_from_unit_nr(unit=self.unit,
                                                               unit_nr=unit_nr,
                                                               cell_nr=pos_entry)
                        if found_entry.get(tuple_on_pos):
                            found_entry[tuple_on_pos].append(loc)
                        else:
                            found_entry[tuple_on_pos] = [loc]

                    found.append([found_entry])

        return found
