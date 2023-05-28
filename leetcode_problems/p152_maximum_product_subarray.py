# Given an integer array nums, find a subarray that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.
# -------------------
# 1 <= nums.length <= 2 * 104  ,  -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


def max_product(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    max_val: int = nums[0]
    for x in range(len(nums)):
        prod: int = nums[x]
        max_val = max(max_val, nums[x])
        for y in range(x + 1, len(nums)):
            prod = prod * nums[y]
            max_val = max(max_val, prod)
            if max_val >= (2 ** 31 - 1) or max_val <= -(2 ** 31):
                return max_val
        prod = nums[x]
        for z in range(x - 1, -1, -1):
            prod = prod * nums[z]
            max_val = max(max_val, prod)
            if max_val >= (2 ** 31 - 1) or max_val <= -(2 ** 31):
                return max_val
    return max_val


# Ok. Another possible cull, skip 1 and -1, but take in consideration that -1 can make
# from -high_product -> + high_product -> and skip 1, because we're already walk through whole right_left sides.
# How?
# -------------------
# 186/190 - passed, last one is time_gates as always,
# And I don't think we can sort like I was thinking, because we're obliged to find SUBARRAY,
# but after sorting we're not having any order to see what is SUBARRAY or just random values,
# how can we cull duplicates?
# !
# The test cases are generated so that the answer will fit in a 32-bit integer. !
# Ok, if we find any values equal or lower, insta return.
# -------------------
# Maybe sorting? Well it could cull everything, because we're just going to calculate
# values from negative, starting from some index which will give us EVEN number of negative,
# like: [-100, -50, -25, -10, 1, 50, 60, 70, 80, 90]
# all we need after sorting is take [0] -> [3] => giving us positive product with the highest values,
# and multiply one by one [1, 50, 60, 70, 80, 90] => most highest value.
# If we're allowing to do this it might be working solution, because I doubt it can pass with just O(n * (n + n).
# But let's fail first.
# -------------------
# !
# A subarray is a contiguous non-empty sequence of elements within an array. !
# Don't know how to make it faster than O(n * (n + n)) at least for now, and I didn't know what time_limit is.
# Let's first try to make it like this and after hitting limit change,
# because I don't see any ways to skip calculations.
# We should always go from index and check every side of it, from 0 - index, and index - end.
# Always compare it to current max, and just return this max. Like I see it for now.


test1 = [2, 3, -2, 4]
test1_out = 6
print(max_product(test1))
assert test1_out == max_product(test1)

test2 = [-2, 0, -1]
test2_out = 0
print(max_product(test2))
assert test2_out == max_product(test2)

test3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test3_out = 3628800
print(max_product(test3))
assert test3_out == max_product(test3)
