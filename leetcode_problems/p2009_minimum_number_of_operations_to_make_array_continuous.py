# You are given an integer array nums. In one operation, you can replace any element in nums with any integer.
#  nums is considered continuous if both of the following conditions are fulfilled:
#   - All elements in nums are unique.
#   - The difference between the maximum element and the minimum element in nums equals nums.length - 1.
# For example, nums = [4, 2, 5, 3] is continuous, but nums = [1, 2, 3, 5, 6] is not continuous.
# Return the minimum number of operations to make nums continuous.
# -----------------
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 9
from random import randint


def min_operations(nums: list[int]) -> int:
    # working_sol (8.55%, 84.87%) -> (1306ms, 35.1mb)  time: O(n * log n) | space: O(n)
    if len(nums) == 1:
        return 0

    def bs(array: list[int], target: int) -> int:
        """
        Binary search to find index with FIRST higher value.
        """
        left: int = 0
        right: int = len(array) - 1
        while left < right:
            middle: int = (left + right) // 2
            if array[middle] <= target:
                left = middle + 1
            else:
                right = middle
        if array[left] > target:
            return left
        # Nothing higher, we can append.
        else:
            return len(array)

    sort_nums: list[int] = sorted(set(nums))
    min_op: int = len(nums)
    for x in range(len(sort_nums)):
        minimum: int = sort_nums[x]
        # ! The difference between the maximum element
        #   and the minimum element in nums equals (nums.length - 1) !
        maximum: int = minimum + len(nums) - 1
        # Using BS to get index of first_higher value than maximum.
        # And it's first value out of our range [minimum, maximum] inclusive.
        # So everything from x -> bs(maximum) is correct values.
        # And everything else should be changed: len(nums) - correct
        cur_op: int = len(nums) - (bs(sort_nums, maximum) - x)
        min_op = min(min_op, cur_op)

    return min_op


# Time complexity: O(n * log n) -> worst case == no duplicates -> sorting whole input array => O(n * log n) ->
# n - len of input array^^| -> cuz there's no duplicates we will BS in original array, but sorted in ascending,
#                              we repeat first_higher index search for every index => O(n * log n).
# Auxiliary space: O(n) -> same worst case -> we're just recreating original array => O(n).
# -----------------
# Tag: BinarySearch.
# Hints:
# !
# Sort the array.
# For every index do a binary search to get the possible right end
#  of the window and calculate the possible answer.
# !
# So we choose some index from left side and it's value becomes minimum.
# And because we need to build continuous array it's actually array with values inside some range(min, max) inclusive.
# We can decide on what highest can be:
# ! The difference between the maximum element and the minimum element in nums equals nums.length - 1 !
# If we sort it, then we can find something higher than this value on right side.
# And this value-index, should be last point to which we already have continuous array.
# Which gives us correct array we already have, and we need to replace everything else.
# Because best option to minimize operations is to reuse what we already have.
# Extra: ! All elements in nums are unique. !
# Make set() of original?
# len(nums) - len(set(nums)) <- to get diff what should be 100% changed?
# No. Better to just decide on what correct values we already have and take it from all.


test: list[int] = [4, 2, 5, 3]
test_out: int = 0
assert test_out == min_operations(test)

test = [1, 2, 3, 5, 6]
test_out = 1
assert test_out == min_operations(test)

test = [1, 10, 100, 1000]
test_out = 3
assert test_out == min_operations(test)

test = [randint(1, 10 ** 9) for _ in range(10 ** 3)]
print(test)
