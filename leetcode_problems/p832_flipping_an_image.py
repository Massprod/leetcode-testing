# Given an n x n binary matrix image, flip the image horizontally,
#  then invert it, and return the resulting image.
# To flip an image horizontally means that each row of the image is reversed.
#  - For example, flipping [1,1,0] horizontally results in [0,1,1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
#  - For example, inverting [0,1,1] results in [1,0,0].
# --------------------
# n == image.length
# n == image[i].length
# 1 <= n <= 20
# images[i][j] is either 0 or 1.
from random import randint


def flip_and_invert_image(image: list[list[int]]) -> list[list[int]]:
    # working_sol (79.36%, 70.62%) -> (46ms, 16.45mb)  time: O(m * n) | space: O(n)
    for row in range(len(image)):
        image[row] = image[row][::-1]
    for row in range(len(image)):
        for col in range(len(image[row])):
            image[row][col] = 1 if 0 == image[row][col] else 0
    return image


# Time complexity: O(m * n) <- m - height of the input matrix `image`, n - length of the input matrix `image`.
# Always traversing the whole matrix and reversing every row, once => O(m * n).
# Extra traversing every cell of the matrix to reverse every cell value => O(2 * m * n).
# --------------------
# Auxiliary space: O(n).
# Using slicing for reversing rows, it will take extra space of the row size => O(n).


test: list[list[int]] = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
test_out: list[list[int]] = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
assert test_out == flip_and_invert_image(test)

test = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
test_out = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]
assert test_out == flip_and_invert_image(test)

test = [[randint(0, 1) for _ in range(20)] for _ in range(20)]
print(test)
