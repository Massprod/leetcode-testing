# Given an array of distinct integers candidates
# and a target integer target, return a list of all unique combinations of candidates
# where the chosen numbers sum to target. You may return the combinations in any order.
#
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
# frequency
#  of at least one of the chosen numbers is different.
#
# The test cases are generated such that the number of unique combinations that sum
# up to target is less than 150 combinations for the given input.

# combinations with backtrack like in p22??

def comb_sum(candidates: list[int], target: int) -> list[list[int]]:
    combos = []
    tempo = []

    def combinations(sliced: list[int], summ: int) -> list[int]:
        pass
    combinations(candidates, target)
    return combos


test1 = [2, 3, 6, 7]
test1_target = 7
test1_out = [[2, 2, 3], [7]]

test2 = [2, 3, 5]
test2_target = 8
test2_out = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

test3 = [2]
test3_target = 1
test3_out = []
