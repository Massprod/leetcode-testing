# Given a rows x cols binary matrix filled with 0's and 1's,
# find the largest rectangle containing only 1's and return its area.
# rows == matrix.length  ,  cols == matrix[i].length
# 1 <= row, cols <= 200  ,  matrix[i][j] is '0' or '1'.

def maximal_rectangle(matrix: list[list[int]]) -> int:
    pass


test1 = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
test1_out = 6

test2 = [["0"]]
test2_out = 0

test3 = [["1"]]
test3_out = 1
