from typing import Dict, List

import sudokuboard
import sudokucandidates
import sudokuconstraints

modules = {'naked_singles': {'module': 'naked_singles',
                             'class': 'NakedSingles'},
           'hidden_singles': {'module': 'hidden_singles',
                              'class': 'HiddenSingles'},
           'naked_pairs': {'module': 'naked_pairs',
                           'class': 'NakedPairs'},
           'hidden_pairs': {'module': 'hidden_pairs',
                            'class': 'HiddenPairs'}
           }


class CollectionStrategy:

    def __init__(self,
                 sudoku: sudokuboard.SudokuBoard,
                 candidates: sudokucandidates.SudokuCandidates,
                 constraints: sudokuconstraints.SudokuConstraints,
                 strategy: str,
                 units: List[str]):
        self.sudoku = sudoku
        self.candidates = candidates
        self.constraints = constraints
        self.module_name = f"strategies.{modules[strategy]['module']}"
        self.class_name = modules[strategy]['class']
        self.units = units

    def detect(self) -> List[Dict]:
        module = __import__(self.module_name, fromlist=[self.module_name])
        class_ = getattr(module, self.class_name)
        found = []
        for unit in self.units:
            instance = class_(sudoku=self.sudoku, candidates=self.candidates, constraints=self.constraints, unit=unit)
            found_from_unit = instance.detect()
            found.append({unit: found_from_unit})
        return found


