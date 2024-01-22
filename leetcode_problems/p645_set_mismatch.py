# You have a set of integers s, which originally contains all the numbers from 1 to n.
# Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set,
#  which results in repetition of one number and loss of another number.
# You are given an integer array nums representing the data status of this set after the error.
# Find the number that occurs twice and the number that is missing and return them in the form of an array.
# ---------------------
# 2 <= nums.length <= 10 ** 4
# 1 <= nums[i] <= 10 ** 4


def find_error_nums(nums: list[int]) -> list[int]:
    # working_sol (93.71%, 51.72%) -> (151ms, 18.69mb)  time: O(n) | space: O(n)
    # [all values we need to have: 1 -> n, inclusive]
    all_used: set[int] = {num for num in range(1, len(nums) + 1)}
    # [used twice, missing]
    out: list[int] = [0, 0]
    for num in nums:
        if num in all_used:
            all_used.remove(num)
        else:
            out[0] = num
    out[1] = all_used.pop()
    return out


# Time complexity: O(n) <- n - length of input array `nums`.
# Creating array `all_used` with size of `n`, including all values we should have => O(n).
# Traversing original input array `nums` to check for duplicate and find missing one => O(n).
# remove() and pop() are constant.
# ---------------------
# Auxiliary space: O(n).
# We're always creating `all_used` depending on size of input array `nums` and they're equal sized => O(n).


test: list[int] = [1, 2, 2, 4]
test_out: list[int] = [2, 3]
assert test_out == find_error_nums(test)

test = [1, 1]
test_out = [1, 2]
assert test_out == find_error_nums(test)

test = [9, 5, 4, 3, 2, 1, 1, 6, 7, 8]
test_out = [1, 10]
assert test_out == find_error_nums(test)
