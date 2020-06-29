
import abc
from typing import Dict, List

import sudokuboard
import sudokucandidates
import sudokuconstraints


class AbstractStrategy(metaclass=abc.ABCMeta):

    def __init__(self,
                 sudoku: sudokuboard.SudokuBoard,
                 candidates: sudokucandidates.SudokuCandidates,
                 constraints: sudokuconstraints.SudokuConstraints,
                 unit: str):

        self.board = sudoku
        self.candidates = candidates
        self.constraints = constraints
        self.unit = unit

    @abc.abstractmethod
    def detect(self) -> List[Dict]:
        pass
