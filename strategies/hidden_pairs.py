
from typing import Dict, List

import strategies.abstractstrategy
import sudokuutils


class HiddenPairs(strategies.abstractstrategy.AbstractStrategy):

    def __init__(self, sudoku, candidates, constraints, unit):
        super().__init__(sudoku=sudoku, candidates=candidates, constraints=constraints, unit=unit)

    def detect(self) -> List[Dict]:
        found = []
        for unit_nr in range(0, 9):
            candidate_statistics = {}
            unit = self.candidates.get_unit(unit=self.unit, num=unit_nr)
            for cell_nr, cell in enumerate(unit):
                if cell:
                    for nr in list(cell):
                        if candidate_statistics.get(nr):
                            candidate_statistics[nr].append(cell_nr)
                        else:
                            candidate_statistics[nr] = [cell_nr]
            for nr_1, loc_list_1 in candidate_statistics.items():
                if len(loc_list_1) != 2:
                    continue
                for nr_2, loc_list_2 in candidate_statistics.items():
                    if nr_1 != nr_2:
                        if loc_list_1 == loc_list_2:
                            pair = (nr_1, nr_2)
                            print('Hidden pair {pair} found in {unit_name} {unit_nr}'.format(pair=pair,
                                                                                             unit_name=self.unit,
                                                                                             unit_nr=unit_nr))
                            loc1 = sudokuutils.get_pos_from_unit_nr(unit=self.unit,
                                                                    unit_nr=unit_nr,
                                                                    cell_nr=loc_list_1[0])
                            loc2 = sudokuutils.get_pos_from_unit_nr(unit=self.unit,
                                                                    unit_nr=unit_nr,
                                                                    cell_nr=loc_list_1[1])
                            found.append({pair: [loc1, loc2]})
        return found

