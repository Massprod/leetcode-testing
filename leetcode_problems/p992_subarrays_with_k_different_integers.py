# Given an integer array nums and an integer k, return the number of good subarrays of nums.
# A good array is an array where the number of different integers in that array is exactly k.
# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.
# ------------------
# 1 <= nums.length <= 2 * 10 ** 4
# 1 <= nums[i], k <= nums.length
from random import randint
from collections import defaultdict


def sub_arrays_with_k_diff(nums: list[int], k: int) -> int:
    # working_sol (92.78%, 59.53) -> (288ms, 19.97mb)  time: O(n) | space: O(n)
    out: int = 0
    # {value: occurrences}
    diffs: dict[int, int] = defaultdict(int)
    left_l: int = 0
    right_l: int = 0
    # Current # of correct subs with k == diff_ints.
    cur_cor_subs: int = 0
    # Every currently correct subarray we have will give us
    # `cur_cor_subs` correct sub arrays and +1 for every `right_l` step we take.
    # Because, every `right_l` step with correct len(diffs) gives us:
    #  1 new big sub_array + every previous sub_array == `cur_cor_subs` can be expended
    #  to include this new value.
    # And this correct subs will be annulled only when we exceed len(diffs) > k.
    while right_l < len(nums):
        diffs[nums[right_l]] += 1
        if len(diffs) > k:
            diffs[nums[left_l]] -= 1
            if not diffs[nums[left_l]]:
                diffs.pop(nums[left_l])
            left_l += 1
            cur_cor_subs = 0
        if len(diffs) == k:
            # Shift `left_l` to get a number of correctly set sub arrays, at this moment.
            while diffs[nums[left_l]] > 1:
                diffs[nums[left_l]] -= 1
                left_l += 1
                cur_cor_subs += 1
            out += cur_cor_subs + 1
        right_l += 1
    return out

# Time complexity: O(n) <- n - length of input array `nums`.
# Standard sliding window with maximum usage of every index Twice => O(2n).
# ------------------
# Auxiliary space: O(n)
# Worst case: we will have every value in `nums` unique.
# All of them will be stored in dict `diffs` => O(n).


test: list[int] = [1, 2, 1, 2, 3]
test_k: int = 2
test_out: int = 7
assert test_out == sub_arrays_with_k_diff(test, test_k)

test = [1, 2, 1, 3, 4]
test_k = 3
test_out = 3
assert test_out == sub_arrays_with_k_diff(test, test_k)

test = [randint(1, 2 * 10 ** 4) for _ in range(10 ** 4)]
print(test)
