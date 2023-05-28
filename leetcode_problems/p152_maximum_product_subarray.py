# Given an integer array nums, find a subarray that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.
# -------------------
# 1 <= nums.length <= 2 * 104  ,  -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


def max_product(nums: list[int]) -> int:
    # working_sol (5.15%, 13.72%) -> (113ms, 16.9mb)  time: O(n * ((n - i) + (0 + i)) | space: O(1)
    if len(nums) == 1:
        return nums[0]
    max_val: int = nums[0]
    prod: int = max_val
    negative_used: bool = False
    for x in range(len(nums)):
        if nums[x] == 1:
            if prod <= 0:
                prod = 1
                max_val = max(max_val, prod)
            continue
        if nums[x] == -1 and prod < 0 and x != 0 and not negative_used:
            prod = prod * -1
            max_val = max(max_val, prod)
            negative_used = True
            continue
        if nums[x] == -1 and negative_used:
            continue
        if nums[x] == -1 and prod > 0:
            continue
        if nums[x] == 0:
            prod = 0
            max_val = max(max_val, prod)
            continue
        prod = nums[x]
        max_val = max(max_val, nums[x])
        negative_used = False
        for y in range(x + 1, len(nums)):
            if nums[y] == 1:
                continue
            prod = prod * nums[y]
            max_val = max(max_val, prod)
            if nums[y] == 0:
                break
            if max_val >= (2 ** 31 - 1):
                return max_val
        prod = nums[x]
        for z in range(x - 1, -1, -1):
            if nums[z] == 1:
                continue
            prod = prod * nums[z]
            max_val = max(max_val, prod)
            if nums[z] == 0:
                break
            if max_val >= (2 ** 31 - 1):
                return max_val
    return max_val


# Time complexity: O(n * ((n - i) + (0 + i)) -> traversing whole input list once => O(n) ->
# n - len of input_list^^ -> for every index on this traversing_way
# i - current index^^        we're checking left(0 + i) and right(n - i) sides of the index
#                            in the worst case, we're having values not equal to 0, 1, -1
#                            than we're checking every index on both sides without breaking => O((n - i) + (0 + i)).
#                  Ω(1) -> best case, we're having 1 value in input_list, and it's equal to (2 ** 31 - 1).
#                  Θ(log n * (log(n - 1) + log(0 + i))) ->
#                  -> part of the input_list will be 0, or 1, or -1 after negative_used
#                     and only part of the input_list and left, right slices going to be checked.
# Space complexity: O(1) -> only 3 extra constants used, and number of constants doesn't depend on input_list => O(1)
# -------------------
# Not bad actual results with my solution, without any extra info via Google or something.
# Median time is like 97ms, and mine is 113.
# -------------------
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
# Ok, if we find any values equal or higher than (2 ** 31 -1), insta return. <- 32 bit positive limit_value
# -------------------
# Maybe sorting? Well it could cull everything, because we're just going to calculate
# values from negative, starting from some index which will give us EVEN number of negative,
# like: [-100, -50, -25, -10, 1, 50, 60, 70, 80, 90]
# all we need after sorting is take [0] -> [3] => giving us positive product with the highest values,
# and multiply one by one [1, 50, 60, 70, 80, 90] => most highest value.
# If we're allowing to do this it might be working solution,
# because I doubt it can pass with just O(n * (log n + log n).
# But let's fail first.
# -------------------
# !
# A subarray is a contiguous non-empty sequence of elements within an array. !
# Don't know how to make it faster than O(n * (log n + log n)) at least for now,
# and I didn't know what time_limit is.
# Let's first try to make it like this and after hitting limit change,
# because I don't see any ways to skip calculations.
# We should always go from index and check every side of it, from 0 <- index, and index -> end.
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

# part of time_limit, whole is x10
test4 = [-5, 2, 4, 1, -2, 2, -6, 3, -1, -1, -1, -2, -3, 5, 1, -3, -4, 2, -4, 6, -1, 5, -6, 1, -1, -1, 1, 1, -1, 1, 1,
         -1, -1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1,
         1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, -1, -1, 1, 1, 1]
print(max_product(test4))

# test5 - failed -> I made IF for the case with prod == 0, but if it was lower than 0 -> 1 is still higher and I should
#                   made prod == 1 in this case, changed for IF prod <= 0.
test5 = [-2, 1, 0]
test5_out = 1
print(max_product(test5))
assert test5_out == max_product(test5)

test6 = [3, -1, 4]
test6_out = 4
print(max_product(test6))
assert test6_out == max_product(test6)
