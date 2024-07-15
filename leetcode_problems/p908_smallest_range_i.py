# You are given an integer array nums and an integer k.
# In one operation, you can choose any index i where 0 <= i < nums.length
#  and change nums[i] to nums[i] + x where x is an integer from the range [-k, k].
# You can apply this operation at most once for each index i.
# The score of nums is the difference between the maximum and minimum elements in nums.
# Return the minimum score of nums
#  after applying the mentioned operation at most once for each index in it.
# ------------------------
# 1 <= nums.length <= 10 ** 4
# 0 <= nums[i] <= 10 ** 4
# 0 <= k <= 10 ** 4
from random import randint


def smallest_range(nums: list[int], k: int) -> int:
    # working_sol (24.39%, 51.48%) -> (103ms, 17.75mb)  time: O(n) | space: O(1)
    # Essentially, all we care is to take -k from max value
    #  and add +k to the lowest.
    # Because, w.e other values might be, we can adjust them to these values.
    # And it's a maximum possible change of range to the lower distance between them.
    min_val: int = 10 ** 5
    max_val: int = 0
    for num in nums:
        min_val = min(min_val, num)
        max_val = max(max_val, num)
    max_val += k * -1
    min_val += k
    # We can either, adjust them to be equal, or just make the distance as small as possible.
    return max_val - min_val if min_val < max_val else 0


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing the input array `nums`, once => O(n).
# ------------------------
# Auxiliary space: O(1)
# Only 2 constant INT's used, none of them depends on input => O(1).


test: list[int] = [1]
test_k: int = 0
test_out: int = 0
assert test_out == smallest_range(test, test_k)

test = [0, 10]
test_k = 2
test_out = 6
assert test_out == smallest_range(test, test_k)

test = [1, 3, 6]
test_k = 3
test_out = 0
assert test_out == smallest_range(test, test_k)

test = [randint(0, 10 ** 4) for _ in range(10 ** 4)]
print(test)
