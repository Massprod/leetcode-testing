# The pair sum of a pair (a,b) is equal to a + b.
# The maximum pair sum is the largest pair sum in a list of pairs.
#  - For example, if we have pairs (1,5), (2,3), and (4,4),
#     the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
# Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:
#  - Each element of nums is in exactly one pair, and
#  - The maximum pair sum is minimized.
# Return the minimized maximum pair sum after optimally pairing up the elements.
# ------------------------
# n == nums.length
# 2 <= n <= 10 ** 5
# n is even.
# 1 <= nums[i] <= 10 ** 5
from random import randint


def min_pair_sum(nums: list[int]) -> int:
    # working_sol (85.09%, 29.82%) -> (966ms, 30.7mb)  time: O(n * log n) | space: O(n)
    # ! Each element of nums is in exactly one pair !
    # First, we can use duplicates ELEMENT in this case is just an INDEX.
    # Second, we need to use EVERYTHING.
    # ! The maximum pair sum is minimized !
    # For this we can always use HIGHEST + LOWEST options from current elements left in the array.
    # Because if we don't use LOWEST + HIGHEST, we will still need to use them later.
    # And it will lead us to use of something HIGHER than our current LOWEST.
    # So, the best option it's just use LOWEST + HIGHEST at every iteration.
    #  (deleting this options == not using them again in our case)
    nums.sort()
    max_sum: int = 0
    ind_1: int = 0
    ind_2: int = len(nums) - 1
    while ind_1 < ind_2:
        max_sum = max(max_sum, nums[ind_1] + nums[ind_2])
        ind_1 += 1
        ind_2 -= 1
    return max_sum


# Time complexity: O(n * log n) -> sorting with builtin => O(n * log n) -> extra use of every index, once => O(n).
# n - len of input array 'nums'^^|
# Auxiliary space: O(n) -> sorting with builtin => O(n) -> 3 constant INTs, none of them depends on input => O(1).
# ------------------------
# By the look of test cases it's like simple take minimum + maximum from current array and choose max of it.
# But is it correct? And can we use duplicates?
# Like -> ! Each element of nums is in exactly one pair !
# Tested with [1, 2, 4, 4] and answer == 6, so we can use duplicates.
# Which means we just need to use ELEMENT like INDEX not unique number.
# Well I guess it's because we're always choosing the smallest value in the array we can,
#  in pair with maximum value we can. Which is actually the lowest PAIR possible to build.
# Because everything after lowest is HIGHER. But why highest?
# Because -> ! Each element of nums is in exactly one pair ! <- we can't skip values.
# And if we skip highest, then we will still need to use it, and it will be used with something HIGHER.
# In which case it will become even higher than value we get with smallest.
# And because we're doing this on every part of the array left, after using 2 elements.
# We're always choosing optimal pair.
# Should be correct.


test: list[int] = [3, 5, 2, 3]
test_out: int = 7
assert test_out == min_pair_sum(test)

test = [3, 5, 4, 2, 4, 6]
test_out = 8
assert test_out == min_pair_sum(test)

test = [1, 2, 4, 4]
test_out = 6
assert test_out == min_pair_sum(test)

test = [randint(1, 10 ** 5) for _ in range(10 ** 4)]
print(test)
