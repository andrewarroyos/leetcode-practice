"""LeetCode 36: Valid Sudoku (Medium).

Determine whether a 9 x 9 Sudoku board is valid. Only filled cells are checked:
each row, column, and 3 x 3 box must contain no repeated digit from 1 through 9.
Empty cells are represented by ".".
A valid partial board does not need to be solvable. Do not solve the puzzle.

Input: a list of 9 lists, each containing 9 single-character strings.
Output: True or False. All cells are "." or digits "1" through "9".

Implement the blank method(s) below. No solution or algorithm hints included.
Run: python 07_valid_sudoku.py
Uses only Python's standard library. Tests fail until you implement the solution.
"""

import unittest


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # TODO: Your solution goes here.








        pass


class TestValidSudoku(unittest.TestCase):
    def test_examples(self):
        rows = [
            "53..7....",
            "6..195...",
            ".98....6.",
            "8...6...3",
            "4..8.3..1",
            "7...2...6",
            ".6....28.",
            "...419..5",
            "....8..79",
        ]
        board = [list(row) for row in rows]
        self.assertIs(Solution().isValidSudoku(board), True)

    def test_partial_boards(self):
        cases = [
            ("empty", [], True),
            ("single_digit", [(0, 0, "5")], True),
            ("row_duplicate", [(0, 0, "5"), (0, 4, "5")], False),
            ("column_duplicate", [(0, 0, "5"), (4, 0, "5")], False),
            ("box_duplicate", [(0, 0, "5"), (1, 1, "5")], False),
            ("bottom_box_duplicate", [(6, 6, "9"), (8, 8, "9")], False),
            ("allowed_repeated_digit", [(0, 0, "5"), (4, 4, "5")], True),
        ]
        for name, cells, expected in cases:
            with self.subTest(case=name):
                board = [["."] * 9 for _ in range(9)]
                for row, col, value in cells:
                    board[row][col] = value
                self.assertIs(Solution().isValidSudoku(board), expected)

    def test_completed_board(self):
        rows = [
            "534678912", "672195348", "198342567",
            "859761423", "426853791", "713924856",
            "961537284", "287419635", "345286179",
        ]
        self.assertIs(Solution().isValidSudoku([list(row) for row in rows]), True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
