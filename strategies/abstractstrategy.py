
import abc
from typing import Dict, List, Set

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

    def detect(self) -> List[Dict]:
        """
        Detects a strategy

        :return: list of found locations of strategy
        """
        found = []
        for unit_nr in range(0, 9):
            analysis_dict = self.initialize_analysis_dict()
            unit = self.candidates.get_unit(unit=self.unit, num=unit_nr)
            if unit:
                for cell_nr, cell in enumerate(unit):
                    analysis_dict = self.analyze_candidates(unit_nr=unit_nr,
                                                            cell_nr=cell_nr,
                                                            cell=cell,
                                                            analysis_dict=analysis_dict)

                new_found = self.evaluate_analysis_dict(analysis_dict=analysis_dict, unit_nr=unit_nr)
                if new_found:
                    found.extend(new_found)
        return found

    @staticmethod
    def initialize_analysis_dict() -> Dict:
        return {}

    @abc.abstractmethod
    def analyze_candidates(self, unit_nr: int, cell_nr: int, cell: Set, analysis_dict: Dict) -> Dict:
        """
        Analyze the candidate entries for one cell and write findings to analysis dict

        :param unit_nr:  number of the current unit
        :param cell_nr: number of the current cell in the unit
        :param cell: set of candidates for the current cell
        :param analysis_dict: analysis dict
        :return: analysis dict with additional entries
        """

    @abc.abstractmethod
    def evaluate_analysis_dict(self, analysis_dict: Dict, unit_nr: int) -> List:
        pass
