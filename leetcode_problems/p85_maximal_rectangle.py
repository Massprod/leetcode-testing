# Given a rows x cols binary matrix filled with 0's and 1's,
# find the largest rectangle containing only 1's and return its area.
# rows == matrix.length  ,  cols == matrix[i].length
# 1 <= row, cols <= 200  ,  matrix[i][j] is '0' or '1'.

def maximal_rectangle(matrix: list[list[str | int]]) -> int:
    # working_sol (23.12%, 13.14%) -> (347ms, 17.7mb)  time: O(n * m) | space: O(m)
    max_area: int = 0

    def stack_calc(hist: list[str]):
        hist_max_area: int = 0
        hist.append("0")
        stack: list[int] = [-1]
        for index in range(len(hist)):
            while int(hist[index]) < int(hist[stack[-1]]):
                height: int = int(hist[stack.pop()])
                lenght: int = index - int(stack[-1]) - 1
                current_area: int = height * lenght
                hist_max_area = max(hist_max_area, current_area)
            stack.append(index)
        hist.pop()
        return hist_max_area
    for y in range(len(matrix)):
        if y >= 1:
            for x in range(len(matrix[y])):
                if int(matrix[y][x]) == 1:
                    matrix[y][x] = int(matrix[y][x]) + int(matrix[y-1][x])
        max_area = max(max_area, stack_calc(matrix[y]))
    return max_area

# Time complexity: O(n * m) -> worst_case, traversing once through all indexes in a row => O(m)
# m - lengths of a row ^^      -> calling stack_calc() and traversing this row twice with a stack => O(2m) ->
# n - lengths of a matrix ^^   -> repeating for every row in a matrix => O(n * m)
#
# Space complexity: O(m) -> creating stack of matrix_row(hist) size => O(m) -> and max_area constant => O(1)

# Using this monstrosity with converting str -> int, cuz I don't want to make extra loop to change all cells to int.
# It's going to be slower than this ^^. But it's very bad looking and error_prone.
# Will change and see diff in speed after first correct commit.
# -------------------
# After failing with p84 and googling for a method, get a glimpse of STACK problems, and this is one of them.
# We can just assume that this matrix rows as histograms,
# and every bar will have a height of cells with 1 + any 1 above (base should be 1, can't place anything on empty spot).


test1 = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
test1_out = 6
test = maximal_rectangle(test1)
assert test1_out == test
for _ in test1:
    print(_)
del test

test2 = [["0"]]
test2_out = 0
test = maximal_rectangle(test2)
assert test2_out == test
for _ in test2:
    print(_)
del test

test3 = [["1"]]
test3_out = 1
test = maximal_rectangle(test3)
assert test3_out == test
for _ in test3:
    print(_)
del test
