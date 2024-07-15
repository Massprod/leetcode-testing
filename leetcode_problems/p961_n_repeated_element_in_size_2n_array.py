# You are given an integer array nums with the following properties:
#  - nums.length == 2 * n.
#  - nums contains n + 1 unique elements.
#  - Exactly one element of nums is repeated n times.
# Return the element that is repeated n times.
# --------------------
# 2 <= n <= 5000
# nums.length == 2 * n
# 0 <= nums[i] <= 10 ** 4
# nums contains n + 1 unique elements and one of them is repeated exactly n times.
from collections import defaultdict


def repeated_n_times(nums: list[int]) -> int:
    # working_sol (40.39%, 79.84%) -> (171ms, 17.85mb)  time: O(n) | space: O(n // 2 + 1)
    # Boyer-Moore Voting Algorithm.
    # Can be used only for elements that appear `more than half the time`.
    # And we need only the half-time, so we need to use HashTable.
    # { values: occurrences }
    occurs: dict[int, int] = defaultdict(int)
    for num in nums:
        occurs[num] += 1
    # ! nums.length == 2 * n. !
    target: int = len(nums) // 2
    for val, occurs in occurs.items():
        # ! Exactly one element of nums is repeated n times !
        if target == occurs:
            return val


# Time complexity: O(n) <- n - length of the input array `nums`.
# We're always traversing `nums` once to get all the values and their occurrences => O(n).
# Extra traversing (n // 2 + 1) unique elements => O(n + (n // 2 + 1)).
# --------------------
# Auxiliary space: O(n // 2 + 1)
# !
# - nums.length == 2 * n.
# - nums contains n + 1 unique elements.
# !


test: list[int] = [1, 2, 3, 3]
test_out: int = 3
assert test_out == repeated_n_times(test)

test = [2, 1, 2, 5, 3, 2]
test_out = 2
assert test_out == repeated_n_times(test)

test = [5, 1, 5, 2, 5, 3, 5, 4]
test_out = 5
assert test_out == repeated_n_times(test)
