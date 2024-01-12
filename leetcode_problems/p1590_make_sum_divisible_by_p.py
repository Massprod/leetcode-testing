# Given an array of positive integers nums,
#  remove the smallest subarray (possibly empty) such that the sum of the remaining elements
#  is divisible by p.
# It is not allowed to remove the whole array.
# Return the length of the smallest subarray that you need to remove,
#  or -1 if it's impossible.
# A subarray is defined as a contiguous block of elements in the array.
# ------------------
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 9
# 1 <= p <= 10 ** 9
from random import randint


def min_subarray(nums: list[int], p: int) -> int:
    # working_sol (85.56%, 53.61%) -> (407ms, 35.70mb)  time: O(n) | space: O(n)
    # F - prefixes array.
    # F[i] - prefix sum for i.
    # F[j<i] - prefix sum for j, where j < i.
    # (F[i] - F[j<i]) % p = sum(nums) % p, we need to satisfy this
    # F[j<i] % p = (F[i] - sum(nums)) % p, we need to find this
    cur_sum: int = sum(nums)
    # We can't make smaller, correctly divisible by `p`.
    if cur_sum < p:
        return -1
    # Already divisible by `p`.
    if 0 == cur_sum % p:
        return 0
    prefix: int = 0
    # {F[i] % p, for subarray with prefix == F[i]: rightmost index of this subarray}
    subs: dict[int, int] = {0: 0}
    out: int = len(nums)
    for index, val in enumerate(nums):
        # F[i]
        prefix += val
        # F[j<i] % p = (F[i] - sum(nums)) % p
        sub: int = (prefix - cur_sum) % p
        # We need some subarray F[j] for which j < i, and
        # (F[i] - F[j<i]) % p == sum(nums) % p
        if sub in subs:
            # what_we_need: int = cur_sum % p
            # print('We need:', what_we_need, 'sum(nums)')
            # print('Current: F[i] ==', prefix, 'Previous: F[j<i] ==', sub)
            # what_we_search: int = (prefix - sub) % p
            # print('We get: (F[i] - F[j<i]) % p ==', what_we_search)
            # assert what_we_search == what_we_need
            # (i + 1 - j + 1) == subarray length.
            out = min(out, (index + 1 - subs[sub]))
        subs[prefix % p] = index + 1  # +1 for 0-indexed.
    return out if out < len(nums) else -1


# Time complexity: O(n) <- n - length of input array `nums`.
# We only traverse input array `nums`, once => O(n).
# ------------------
# Auxiliary space: O(n)
# Worst case: every (prefix % p) will give unique value.
# So, dict `subs` will store all of them => O(n).


test: list[int] = [3, 1, 4, 2]
test_p: int = 6
test_out: int = 1
assert test_out == min_subarray(test, test_p)

test = [6, 3, 5, 2]
test_p = 9
test_out = 2
assert test_out == min_subarray(test, test_p)

test = [1, 2, 3]
test_p = 3
test_out = 0
assert test_out == min_subarray(test, test_p)

test = [4, 5, 8, 5, 4]
test_p = 7
test_out = 1
assert test_out == min_subarray(test, test_p)

test = [8, 32, 31, 18, 34, 20, 21, 13, 1, 27, 23, 22, 11, 15, 30, 4, 2]
test_p = 148
test_out = 7
assert test_out == min_subarray(test, test_p)

test = [randint(1, 10 ** 9) for _ in range(10 ** 2)]
test_p = randint(1, 10 ** 9)
print(f'{test}\n\n{test_p}')
