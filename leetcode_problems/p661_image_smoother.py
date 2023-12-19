# An image smoother is a filter of the size 3 x 3 that can be applied
#  to each cell of an image by rounding down the average of the cell and the eight surrounding cells
#  (i.e., the average of the nine cells in the blue smoother).
# If one or more of the surrounding cells of a cell is not present,
#  we do not consider it in the average (i.e., the average of the four cells in the red smoother).
# Given an m x n integer matrix img representing the grayscale of an image,
#  return the image after applying the smoother on each cell of it.
# ----------------
# m == img.length
# n == img[i].length
# 1 <= m, n <= 200
# 0 <= img[i][j] <= 255
from random import randint


def image_smoother(img: list[list[int]]) -> list[list[int]]:
    # working_sol (26.67%, 59.70%) -> (528ms, 17mb)  time: O(m * n) | space: O(m * n)
    # Step options (dy, dx) in clockwise from top-left -> left.
    options: list[tuple[int, int]] = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    out: list[list[int]] = [[col for col in range(len(img[row]))] for row in range(len(img))]
    for row in range(len(img)):
        for col in range(len(img[row])):
            # We need current cell + 8 neighbours (of less if not available).
            summ: int = img[row][col]
            # avg = sum // cells used
            cells: int = 1
            for option in options:
                new_row: int = row + option[0]
                new_col: int = col + option[1]
                if 0 <= new_row < len(img) and 0 <= new_col < len(img[row]):
                    summ += img[new_row][new_col]
                    cells += 1
            out[row][col] = summ // cells
    return out


# Time complexity: O(m * n) <- m - rows of input matrix `img`, n - columns of input matrix `img`.
# Single traverse to recreate original `img` as `out` => O(m * n).
# Another traverse to calc every cell average => O(m * n * 8).
# Auxiliary space: O(m * n).
# Copy of original input matrix `img`, but with different values.


test: list[list[int]] = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
test_out: list[list[int]] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
assert test_out == image_smoother(test)

test = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
test_out = [[137, 141, 137], [141, 138, 141], [137, 141, 137]]
assert test_out == image_smoother(test)

test = [[randint(0, 255) for _ in range(200)] for _ in range(200)]
print(test)
