# In the town of Digitville, there was a list of numbers called nums containing integers from 0 to n - 1.
# Each number was supposed to appear exactly once in the list, however,
#  two mischievous numbers sneaked in an additional time, making the list longer than usual.
# As the town detective, your task is to find these two sneaky numbers.
# Return an array of size two containing the two numbers (in any order),
#  so peace can return to Digitville.
# -----------------------
# 2 <= n <= 100
# nums.length == n + 2
# 0 <= nums[i] < n
# The input is generated such that nums contains exactly two repeated elements.


def get_sneaky_numbers(nums: list[int]) -> list[int]:
    # working_sol (80.59%, 97.64%) -> (45ms, 16.38mb)  time: O(n) | space: O(1)
    out: list[int] = []
    limit: int = -150
    # !
    # The input is generated such that nums contains exactly two repeated elements.
    # ! <- we can just use original to mark spots.
    for num in nums:
        if limit == num:
            continue
        target: int = abs(num)
        if 0 > nums[target]:
            out.append(abs(num))
        else:
            if 0 == nums[target]:
                nums[target] = -150
            else:
                nums[target] *= -1
    # We're skipping `0` because we're marking it as `-150`.
    # So, we need to extra add it later.
    if 2 == len(out):
        return out
    return out + [0]


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing whole input array `nums`, once => O(n).
# -----------------------
# Auxiliary space: O(1)
# `out` <- always of the constant size `2`, nothing extra is used => O(1).


test: list[int] = [0, 1, 1, 0]
test_out: list[int] = [0, 1]
assert test_out == sorted(get_sneaky_numbers(test))

test = [0, 3, 2, 1, 3, 2]
test_out = [2, 3]
assert test_out == sorted(get_sneaky_numbers(test))

test = [7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]
test_out = [4, 5]
assert test_out == sorted(get_sneaky_numbers(test))

test = [1, 0, 1, 0]
test_out = [0, 1]
assert test_out == sorted(get_sneaky_numbers(test))
