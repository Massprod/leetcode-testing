# There are n people that are split into some unknown number of groups.
# Each person is labeled with a unique ID from 0 to n - 1.
# You are given an integer array groupSizes, where groupSizes[i]
#  is the size of the group that person i is in. For example, if groupSizes[1] = 3,
#  then person 1 must be in a group of size 3.
# Return a list of groups such that each person i is in a group of size groupSizes[i].
# Each person should appear in exactly one group, and every person must be in a group.
# If there are multiple answers, return any of them.
# It is guaranteed that there will be at least one valid solution for the given input.
# --------------------------
# groupSizes.length == n
# 1 <= n <= 500
# 1 <= groupSizes[i] <= n


def group_the_people(groupSizes: list[int]) -> list[list[int]]:
    # working_sol (84.71%, 91.52%) -> (69ms, 16.31mb)  time: O(n) | space: O(n)
    # Groups by size, with values of the group inside.
    groups: dict[int, list[list[int]]] = {}
    out: list[list[int]] = []
    for x in range(len(groupSizes)):
        size: int = groupSizes[x]
        if size in groups:
            if len(groups[size][-1]) != size:
                groups[size][-1].append(x)
        else:
            groups[size] = [[x]]
        # If group fully filled, populate answer + reset.
        if len(groups[size][-1]) == size:
            out.append(groups[size][-1])
            groups[size] = [[]]
    return out


# Time complexity: O(n) -> worst case, [1 for _ in range(500)] every value will be in the unique group ->
# n - len of input_list^^| -> traversing once to get all values by their groups, and append if correct size => O(n).
# Auxiliary space: O(n) -> same case, for every value creating list with it inside => O(n).
#                          Otherwise, multiple lists with essentially n values inside, linear anyway.
# --------------------------
# Save everything by groups and return combined. Should be easy. Totally can be done with one traverse.
# What if I check correct len of the group after adding? Correct 1 traverse.


test: list[int] = [3, 3, 3, 3, 3, 1, 3]
test_out: list[list[int]] = [[0, 1, 2], [3, 4, 6], [5]]
for ans in group_the_people(test):
    assert ans in test_out

test = [2, 1, 3, 3, 3, 2]
test_out = [[1], [0, 5], [2, 3, 4]]
for ans in group_the_people(test):
    assert ans in test_out
