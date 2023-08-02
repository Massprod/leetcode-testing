# Given an array nums of distinct integers, return all the possible permutations.
# You can return the answer in any order.
# ------------
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
import math


def permute(nums: list[int]) -> list[list[int]]:
    # working_sol (98.74%, 99.5%) -> (39ms, 14.1mb)  time: O(n * n!) | space: O(n * n!)
    # n! == all permutations of any n size.
    permutations: list[list[int]] = []

    def rec_permute(to_check: list[int], start_ind: int = 0) -> None:
        # start_ind out of bounds, and we can't switch.
        if start_ind == len(to_check):
            permutations.append(to_check.copy())
            return
        # Every start_ind will be placed on every other index_position once.
        # And recalling for every start_ind possible.
        # [0, 1, 2] -> [1, 0, 2] -> [2, 0, 1] <- 0 switched with everyone and recall for every switch.
        # inside [1, 0, 2] -> [1, 2, 0] etc.
        for x in range(start_ind, len(to_check)):
            to_check[x], to_check[start_ind] = to_check[start_ind], to_check[x]
            rec_permute(to_check, start_ind + 1)
            to_check[x], to_check[start_ind] = to_check[start_ind], to_check[x]

    rec_permute(nums)
    return permutations


# Time complexity: O(n * n!) -> n! == permutations of some array with n elements without duplicates ->
# n - len of input_array^^|  -> we're building all these permutations and in the worst case starting from 0 -> n
#                            looping through all elements of n, extra copying them into permutations => O(n * n!).
# Auxiliary space: O(n * n!) -> creating lists with n! lists in it, and every list is size of n => O(n * n!).
# ------------
# Backtracking almost like in p22 with parentheses, but we're removing element not adding it,
# and switching every index on every position from ! 0-len()-1 ! until we run out of them | start_ind == len(to_check)
# After switching, always rebuilding list to_check into pre_calling state.


test1 = [1, 2, 3]
test1_out = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
test: list[list[int]] = permute(test1)
for _ in test1_out:
    assert len(test1_out) == len(test)
    assert _ in test
del test

test2 = [0, 1]
test2_out = [[0, 1], [1, 0]]
test = permute(test2)
for _ in test2_out:
    assert len(test2_out) == len(test)
    assert _ in test
del test

test3 = [1]
test3_out = [[1]]
test = permute(test3)
for _ in test3_out:
    assert len(test3_out) == len(test)
    assert _ in test
del test

# Time/Space complexity visualisation.
test4 = [1, 2, 3, 4, 5, 6, 7]
print(math.factorial(len(test4)))
print(len(permute(test4)))
