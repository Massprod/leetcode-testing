# You are given a 0-indexed integer array nums.
# Rearrange the values of nums according to the following rules:
# 1. Sort the values at odd indices of nums in non-increasing order.
#   - For example, if nums = [4,1,2,3] before this step, it becomes [4,3,2,1] after.
#     The values at odd indices 1 and 3 are sorted in non-increasing order.
# 2. Sort the values at even indices of nums in non-decreasing order.
#   - For example, if nums = [4,1,2,3] before this step, it becomes [2,1,4,3] after.
#     The values at even indices 0 and 2 are sorted in non-decreasing order.
# Return the array formed after rearranging the values of nums.
# ---------------------
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100


def sort_even_odd(nums: list[int]) -> list[int]:
    # working_sol (50.92%, 57.24%) -> (52ms, 16.60mb)  time: O(n * log n) | space: O(n)
    enumerated: list[tuple[int, int]] = list(enumerate(nums))
    odd: list[int] = [
        value for index, value in enumerated if index % 2
    ]
    even: list[int] = [
        value for index, value in enumerated if not index % 2
    ]
    odd.sort(reverse=True)
    even.sort()
    out: list[int] = []
    # If there's `even` elements => last index == odd
    # Otherwise => last index == even
    start: bool = False
    if len(nums) % 2:
        start = True
    while odd or even:
        if start:
            if even:
                out.append(even.pop())
            if odd:
                out.append(odd.pop())
        else:
            if odd:
                out.append(odd.pop())
            if even:
                out.append(even.pop())
    return out[::-1]


# Time complexity: O(n * log n) <- n - length of the input array `nums`.
# Essentially, we're always sorting all values from `nums` => O(n * log n).
# And extra traversing them, twice => O(n * log n + 2 * n).
# ---------------------
# Auxiliary space: O(n)
# In the worst case there's only even index == 0.
# `sort` will use it, and we will store it in `odd` => O(n).


test: list[int] = [4, 1, 2, 3]
test_out: list[int] = [2, 3, 4, 1]
assert test_out == sort_even_odd(test)

test = [2, 1]
test_out = [2, 1]
assert test_out == sort_even_odd(test)
