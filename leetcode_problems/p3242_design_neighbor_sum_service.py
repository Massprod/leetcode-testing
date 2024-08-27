# You are given a n x n 2D array grid containing distinct elements in the range [0, n ** 2 - 1].
# Implement the NeighborSum class:
#  - NeighborSum(int [][]grid) initializes the object.
#  - int adjacentSum(int value) returns the sum of elements which are adjacent neighbors of value,
#    that is either to the top, left, right, or bottom of value in grid.
#  - int diagonalSum(int value) returns the sum of elements which are diagonal neighbors of value,
#    that is either to the top-left, top-right, bottom-left, or bottom-right of value in grid.
# ---------------------------
# 3 <= n == grid.length == grid[0].length <= 10
# 0 <= grid[i][j] <= n ** 2 - 1
# All grid[i][j] are distinct.
# value in adjacentSum and diagonalSum will be in the range [0, n ** 2 - 1].
# At most 2 * n ** 2 calls will be made to adjacentSum and diagonalSum.


class NeighborSum:
    # working_sol (43.09%, 77.64%) -> (182ms, 16.75mb)
    def __init__(self, grid: list[list[int]]):
        self.grid: list[list[int]] = grid
        self.values: dict[int, dict[str, int]] = {}
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                self.values[self.grid[row][col]] = {
                    'row': row,
                    'col': col,
                    'adjSum': -1,
                    'diagSum': -1,
                }
        # [dy, dx]
        self.adj_options: list[list[int]] = [
            [-1, 0], [0, 1], [1, 0], [0, -1],
        ]
        self.diag_options: list[list[int]] = [
            [-1, -1], [-1, 1], [1, 1], [1, -1],
        ]

    def adjacentSum(self, value: int) -> int:
        out: int = 0
        if value in self.values and -1 != self.values[value]['adjSum']:
            return self.values[value]['adjSum']
        row: int = self.values[value]['row']
        col: int = self.values[value]['col']
        for dy, dx in self.adj_options:
            new_row: int = row + dy
            new_col: int = col + dx
            if 0 <= new_row < len(self.grid) and 0 <= new_col < len(self.grid[0]):
                out += self.grid[new_row][new_col]
        self.values[value]['adjSum'] = out
        return out

    def diagonalSum(self, value: int) -> int:
        out: int = 0
        if value in self.values and -1 != self.values[value]['diagSum']:
            return self.values[value]['diagSum']
        row: int = self.values[value]['row']
        col: int = self.values[value]['col']
        for dy, dx in self.diag_options:
            new_row: int = row + dy
            new_col: int = col + dx
            if 0 <= new_row < len(self.grid) and 0 <= new_col < len(self.grid[0]):
                out += self.grid[new_row][new_col]
        self.values[value]['diagSum'] = out
        return out
