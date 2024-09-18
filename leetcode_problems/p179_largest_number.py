# Given a list of non-negative integers nums,
#  arrange them such that they form the largest number and return it.
# Since the result may be very large, so you need to return a string instead of an integer.
# -------------------------
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 10 ** 9
from random import randint


def largest_number(nums: list[int]) -> str:
    # working_sol (92.96%, 32.99%) -> (33ms, 16.66mb)  time: O(n * log n) | space: O(n)
    # Actually, we need to create a sorting function by ourselves.
    # Like merge sort with comparing not just values,
    # but (a + b) >= (b + a)
    # Which is not hard, but no time for this.
    # So, using approach of editorial with `* 10`.
    # Maybe rebuild it later.
    # It's even harder to understand, if I return, it's better to find how it works.
    # Because we're just repeating a string for `10` times, why it gives correct values?
    str_nums: list[str] = [str(num) for num in nums]
    str_nums.sort(reverse=True, key=lambda x: x * 10)
    if '0' == str_nums[0]:
        return str_nums[0]
    return ''.join(str_nums)


# Time complexity: O((n * k) * log (n * k)) <- n - length of the input array `nums`, k - average digits in `num`s
# We're creating an array with all numbers in `str` format with all `digits `used => O(n * k).
# Sorting it with built-in `sort` => O(n * k + (n * k) * log (n * k))
# -------------------------
# Auxiliary space: O(n * k)
# `str_nums` <- allocates space for `n` string of `k` size on average => O(n * k).
# `sort` <- takes the same space => O(2 * (n * k)).


test: list[int] = [10, 2]
test_out: str = "210"
assert test_out == largest_number(test)

test = [3, 30, 34, 5, 9]
test_out = "9534330"
assert test_out == largest_number(test)

test = [randint(0, 10 ** 9) for _ in range(100)]
print(test)
