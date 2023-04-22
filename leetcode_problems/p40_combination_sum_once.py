# Given a collection of candidate numbers (candidates) and a target
# number (target), find all unique combinations in candidates where
# the candidate numbers sum to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note: The solution set must not contain duplicate combinations.

# As always they want to return list, but in reality it can be set...
# w.e speed not a goal here

def comb_sums(candidates: list[int], target: int) -> list[list[int]]:
    pass


test1 = [10, 1, 2, 7, 6, 1, 5]
test1_target = 8
test1_out = [
    [1, 1, 6],
    [1, 2, 5],
    [1, 7],
    [2, 6],
]

test2 = [2, 5, 2, 1, 2]
test2_target = 5
test2_out = [
    [1, 2, 2],
    [5],
]
