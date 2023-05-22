# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.
# -------------------------
# 1 <= nums.length <= 10  ,  -10 <= nums[i] <= 10


def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    # working_sol (5.26%, 6.4%) -> (64ms, 16.8mb)  time: O(n * (n ** k) + g * h) | space: O(2 * (n * (nCk * k)))
    k_numbers: set = set()
    tempo: list[int] = []
    power_set: list[list[int]] = [[]]

    def new_combine(left_to_use: int, start: int = 0, end: int = len(nums), ) -> None:
        if left_to_use == 0:
            k_numbers.add(tuple(sorted(tempo)))
            return
        for num in range(start, end):
            if num in tempo:
                break
            tempo.append(num)
            new_combine(left_to_use - 1, start + 1, end)
            tempo.pop()

    for x in range(1, len(nums) + 1):
        new_combine(x)
    new_set: list[int] = []
    for tup in k_numbers:
        for index in tup:
            new_set.append(nums[index])
        new_set.sort()
        if new_set not in power_set:
            power_set.append(new_set)
        new_set = []
    return power_set


# Time complexity: O(n * (n ** k) + g * h) -> recursion tree with n branches and k depths => O(n ** k) ->
# g - number of created tuples ^^             -> calling recursion for input_nums_length times => O(n * (n ** k) ->
# h - size of a tuple          ^^             -> nested loop for all created tuples in recursion => O(g * h).
# n - length of input_nums     ^^
# k - size of a subset         ^^
# ---------------------
# Space complexity: O(2 * (n * (nCk * k))) -> creating set() with tuples of index_combinations
# n - length of input_nums     ^^             for sizes from 1 to len(nums) => O(n * (nCk * k)) ->
# k - size of a subset         ^^             -> creating list of the same size but filled with values from indexes.
# ! worst case there's no duplicates, and we're creating list + set of identical size, but in case of duplicates,
#   only part of n will be used and duplicates ignored in power_set => O(log n * (nCk * k)) !
# -------------------------
# Well it's working, but I just reused solution with extra check if combo already in power_set.
# 67ms is fine for me, not going to rebuild it.
# -------------------------
# If I recall correctly what I made in p78, is unique permutations for all INDEXES in a list.
# Not just numbers in not, so it's should work with that, because w.e is inside we're just going to get all
# unique combinations of INDEXES not values on it.
# Try to reuse it, maybe modify, but already did this in p78 with same logic,
# if w.e values we have, all we need is combinations of indexes.


test1 = [1, 2, 2]
test1_out = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
test = subsets_with_dup(test1)
print(test)
assert len(test) == len(test1_out)
for _ in test:
    assert _ in test1_out
del test

test2 = [0]
test2_out = [[], [0]]
test = subsets_with_dup(test2)
print(test)
assert len(test) == len(test2_out)
for _ in test:
    assert _ in test2_out
del test

# test3 - failed -> I was stupid enough to use all combinations without sorting, and forgot about task_rule,
#                   we shouldn't have duplicates -> which is same values when sorted [1, 4] == [4,1].
#                   Don't want to rebuild until I hit time_limit, so I will just sort it before append.
test3 = [4, 4, 4, 1, 4]
test3_out = [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]]
test = subsets_with_dup(test3)
print(test)
assert len(test) == len(test3_out)
for _ in test:
    assert _ in test3_out
del test
