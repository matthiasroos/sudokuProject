from typing import Dict, List

import sudokuboard
import sudokucandidates
import sudokuconstraints

modules = {'naked_singles': {'folder': 'naked_tuples',
                             'module': 'naked_singles',
                             'class': 'NakedSingles'},
           'hidden_singles': {'folder': 'hidden_tuples',
                              'module': 'hidden_singles',
                              'class': 'HiddenSingles'},
           'naked_pairs': {'folder': 'naked_tuples',
                           'module': 'naked_pairs',
                           'class': 'NakedPairs'},
           'hidden_pairs': {'folder': 'hidden_tuples',
                            'module': 'hidden_pairs',
                            'class': 'HiddenPairs'},
           'naked_triples': {'folder': 'naked_tuples',
                             'module': 'naked_triples',
                             'class': 'NakedTriples'},
           'hidden_triples': {'folder': 'hidden_tuples',
                              'module': 'hidden_triples',
                              'class': 'HiddenTriples'},
           'naked_quartets': {'folder': 'naked_tuples',
                              'module': 'naked_quartets',
                              'class': 'NakedQuartet'}
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
        self.module_name = f"strategies.{modules[strategy]['folder']}.{modules[strategy]['module']}"
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
