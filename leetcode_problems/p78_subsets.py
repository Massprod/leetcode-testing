# Given an integer array nums of unique elements, return all possible subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.
# ------------------------
# 1 <= nums.length <= 10  ,  -10 <= nums[i] <= 10
# All the numbers of nums are unique.


def subsets(nums: list[int]) -> list[list[int]]:
    # working_sol (24.47%, 10.45%) -> (49ms, 16.7mb)  time: O(n * (n ** k) + g * h) | space: O(n * (nCk * k))
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
# ---------------------
# Well. Unexpectedly it's not slow and worked as intended.
# ---------------------
# I made a bad solution, and dunno about time_limit, but I wanted to use my previous solution(p77) for
# all combinations with different sizes and expend it to this.
# 99% need to rebuild but let's try to commit this first.


test1 = [1, 2, 3]
test1_out = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
test = subsets(test1)
for _ in test1_out:
    assert _ in test
print(test)
del test

test2 = [0]
test2_out = [[], [0]]
test = subsets(test2)
for _ in test2_out:
    assert _ in test
print(test)
del test
