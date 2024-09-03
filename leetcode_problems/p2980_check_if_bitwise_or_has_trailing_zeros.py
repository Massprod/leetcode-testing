# You are given an array of positive integers nums.
# You have to check if it is possible to select two or more elements in the array
#  such that the bitwise OR of the selected elements has at least one trailing zero in its binary representation.
# For example, the binary representation of 5, which is "101", does not have any trailing zeros,
#  whereas the binary representation of 4, which is "100", has two trailing zeros.
# Return true if it is possible to select two or more elements whose bitwise OR has trailing zeros,
#  return false otherwise.
# -------------------------
# 2 <= nums.length <= 100
# 1 <= nums[i] <= 100


def has_trailing_zeros(nums: list[int]) -> bool:
    # working_sol (96.31%, 77.87%) -> (47ms, 16.48mb)  time: O(n) | space: O(1)
    # If we have 2 numbers with `0` LSB.
    # We can use them to get trailing zero.
    count: int = 0
    for num in nums:
        if not (1 & num):
            count += 1
            if 2 <= count:
                return True
    return False


# Time complexity: O(n) <- n - length of the input array `nums`.
# In the worst case last index needs to be used, traversing whole `nums`, once => O(n).
# -------------------------
# Auxiliary space: O(1).
# Only 1 constant INT is used, doesn't depend on input => O(1).


test: list[int] = [1, 2, 3, 4, 5]
test_out: bool = True
assert test_out == has_trailing_zeros(test)

test = [2, 4, 8, 16]
test_out = True
assert test_out == has_trailing_zeros(test)

test = [1, 3, 5, 7, 9]
test_out = False
assert test_out == has_trailing_zeros(test)
