# There is a circle of red and blue tiles.
# You are given an array of integers colors.
# The color of tile i is represented by colors[i]:
#  - colors[i] == 0 means that tile i is red.
#  - colors[i] == 1 means that tile i is blue.
# Every 3 contiguous tiles in the circle with alternating colors
#  (the middle tile has a different color from its left and right tiles) is called an alternating group.
# Return the number of alternating groups.
# Note that since colors represents a circle,
#  the first and the last tiles are considered to be next to each other.
# ----------------------
# 3 <= colors.length <= 100
# 0 <= colors[i] <= 1


def number_of_alternating_groups(colors: list[int]) -> int:
    # working_sol (88.64%, 77.64%) -> (46ms, 16.46mb)  time: O(n) | space: O(n)
    out: int = 0
    # ! 3 <= colors.length <= 100 ! <- we always need to have circle.
    cor_circle: list[int] = [colors[-1]] + colors + [colors[0]]
    for index in range(1, len(cor_circle) - 1):
        if (cor_circle[index - 1] != cor_circle[index] != cor_circle[index + 1]
                and cor_circle[index - 1] == cor_circle[index + 1]):
            out += 1
    return out


# Time complexity: O(n) <- n - length of the input array `colors`.
# Always converting an input array to `cor_circle` => O(n + 2).
# Extra traversing every index of `cor_circle`, once => O((n + 2) * 2).
# ----------------------
# Auxiliary space: O(n)
# `cor_circle` <- always of the same size == `n + 2` => O(n + 2).


test: list[int] = [1, 1, 1]
test_out: int = 0
assert test_out == number_of_alternating_groups(test)

test = [0, 1, 0, 0, 1]
test_out = 3
assert test_out == number_of_alternating_groups(test)
