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
    # working_sol (46.67%, 48.90%)  time: O(n**(n*n)) | space: O(n*n)
    combos = []
    candidates.sort()
    if len(candidates) == 1:
        if candidates[0] == target:
            combos.append([candidates[0]])
            return combos
        if candidates[0] != target:
            return combos
    if sum(candidates) < target:
        return combos
    if min(candidates) > target:
        return combos

    def combinations(path: list[int], start: int = 0, summ: int = 0) -> None:
        if summ == target:
            path.sort()
            if path not in combos:
                combos.append(path)
                return
        if summ > target:
            return
        for x in range(start, len(candidates)):
            if x > start and candidates[x] == candidates[x - 1]:
                continue
            combinations(path + [candidates[x]], x + 1, summ + candidates[x])

    combinations([])
    return combos


# Time complexity: O(n**(n*n) -> for every n element in candidates recursion with n*n - branches.
# Space complexity: O(n*n) -> n lists in list for each combination.

# Slicing not just going through indexes is slower and I couldn't find a method to skip with same values.
# ! if x > start and candidates[x] == candidates[x - 1]:
#       continue    !
# This ^^^^ part I couldn't implement with slicing because everytime we slice we're losing [x - 1],
# and slicing takes time to create a new list's -> maybe rebuild p39, slicing -> indexes.
# Allows us to skip same values recursion calls, after taking first values from it.
# Only taking x < start which is first value within slice candidates[x + 1:] and other calls skipped.

# -----------------------------------------------
# I don't get how can we speed up a search.
#   - we can't stop on encountering same value - True
#   - we can stop if the same value used 30 times and still 70 left -> leads us to same combos, how can I check this?
# Creating dictionary with available usages of same number. Only allowing me to skip same_values tests.
# But what if there's 11111111121111111???
# Don't get it. We can't skip values even if it's repeating 10000times, after this 10000time can be another value,
# and we should count this as a summ.
# But if there's only ONE value in a list 10000times im skipping it with a dictionary usage. Google time?

test1 = [10, 1, 2, 7, 6, 1, 5]
test1_target = 8
test1_out = [
    [1, 1, 6],
    [1, 2, 5],
    [1, 7],
    [2, 6],
]
print(comb_sums(test1, test1_target))
answer1 = comb_sums(test1, test1_target)
assert len(answer1) == len(test1_out)
for _ in answer1:
    assert _ in test1_out

test2 = [2, 5, 2, 1, 2]
test2_target = 5
test2_out = [
    [1, 2, 2],
    [5],
]
print(comb_sums(test2, test2_target))
answer2 = comb_sums(test2, test2_target)
assert len(answer2) == len(test2_out)
for _ in answer2:
    assert _ in test2_out

# test3 - failed -> time_limit | apparently I need speed :) but I can't ignore that 1 can be used every time.
test3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
test3_target = 27
test3_out = []
answer3 = comb_sums(test3, test3_target)
print(answer3)
assert len(answer3) == len(test3_out)
for _ in answer3:
    assert _ in test3_out

# test4 - failed -> time_limit | combos = list(30x1), how can I stop iteration?
test4 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
test4_target = 30
test4_out = [[1 for _ in range(30)]]
answer4 = comb_sums(test4, test4_target)
print(answer4)
assert len(answer4) == len(test4_out)
for _ in answer4:
    assert _ in test4_out

test5 = [3, 1, 3, 5, 1, 5, 2, 3, 2, 5, 4]
test5_target = 1
test5_out = [[1]]
answer5 = comb_sums(test5, test5_target)
print(answer5)
assert len(answer5) == len(test5_out)
for _ in answer5:
    assert _ in test5_out

test6 = [2, 2, 2]
test6_target = 4
test6_out = [[2, 2]]
answer6 = comb_sums(test6, test6_target)
print(answer6)

# test7 - failed -> YEP. 11111121111 case, as I was thinking. 175/176 cases.
#                   Failed so much, not going to stop with last 2 cases, and just brute force it before googling.
test7 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
test7_target = 30
test7_out = []
print(comb_sums(test7, test7_target))
