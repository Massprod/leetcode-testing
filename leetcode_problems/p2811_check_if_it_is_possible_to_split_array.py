# You are given an array nums of length n and an integer m.
# You need to determine if it is possible to split the array into n non-empty arrays
#  by performing a series of steps.
# In each step, you can select an existing array (which may be the result of previous steps)
#  with a length of at least two and split it into two subarrays,
#  if, for each resulting subarray, at least one of the following holds:
#    - The length of the subarray is one, or
#    - The sum of elements of the subarray is greater than or equal to m.
# Return true if you can split the given array into n arrays, otherwise return false.
# Note: A subarray is a contiguous non-empty sequence of elements within an array.
# -----------------------
# 1 <= n == nums.length <= 100
# 1 <= nums[i] <= 100
# 1 <= m <= 200
from random import randint


def can_split_array(nums: list[int], m: int) -> bool:
    # working_sol (77.82%, 80.27%) -> (53ms, 16.24mb)  time: O(n) | space: O(1)
    # 2 can be split to 1, 1 <- n == 2
    # 1 is already 1 == n.
    if len(nums) <= 2:
        return True
    # Otherwise we can take 1 element at a time,
    #  until there's some PAIR of indexes which gives m.
    # When only this pair left, we can just cut it in half.
    pair: bool = False
    for x in range(1, len(nums)):
        if (nums[x] + nums[x - 1]) >= m:
            pair = True
            break
    return pair


# Time complexity: O(n) -> worst case, pair is last indexes, so we will traverse full input_array => O(n).
# n - len of input_array^^|
# Auxiliary space: O(1) -> only 1 extra constant BOOLEAN used => O(1).
# -----------------------
# Ok. It's actually simplier than expected. Cuz we can always take split by One index, no matter what.
# And we can take it until there's some PAIR of indexes presented which gives SUM >= m.
# So we will take everything from it, except this pair, and then cut this pair in half.
# -----------------------
# Constraints are low, so it should be fine to check every possible subarray.
# Working with random test_cases, no idea about tricky parts. Let's fail.
# Ok. TLE with recursion, rebuild.


test: list[int] = [2, 2, 1]
test_m: int = 4
test_out: bool = True
assert test_out == can_split_array(test, test_m)

test = [2, 1, 3]
test_m = 5
test_out = False
assert test_out == can_split_array(test, test_m)

test = [2, 3, 3, 2, 3]
test_m = 6
test_out = True
assert test_out == can_split_array(test, test_m)

test = [1, 1]
test_m = 3
test_out = True
assert test_out == can_split_array(test, test_m)

test = []
for _ in range(100):
    test.append(randint(1, 100))
test_m = randint(1, 200)
print(test)
print('---------')
print(test_m)
