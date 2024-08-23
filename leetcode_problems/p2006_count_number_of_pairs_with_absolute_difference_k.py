# Given an integer array nums and an integer k, return the number of pairs (i, j)
#  where i < j such that |nums[i] - nums[j]| == k.
# The value of |x| is defined as:
#  - x if x >= 0.
#  - -x if x < 0.
# ----------------------
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
# 1 <= k <= 99


def count_k_difference(nums: list[int], k: int) -> int:
    # working_sol (81.26%, 77.28%) -> (59ms, 16.42mb)  time: O(n) | space: O(n)
    out: int = 0
    present: dict[int, int] = {}
    for num in nums:
        option: int = num - k
        if option in present:
            out += present[option]
        option = k + num
        if option in present:
            out += present[option]
        if num in present:
            present[num] += 1
        else:
            present[num] = 1
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing whole input array `nums`, once => O(n).
# ----------------------
# Auxiliary space: O(n)
# `present` <- allocates space for every value from `nums` => O(n).


test: list[int] = [1, 2, 2, 1]
test_k: int = 1
test_out = 4
assert test_out == count_k_difference(test, test_k)

test = [1, 3]
test_k = 3
test_out = 0
assert test_out == count_k_difference(test, test_k)

test = [3, 2, 1, 5, 4]
test_k = 2
test_out = 3
assert test_out == count_k_difference(test, test_k)
