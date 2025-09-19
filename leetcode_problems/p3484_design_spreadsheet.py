# A spreadsheet is a grid with 26 columns (labeled from 'A' to 'Z')
#  and a given number of rows.
# Each cell in the spreadsheet can hold an integer value between 0 and 10 ** 5.
# Implement the Spreadsheet class:
#  - Spreadsheet(int rows) Initializes a spreadsheet with 26 columns (labeled 'A' to 'Z')
#    and the specified number of rows. All cells are initially set to 0.
#  - void setCell(String cell, int value) Sets the value of the specified cell.
#    The cell reference is provided in the format "AX" (e.g., "A1", "B10"),
#    where the letter represents the column (from 'A' to 'Z')
#    and the number represents a 1-indexed row.
#  - void resetCell(String cell) Resets the specified cell to 0.
#  - int getValue(String formula) Evaluates a formula of the form "=X+Y",
#    where X and Y are either cell references or non-negative integers,
#    and returns the computed sum.
#  - Note: If getValue references a cell that has not been explicitly set using setCell,
#    its value is considered 0.
# --- --- --- ---
# 1 <= rows <= 10 ** 3
# 0 <= value <= 10 ** 5
# The formula is always in the format "=X+Y", where X and Y
#  are either valid cell references or non-negative integers with values
#  less than or equal to 10 ** 5.
# Each cell reference consists of a capital letter from 'A' to 'Z' followed
#  by a row number between 1 and rows.
# At most 10 ** 4 calls will be made in total to setCell, resetCell, and getValue.
from string import ascii_uppercase


class Spreadsheet:
    # working_solution: (26.16%, 9.77%) -> (247ms, 23.97mb)  Time: O(n) Space: O(n)
    def __init__(self, rows: int) -> None:
        # { column: [ list of values, index == row number <- 0 - indexed ] }
        self.spreadsheet: dict[str, list[int]] = {
            char: [0 for _ in range(rows)]
            for char in ascii_uppercase
        }

    def get_cell_coord(self, cell: str) -> tuple[str, int]:
        # (column, row)
        return ( cell[0], int(cell[1:]) )

    def setCell(self, cell: str, value: int) -> None:
        column: str
        row: int
        column, row = self.get_cell_coord(cell)
        self.spreadsheet[column][row - 1] = value  # -1 for 0 - indexed.

    def resetCell(self, cell: str) -> None:
        column: str
        row: int
        column, row = self.get_cell_coord(cell)
        self.spreadsheet[column][row - 1] = 0

    def getValue(self, formula: str) -> int:
        column: str
        row: int
        stripped_formula: str = formula[1:]
        values: list[str] = stripped_formula.split('+')
        out: int = 0
        for value in values:
            # It's just an integer => insta sum it.
            if not self.spreadsheet.get(value[0]):
                out += int(value)
                continue
            # Otherwise, get the value.
            column, row = self.get_cell_coord(value)
            out += self.spreadsheet[column][row - 1]
        
        return out


# Time complexity: O(n) <- input init value `rows`
# Everything is constant, except an initiation.
# We create a list with `rows` values => O(n).
# --- --- --- ---
# Space complexity: O(n)
# `self.spreadsheet` <- allocates space for each created row.
