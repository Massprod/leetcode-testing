# You are given an integer array nums and an integer k.
# You can perform the following operation any number of times:
#  - Select an index i and replace nums[i] with nums[i] - 1.
# Return the minimum number of operations required to make
#  the sum of the array divisible by k.
# ------------------------
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 1000
# 1 <= k <= 100


def min_operations(nums: list[int], k: int) -> int:
    # working_sol (100%, 54.87%) -> (0ms, 17.92mb)  time: O(n) | space: O(1)
    # W.e the value we change.
    # All we do is taking `-1` from the sum.
    # So, it's just == sum % k.
    return sum(nums) % k


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing every index of the input array `nums`, once => O(n).
# ------------------------
# Auxiliary space: O(1).


test: list[int] = [3, 9, 7]
test_k: int = 5
test_out: int = 4
assert test_out == min_operations(test, test_k)

test = [4, 1, 3]
test_k = 4
test_out = 0
assert test_out == min_operations(test, test_k)

test = [3, 2]
test_k = 6
test_out = 5
assert test_out == min_operations(test, test_k)
