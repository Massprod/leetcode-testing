# There is a circle of red and blue tiles.
# You are given an array of integers colors and an integer k.
# The color of tile i is represented by colors[i]:
#  - colors[i] == 0 means that tile i is red.
#  - colors[i] == 1 means that tile i is blue.
# An alternating group is every k contiguous tiles in the circle
#  with alternating colors (each tile in the group except the first and last one
#  has a different color from its left and right tiles).
# Return the number of alternating groups.
# Note that since colors represents a circle,
#   the first and the last tiles are considered to be next to each other.
# ------------------------
# 3 <= colors.length <= 10 ** 5
# 0 <= colors[i] <= 1
# 3 <= k <= colors.length


def number_of_alternating_groups(colors: list[int], k: int) -> int:
    # working_sol (46.84%, 25.91%) -> (733ms, 21.94mb)  time: O(n + k) | space: O(k)
    # Circular array with limit of `k`.
    colors = colors + colors[:k - 1]
    out: int = 0
    left: int = 0
    right: int = 1
    while right < len(colors):
        # ! 3 <= k <= colors.length ! <- if 2 in a row is equal => new window
        if colors[right] == colors[right - 1]:
            left, right = right, right + 1
            continue
        right += 1
        # We need more colors in a sequence.
        if k != (right - left):
            continue
        # Otherwise correct sequence with `k` length
        out += 1
        # And because we only care about `k` length => insta move it to the next.
        left += 1

    return out


# Time complexity: O(n + k) <- n - length of the input array `colors`.
# We expand original array by an extra `k - 1` colors to make it circular.
# And traversing resulting array, once => O(n + k).
# ------------------------
# Auxiliary space: O(k)
# `colors` <- get an extra `k - 1` values => O(k).


test: list[int] = [0, 1, 0, 1, 0]
test_k: int = 3
test_out: int = 3
assert test_out == number_of_alternating_groups(test, test_k)

test = [0, 1, 0, 0, 1, 0, 1]
test_k = 6
test_out = 2
assert test_out == number_of_alternating_groups(test, test_k)

test = [1, 1, 0, 1]
test_k = 4
test_out = 0
assert test_out == number_of_alternating_groups(test, test_k)
