# You are given n rectangles represented by a 0-indexed 2D integer array rectangles,
#  where rectangles[i] = [widthi, heighti] denotes the width and height of the ith rectangle.
# Two rectangles i and j (i < j) are considered interchangeable if they have the same width-to-height ratio.
# More formally, two rectangles are interchangeable if widthi/heighti == widthj/heightj
#  (using decimal division, not integer division).
# Return the number of pairs of interchangeable rectangles in rectangles.
# ---------------------------
# n == rectangles.length
# 1 <= n <= 10 ** 5
# rectangles[i].length == 2
# 1 <= widthi, heighti <= 10 ** 5
from collections import defaultdict


def interchangeable_rectangles(rectangles: list[list[int]]) -> int:
    # working_sol (82.63%, 43.36%) -> (1290ms, 72.86mb)  time: O(n) | space: O(n)
    out: int = 0
    # {ratio: # of rectangles with such a ratio}
    ratios: dict[float, int] = defaultdict(int)
    for width, height in rectangles:
        ratios[width / height] += 1
    # n * (n - 1) // 2 <- all combinations with 2 unique elements
    for key, value in ratios.items():
        out += (value * (value - 1)) // 2
    return out


# Time complexity: O(n) <- n - length of the input array `rectangles`
# Traversing whole input array `rectangles` to get all rectangle ratios => O(n)
# In the worst case, every rectangle is having a unique ratio.
# So, we will extra traverse `n` keys in `ratios` to calc their combinations => O(n).
# ---------------------------
# Auxiliary space: O(n)
# Same worst case, we will have `ratios` with `n` keys and INT for each => O(n).


test: list[list[int]] = [[4, 8], [3, 6], [10, 20], [15, 30]]
test_out: int = 6
assert test_out == interchangeable_rectangles(test)

test = [[4, 5], [7, 8]]
test_out = 0
assert test_out == interchangeable_rectangles(test)
