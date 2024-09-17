# There are n mountains in a row, and each mountain has a height.
# You are given an integer array height where height[i] represents
#  the height of mountain i, and an integer threshold.
# A mountain is called stable if the mountain just before it (if it exists)
#  has a height strictly greater than threshold. Note that mountain 0 is not stable.
# Return an array containing the indices of all stable mountains in any order.
# ------------------------------
# 2 <= n == height.length <= 100
# 1 <= height[i] <= 100
# 1 <= threshold <= 100


def stable_mountains(height: list[int], threshold: int) -> list[int]:
    # working_sol (62.26%, 97.21%) -> (47ms, 16.36mb)  time: O(n) | space: O(n)
    out: list[int] = []
    for index in range(1, len(height)):
        if threshold < height[index - 1]:
            out.append(index)
    return out


# Time complexity: O(n) <- n - length of the input array `height`.
# Always traversing `n - 1` indexes of the input array `height` => O(n - 1).
# ------------------------------
# Auxiliary space: O(n)
# `out` <- will store `n - 1` indexes => O(n - 1).


test_height: list[int] = [1, 2, 3, 4, 5]
test_threshold: int = 2
test_out: list[int] = [3, 4]
assert test_out == stable_mountains(test_height, test_threshold)

test_height = [10, 1, 10, 1, 10]
test_threshold = 3
test_out = [1, 3]
assert test_out == stable_mountains(test_height, test_threshold)

test_height = [10, 1, 10, 1, 10]
test_threshold = 10
test_out = []
assert test_out == stable_mountains(test_height, test_threshold)
