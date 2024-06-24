# Given an array of integers nums and an integer limit,
#  return the size of the longest non-empty subarray such that
#  the absolute difference between any two elements of this subarray is less than or equal to limit.
# ----------------------
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 9
# 0 <= limit <= 10 ** 9
from collections import deque
from random import randint


def longest_subarray(nums: list[int], limit: int) -> int:
    # working_sol (37.72%, 17.14%) -> (492ms, 34.3mb)  time: O(n) | space: O(n)
    # [value, index] - monoStack in ascending for minimum values
    mins: deque[tuple[int, int]] = deque([])
    # [value, index] - monoStack in descending for maximum values
    maxs: deque[tuple[int, int]] = deque([])
    out: int = 0
    left_l: int = 0
    for index, num in enumerate(nums):
        while mins and mins[-1][0] > num:
            mins.pop()
        mins.append((num, index))
        while maxs and maxs[-1][0] < num:
            maxs.pop()
        maxs.append((num, index))
        # ! absolute difference between any two elements of this subarray is less than or equal to limit !
        # If we can have absolute difference between Maximum and Minimum of the current Window.
        # Everything else will be fine as well.
        while maxs and mins and abs(mins[0][0] - maxs[0][0]) > limit:
            left_l += 1
            # Shrinking window, so if we have values with lower indexes => delete them.
            while mins and mins[0][1] < left_l:
                mins.popleft()
            while maxs and maxs[0][1] < left_l:
                maxs.popleft()
        out = max(out, (index - left_l) + 1)
    return out


# Time complexity: O(n) <- n - length of the input array `nums`
# Always traversing all the input array `nums`, once => O(n).
# And if we have every window diff > limit, we will use every index of the array for deletion as well => O(2n).
# ----------------------
# Auxiliary space: O(n)
# In the worst case, we're going to have `limit` which allows us to use whole array `nums`
#  in ascending or descending order and `maxs` or `mins` will be a size of `nums` => O(n).


test: list[int] = [8, 2, 4, 7]
test_limit: int = 4
test_out: int = 2
assert test_out == longest_subarray(test, test_limit)

test = [10, 1, 2, 4, 7, 2]
test_limit = 5
test_out = 4
assert test_out == longest_subarray(test, test_limit)

test = [4, 2, 2, 2, 4, 4, 2, 2]
test_limit = 0
test_out = 3
assert test_out == longest_subarray(test, test_limit)

test = [randint(1, 10 ** 9) for _ in range(10 ** 2)]
test_limit = randint(0, 10 ** 9)
print(test, '\n\n', test_limit)
