# Given an array of distinct integers candidates
# and a target integer target, return a list of all unique combinations of candidates
# where the chosen numbers sum to target. You may return the combinations in any order.
#
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
# frequency of at least one of the chosen numbers is different.
#
# The test cases are generated such that the number of unique combinations that sum
# up to target is less than 150 combinations for the given input.

# combinations with backtrack like in p22??

def comb_sum(candidates: list[int], target: int) -> list[list[int]]:
    # first_working_sol (5%, 21.25%)  time: O(n**(n*n)) | space: O(n*n)
    combos = []
    tempo = []

    def combinations(sliced: list[int], temp: list) -> None:
        if sum(temp) == target:
            to_add = temp.copy()
            to_add.sort()
            if to_add not in combos:
                combos.append(to_add)
                return
        if sum(temp) > target:
            return
        for _ in sliced:
            temp.append(_)
            combinations(sliced, temp)
            temp.pop()

    combinations(candidates, tempo)
    return combos


# Time complexity: O(n**(n*n)) -> for every n element in candidates recursion with n*n - branches
# Space complexity: O(n*n) -> n lists in list for each combination, worst case -> we have all candidates
#                             returns with correct summ.


test1 = [2, 3, 6, 7]
test1_target = 7
test1_out = [[2, 2, 3], [7]]
print(comb_sum(test1, test1_target))
assert comb_sum(test1, test1_target) == test1_out

test2 = [2, 3, 5]
test2_target = 8
test2_out = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
print(comb_sum(test2, test2_target))
assert comb_sum(test2, test2_target) == test2_out

test3 = [2]
test3_target = 1
test3_out = []
print(comb_sum(test3, test3_target))
assert comb_sum(test3, test3_target) == test3_out

# Test4 - failed, -> I was using sort to check if there's duplicate already existing in COMBOS.
#                   Stupid enough to SORT temp where's values going to be removed by POP() and it's always right_most
#                   obviously after sorting it's not last_value added......
#                   There's 2 way to work it fine is to make copy and sort it before appending,
#                   or we have all DISTINCT_DIGITS and I could use remove(value) to remove last added value.
#                   Because it's a SUM there's no matter what order of this value in a temp would be.
test4 = [7, 3, 2]
test4_target = 18
test4_out = [
    [7, 7, 2, 2],
    [7, 3, 3, 3, 2],
    [7, 3, 2, 2, 2, 2],
    [3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 2, 2, 2],
    [3, 3, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2]
]
for _ in test4_out:  # You may return the combinations in any order.
    _.sort()
print(comb_sum(test4, test4_target))
assert test4_out == comb_sum(test4, test4_target)
