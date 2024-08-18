# Given an integer array nums of size n, return the number with the value closest to 0 in nums.
# If there are multiple answers, return the number with the largest value.
# ------------------------------
# 1 <= n <= 1000
# -10 ** 5 <= nums[i] <= 10 ** 5
from random import randint


def find_closest_number(nums: list[int]) -> int:
    # working_sol (85.39%, 60.70%) -> (115ms, 16.71mb)  time: O(n) | space: O(1)
    cur_distance: int = 10 ** 5
    cur_num: int = -10 ** 5
    for num in nums:
        distance: int = abs(0 + num)
        if distance < cur_distance:
            cur_num = num
            cur_distance = distance
        elif distance == cur_distance:
            cur_num = max(cur_num, num)
    return cur_num


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing whole input array `nums`, once => O(n).
# ------------------------------
# Auxiliary space: O(1).
# Only 3 constant INTs used, none of them depends on input => O(1).


test: list[int] = [-4, -2, 1, 4, 8]
test_out: int = 1
assert test_out == find_closest_number(test)

test = [2, -1, 1]
test_out = 1
assert test_out == find_closest_number(test)

test = [randint(-10 ** 5, 10 ** 5) for _ in range(1000)]
print(test)
