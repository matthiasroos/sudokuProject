
from typing import Dict, List

import strategies.abstractstrategy
import sudokuutils


class NakedPairs(strategies.abstractstrategy.AbstractStrategy):

    def __init__(self, sudoku, candidates, constraints, unit):
        super().__init__(sudoku=sudoku, candidates=candidates, constraints=constraints, unit=unit)

    def detect(self) -> List[Dict]:
        found = []
        for unit_nr in range(0, 9):
            candidate_pairs = {}
            unit = self.candidates.get_unit(unit=self.unit, num=unit_nr)
            for cell_nr, cell in enumerate(unit):
                if cell:
                    if len(cell) == 2:
                        pair = tuple(nr for nr in list(cell))
                        pos_row, pos_column = sudokuutils.get_pos_from_unit_nr(unit=self.unit,
                                                                               unit_nr=unit_nr,
                                                                               cell_nr=cell_nr)
                        if candidate_pairs.get(pair):
                            candidate_pairs[pair].append((pos_row, pos_column))
                        else:
                            candidate_pairs[pair] = [(pos_row, pos_column)]
            for pair, locs in candidate_pairs.items():
                if len(locs) == 2:
                    print('Naked Pair {pair} found in {unit_name} {unit_nr}'.format(pair=pair, unit_name=self.unit,
                                                                                    unit_nr=unit_nr))
                    found.append({pair: locs})
        return found



