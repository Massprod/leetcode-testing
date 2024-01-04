# Given a 0-indexed integer array nums of length n and an integer k,
#  return the number of pairs (i, j) such that:
#   - 0 <= i < j <= n - 1 and
#   - nums[i] * nums[j] is divisible by k.
# ---------------
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i], k <= 10 ** 5
from random import randint
from collections import Counter


def count_pairs(nums: list[int], k: int) -> int:
    # working_sol (87.8%, 14.83%) -> (581ms, 31.3mb)  time: O(n * log(min(val, k)) + k) | space: O(sqrt(k))

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    # gcd(a, k) * gcd(b, k) % k == 0
    out: int = 0
    # {gcd: # of values with same gcd}
    all_gcds: dict[int, int] = Counter(gcd(k, val) for val in nums)
    for f_gcd, f_occurs in all_gcds.items():
        for s_gcd, s_occurs in all_gcds.items():
            if f_gcd <= s_gcd and 0 == (f_gcd * s_gcd) % k:
                # Same gcd == we can use only half, to pair them.
                if f_gcd == s_gcd:
                    out += f_occurs * (s_occurs - 1) // 2
                else:
                    out += f_occurs * s_occurs
    return out


# Time complexity: O(n * log(min(val, k)) + k) <- n - length of input array `nums`, val - current value of `nums`.
# We traverse whole input array `nums` and calc gdc() for every value => O(n * log(min(val, k)).
# We taking gcd() for every (k, value) pairs, and the number of factors of 'k' will not be above 2 * sqrt(k).
# So, we will have `all_gcds` with (2 * sqrt(k)) keys in the worst case, nested loop => O(4 * sqrt(k) * sqrt(k)).
# Which should be correct to say O(k), because (sqrt(k) * sqrt(k) == k).
# ---------------
# Auxiliary space: O(sqrt(k)).
# In the worst case number of factors of 'k' == (2 * sqrt(k)), `all_gcds` will store all of them => O(2 * sqrt(k)).
# ---------------
# gcd(a, k) * gcd(b, k) % k == 0.
# If it's correct then it's correct pair of (a, b) values.
# We don't care about placement: ! 0 <= i < j <= n - 1 !
# Because we can use any index as 'j' or 'i', when multiplying them.
# So, we need to check only this rule for all values in `nums`.


test: list[int] = [1, 2, 3, 4, 5]
test_k: int = 2
test_out: int = 7
assert test_out == count_pairs(test, test_k)

test = [1, 2, 3, 4]
test_k = 5
test_out = 0
assert test_out == count_pairs(test, test_k)

test = [randint(1, 10 ** 5) for _ in range(10 ** 5)]
print(test)
