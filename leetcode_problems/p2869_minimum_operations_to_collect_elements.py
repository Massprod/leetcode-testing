# You are given an array nums of positive integers and an integer k.
# In one operation, you can remove the last element of the array and add it to your collection.
# Return the minimum number of operations needed to collect elements 1, 2, ..., k.
# -----------------------
# 1 <= nums.length <= 50
# 1 <= nums[i] <= nums.length
# 1 <= k <= nums.length
# The input is generated such that you can collect elements 1, 2, ..., k.


def min_operations(nums: list[int], k: int) -> int:
    # working_sol (80.85%, 95.02%) -> (37ms, 16.37mb)  time: O(n) | space: O(k)
    # !
    # The input is generated such that you can collect elements 1, 2, ..., k.
    # ! <- So, all we care is how many times we take a value from `nums`.
    not_used: set[int] = {val for val in range(1, k + 1)}
    out: int = 0
    while not_used:
        cur_num: int = nums.pop()
        if cur_num in not_used:
            not_used.remove(cur_num)
        out += 1
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always using every value from `nums`, once => O(n).
# -----------------------
# Auxiliary space: O(k)
# `not_used` <- always of the size `k` => O(k).


test: list[int] = [3, 1, 5, 4, 2]
test_k: int = 2
test_out: int = 4
assert test_out == min_operations(test, test_k)

test = [3, 1, 5, 4, 2]
test_k = 5
test_out = 5
assert test_out == min_operations(test, test_k)

test = [3, 2, 5, 3, 1]
test_k = 3
test_out = 4
assert test_out == min_operations(test, test_k)
