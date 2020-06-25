
import sudokuboard
import sudokucandidates
import sudokuconstraints


class HiddenSingles:

    def __init__(self,
                 sudoku: sudokuboard.SudokuBoard,
                 candidates: sudokucandidates.SudokuCandidates,
                 constraints: sudokuconstraints.SudokuConstraints,
                 unit: str):

        self.board = sudoku
        self.candidates = candidates
        self.constraints = constraints
        self.unit = unit

    def detect(self):
        for i in range(0, 9):
            candidates_statistic = {i: 0 for i in range(1, 10)}
            box = self.candidates.get_unit(unit=self.unit, num=i)
            for cell in box:
                if cell:
                    for entry in cell:
                        candidates_statistic[entry] = candidates_statistic[entry] + 1
            for number, entry in candidates_statistic.items():
                if entry == 1:
                    print('Hidden Single {num} found in {unit_name} {unit_nr}'.format(num=number, unit_name=self.unit,
                                                                                      unit_nr=i))
