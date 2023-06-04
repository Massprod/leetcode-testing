# There is a function signFunc(x) that returns:
#   1 if x is positive.
#   -1 if x is negative.
#   0 if x is equal to 0.
# You are given an integer array nums. Let product be the product of all values in the array nums.
# Return signFunc(product).
# ----------------------------
# 1 <= nums.length <= 1000  ,  -100 <= nums[i] <= 100


def array_sign(nums: list[int]) -> int:
    # working_sol (80.22%, 45.83%) -> (70ms, 16.5mb)  time: O(n) | space: O(1)
    negative: bool = False
    for num in nums:
        if num == 0:
            return 0
        if num < 0:
            negative = not negative
    if negative:
        return -1
    return 1


# Time complexity: O(n) -> traversing whole input_list once => O(n)
# n - len of input_list^^|
# Auxiliary space: O(1) -> only 1 constant doesn't depend on input => O(1)


test1 = [-1, -2, -3, -4, 3, 2, 1]
test1_out = 1
print(array_sign(test1))
assert test1_out == array_sign(test1)

test2 = [1, 5, 0, 2, -3]
test2_out = 0
print(array_sign(test2))
assert test2_out == array_sign(test2)

test3 = [-1, 1, -1, 1, -1]
test3_out = -1
print(array_sign(test3))
assert test3_out == array_sign(test3)
