# You are given an array nums of non-negative integers.
# nums is considered special if there exists a number x such
#   that there are exactly x numbers in nums that are greater than or equal to x.
# Notice that x does not have to be an element in nums.
# Return x if the array is special, otherwise, return -1.
# It can be proven that if nums is special, the value for x is unique.
# ------------------
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000
from random import randint


def special_array(nums: list[int]) -> int:
    # working_sol (82.72%, 48.53%) -> (36ms, 16.56mb)  time: O(n * log n) | space: O(n)
    nums.sort()

    def bs(value: int) -> int:
        left_l: int = 0
        right_l: int = len(nums) - 1
        index: int = -1
        while left_l <= right_l:
            middle: int = (left_l + right_l) // 2
            # We need a first index which is lower than our `value`.
            # Then, we can say that everything on the right side of it is higher than our `value`.
            if nums[middle] >= value:
                index: int = middle
                right_l = middle - 1
            else:
                left_l = middle + 1
        return index

    for val in range(1, len(nums) + 1):
        _index: int = bs(val)
        # ! x numbers in nums that are greater than or equal to x !
        # val == x == (len(nums) - _index).
        if val == (len(nums) - _index):
            return val
    return -1


# Time complexity: O(n * log n) <- n - length of input array `nums`.
# First, we're sorting our input array with standard `sort()` => O(n * log n).
# Second, for every value in range 1 -> len(nums) !inclusive!, we're doing BinarySearch to get the index
#  from which every value is higher than his value => O(n * log n).
# ------------------
# Auxiliary space: O(n)
# Standard `sort()` always takes O(n), and our BinarySearch is constant => O(n).


test: list[int] = [3, 5]
test_out: int = 2
assert test_out == special_array(test)

test = [0, 0]
test_out = -1
assert test_out == special_array(test)

test = [0, 4, 3, 0, 4]
test_out = 3
assert test_out == special_array(test)

test = [randint(0, 1000) for _ in range(100)]
print(test)
