# Given an integer array nums of unique elements,
#  return all possible subsets (the power set).
# The solution set must not contain duplicate subsets.
# Return the solution in any order.
# ------------------------
# 1 <= nums.length <= 10  ,  -10 <= nums[i] <= 10
# All the numbers of nums are unique.
from random import shuffle, randint


def subsets(nums: list[int]) -> set[tuple[int, ...]]:
    # working_sol (80.68%, 77.55%) -> (33ms, 16.61mb)  time: O(n * 2 ** n) | space: O(n * 2 ** n)
    # We have only unique values, but they can be disordered.
    # So, we either check for what we already used in `subset` or sort beforehand.
    nums.sort()
    all_subsets: set[tuple[int, ...]] = set()
    # Empty `subset`
    all_subsets.add(())

    def new_subset(start_index: int, length: int, subset: list[int]) -> None:
        nonlocal all_subsets
        if length == len(subset):
            all_subsets.add(tuple(subset))
            return
        # Use or skip element.
        for index in range(start_index, len(nums)):
            new_subset(index + 1, length, subset + [nums[index]])

    for length_limit in range(1, len(nums) + 1):
        new_subset(0, length_limit, [])
    return all_subsets


# Time complexity: O(n * 2 ** n) <- n - length of an input array `nums`.
# First, we're sorting `nums` to use them without bothering about duplicates => O(n * log n).
# Second, we're looping through `n` `length_limit` options to get all the (2 ** n) combinations => O(n * 2 ** n).
# ------------------------
# Auxiliary space: O(n * 2 ** n)
# There's (2 ** n) solutions, and their max size is `n` => O(n * 2 ** n).


test: list[int] = [1, 2, 3]
test_out: set[tuple[int, ...]] = set([tuple(_list) for _list in [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]])
test_res: set[tuple[int, ...]] = subsets(test)
assert test_res == test_out

test = [0]
test_out = set([tuple(_list) for _list in [[], [0]]])
test_res = subsets(test)
assert test_res == test_out

test_uniques: set[int] = set()
while len(test_uniques) < 10:
    test_uniques.add(randint(-10, 10))
test = list(test_uniques)
shuffle(test)
print(test)
