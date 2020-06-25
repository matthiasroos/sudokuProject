
import sudokuboard
import sudokucandidates
import sudokuconstraints


class NakedSingles:

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
            box = self.candidates.get_unit(unit=self.unit, num=i)
            for cell in box:
                if len(cell) == 1:
                    print('Naked Single found in {unit_name} {unit_nr}'.format(unit_name=self.unit, unit_nr=i))
