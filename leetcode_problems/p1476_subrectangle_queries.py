# Implement the class SubrectangleQueries which receives a rows x cols rectangle as a matrix of integers
#  in the constructor and supports two methods:
# 1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)
#   - Updates all values with newValue in the subrectangle whose upper left coordinate is (row1,col1)
#     and bottom right coordinate is (row2,col2).
# 2. getValue(int row, int col)
#   - Returns the current value of the coordinate (row,col) from the rectangle.
# ---------------------------
# There will be at most 500 operations considering both methods: updateSubrectangle and getValue.
# 1 <= rows, cols <= 100
# rows == rectangle.length
# cols == rectangle[i].length
# 0 <= row1 <= row2 < rows
# 0 <= col1 <= col2 < cols
# 1 <= newValue, rectangle[i][j] <= 10^9
# 0 <= row < rows
# 0 <= col < cols


class SubrectangleQueries:
    # working_sol (41.89%, 78.68%) -> (141ms, 18.54mb)
    def __init__(self, rectangle: list[list[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        try:
            for row in range(row1, row2 + 1):
                for col in range(col1, col2 + 1):
                    self.rectangle[row][col] = newValue
        except IndexError:
            return

    def getValue(self, row: int, col: int) -> int | None:
        if (0 <= row < len(self.rectangle)
                and 0 <= col < len(self.rectangle[0])):
            return self.rectangle[row][col]
        return None


# Time complexity:
#   `updateSubrectangle`: O((row2 - row1) * (col2 - col1))
#   `getValue`: O(1)
# Auxiliary space:
#   nothing extra used
