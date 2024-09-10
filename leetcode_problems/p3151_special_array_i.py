# An array is considered special if every pair of its adjacent elements contains two numbers with different parity.
# You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.
# -------------------------
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100


def is_array_special(nums: list[int]) -> bool:
    # working_sol (33.59%, 90.99%) -> (56ms, 16.50mb)  time: O(n) | space: O(1)
    for index in range(1, len(nums)):
        if nums[index] % 2 == nums[index - 1] % 2:
            return False
    return True


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing whole input array `nums`, once => O(n).
# -------------------------
# Auxiliary space: O(1).


test: list[int] = [1]
test_out: bool = True
assert test_out == is_array_special(test)

test = [2, 1, 4]
test_out = True
assert test_out == is_array_special(test)

test = [4, 3, 1, 6]
test_out = False
assert test_out == is_array_special(test)
