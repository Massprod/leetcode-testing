# The frequency of an element is the number of times it occurs in an array.
# You are given an integer array nums and an integer k.
# In one operation, you can choose an index of nums and increment the element at that index by 1.
# Return the maximum possible frequency of an element after performing at most k operations.
# ----------------
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 5
# 1 <= k <= 10 ** 5
from random import randint


def max_frequency(nums: list[int], k: int) -> int:
    # working_sol (64.61%, 55.16%) -> (1153ms, 31.2mb)  time: O(n * log n) | space: O(n)
    # We can do this with (dict + heapq) instead of sorting, but it's slower.
    # And I don't see how else it can be done without sorting.
    nums.sort()
    cur_ops: int = 0
    # Standard sliding window.
    left_l: int = 0
    right_l: int = 0
    max_freq: int = 1
    while right_l < len(nums) - 1:
        right_l += 1
        # Going left -> right. For every higher value, we increment previous values to this new value.
        # And because we're already having all previous values set correctly, we can just multiply them.
        # Like: [1, 2, 3] -> 1 * 1 -> [2, 2, 3] -> 1 * 2 -> [3, 3, 3]. `right_l` <- not included in incrementing.
        cur_ops += (nums[right_l] - nums[right_l - 1]) * (right_l - left_l)
        while cur_ops > k:
            # Shrink window by taking out first value of the sequence.
            # We're always incrementing everything to current highest.
            # So, HIGHEST - FIRST == # of increments we did on that value.
            cur_ops -= nums[right_l] - nums[left_l]
            left_l += 1
        # +1 for 0-indexed.
        max_freq = max(max_freq, right_l - left_l + 1)
    return max_freq


# Time complexity: O(n * log n) -> built_in sorting => O(n * log n) -> extra traverse of the whole array in worst case
# n - length of input array 'nums'^^|  with k == 1, every index will be used twice == add in window + remove => O(2n).
# Auxiliary space: O(n) -> built_in sorting => O(n) -> 4 extra constant INT's none of them depends on input.
# ----------------
# With sorting, it's easy, but without?
# Can't find any solution without sorting and some1 even comments it's impossible.
# Well I know how we can do this with (heapq + dictionary), but it's going to be slower than sorting.
# Because we will always recheck lower values, and heapq operations are slow.
# So, I will just stick to sort + window.


test: list[int] = [1, 2, 4]
test_k: int = 5
test_out: int = 3
assert test_out == max_frequency(test, test_k)

test = [1, 4, 8, 13]
test_k = 5
test_out = 2
assert test_out == max_frequency(test, test_k)

test = [3, 9, 6]
test_k = 2
test_out = 1
assert test_out == max_frequency(test, test_k)

test = [randint(1, 10 ** 5) for _ in range(10 ** 4)]
# print(test)
