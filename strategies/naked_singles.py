
import sudokuboard
import sudokucandidates
import sudokuconstraints


class NakedSingles:

    def __init__(self,
                 sudoku: sudokuboard.SudokuBoard,
                 candidates: sudokucandidates.SudokuCandidates,
                 constraints: sudokuconstraints.SudokuConstraints):

        self.board = sudoku
        self.candidates = candidates
        self.constraints = constraints

    def detect(self):
        for i in range(0, 9):
            box = self.candidates.get_unit(unit='box', num=i)
            for cell in box:
                if len(cell) == 1:
                    print('Naked Single found in box {}'.format(i))
