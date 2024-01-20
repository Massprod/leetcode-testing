# Given an integer array nums, handle multiple queries of the following type:
#  - Calculate the sum of the elements of nums between indices left and right inclusive
#   where left <= right.
# Implement the NumArray class:
#  - NumArray(int[] nums) Initializes the object with the integer array nums.
#  - int sumRange(int left, int right) Returns the sum of the elements of nums between
#     indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
# ----------------------
# 1 <= nums.length <= 10 ** 4
# -10 ** 5 <= nums[i] <= 10 ** 5
# 0 <= left <= right < nums.length
# At most 10 ** 4 calls will be made to sumRange.


class NumArray:
    # working_sol (96.27%, 77.54%) -> (63ms, 20.1mb)  time: O(n) | space: O(n)
    def __init__(self, nums: list[int]):
        # Start with 0 as prefix of [0], and we need to include prefix of last index.
        self.prefixes: list[int] = [0]
        prefix: int = 0
        for num in nums:
            prefix += num
            self.prefixes.append(prefix)

    def sumRange(self, left: int, right: int) -> int:
        # We need to include right, so it's prefix of (right + 1).
        # And exclude everything before left.
        return self.prefixes[right + 1] - self.prefixes[left]


# Time complexity: O(n) <- for initiation of object, and O(1) for `sumRange`.
# Auxiliary space: O(n) same.
