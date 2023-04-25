# Given an array nums of distinct integers, return all the possible permutations.
# You can return the answer in any order.
import math


def permute(nums: list[int]) -> list[list[int]]:
    # working_sol (63.90%, 49.5%) -> (46ms, 14.1mb)  time: O(n!) | space: O(n!)
    permutes = []
    origin = nums

    def rec_permute(to_check: list[int], start_ind: int = 0):
        if start_ind == len(to_check):
            permutes.append(to_check.copy())
            return
        for x in range(start_ind, len(to_check)):
            to_check[x], to_check[start_ind] = to_check[start_ind], to_check[x]
            rec_permute(to_check, start_ind + 1)
            to_check[x], to_check[start_ind] = to_check[start_ind], to_check[x]
    rec_permute(origin)
    return permutes

# Time complexity: O(n*n!) -> calling recursion for n elements in given input,
#                             and for each element recursion for n! times.
# Space complexity: O(n!) -> creating lists with n! lists in it, n! <- all combinations of input list.

# Backtracking almost like in p22 with parentheses, but we're removing element not adding it,
# and switching every index on every position from ! 0-len()-1 ! until we run out of them | start_ind == len(to_check)
# After switching, always rebuilding list to_check into pre_recursion state.


test1 = [1, 2, 3]
test1_out = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
print(permute(test1))
for _ in test1_out:
    test = permute(test1)
    assert len(test1_out) == len(test)
    assert _ in test

test2 = [0, 1]
test2_out = [[0, 1], [1, 0]]
print(permute(test2))
for _ in test2_out:
    test = permute(test2)
    assert len(test2_out) == len(test)
    assert _ in test

test3 = [1]
test3_out = [[1]]
print(permute(test3))
for _ in test3_out:
    test = permute(test3)
    assert len(test3_out) == len(test)
    assert _ in test

test4 = [1, 2, 3, 4, 5, 6, 7]
print(math.factorial(len(test4)))
print(len(permute(test4)))
