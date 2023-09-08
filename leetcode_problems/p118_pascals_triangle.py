# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
# -----------------
# 1 <= numRows <= 30


def generate(numRows: int) -> list[list[int]]:
    # working_sol (90.92%, 71.54%) -> (35ms, 16.2mb)  time: O(n * log n) | space: O(n * log n)
    triangle: list[list[int]] = [[1]]
    if numRows == 1:
        return triangle
    while len(triangle) != numRows:
        triangle.append([0 for _ in range(len(triangle[-1]) + 1)])
        triangle[-1][0] = 1
        triangle[-1][-1] = 1
        for x in range(1, len(triangle[-1]) - 1):
            triangle[-1][x] = triangle[-2][x - 1] + triangle[-2][x]
    return triangle


# Time complexity: O(n * log n) -> creating n rows and for every row above, only part of maximum n given.
# Auxiliary space: O(n * log n) -> same.


test: int = 1
test_out: list[list[int]] = [[1]]
assert test_out == generate(test)

test = 5
test_out = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
assert test_out == generate(test)
