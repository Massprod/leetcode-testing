# Given an integer array nums where nums[i] is either a positive integer or -1.
# We need to find for each -1 the respective positive integer, which we call the last visited integer.
# To achieve this goal, let's define two empty arrays: seen and ans.
# Start iterating from the beginning of the array nums.
#  - If a positive integer is encountered, prepend it to the front of seen.
#    - If -1 is encountered, let k be the number of consecutive -1s seen so far (including the current -1),
#    - If k is less than or equal to the length of seen, append the k-th element of seen to ans.
#    - If k is strictly greater than the length of seen, append -1 to ans.
# Return the array ans.
# ----------------------
# 1 <= nums.length <= 100
# nums[i] == -1 or 1 <= nums[i] <= 100
from collections import deque
from random import randint, choice


def last_visited_integers(nums: list[int]) -> list[int]:
    # working_sol (85.13%, 71.72%) -> (42ms, 16.43mb)  time: O(n) | space: O(n)
    seen: deque[int] = deque([])
    k: int = -1
    out: list[int] = []
    for num in nums:
        if -1 == num:
            k += 1
            if k >= len(seen):
                out.append(-1)
            else:
                out.append(seen[k])
        else:
            k = -1
            seen.appendleft(num)
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing whole input array `nums`, once => O(n).
# ----------------------
# Auxiliary space: O(n)
# `seen` <- in the worst case will hold every value from `nums`, but `out` is empty => O(n).
# `out` <- in the worst case will hold every value == -1, but `seen` is empty => O(n).
# Or they will have values shared between them, but never exceed `n` elements => O(n).


test: list[int] = [1, 2, -1, -1, -1]
test_out: list[int] = [2, 1, -1]
assert test_out == last_visited_integers(test)

test = [1, -1, 2, -1, -1]
test_out = [1, 2, 1]
assert test_out == last_visited_integers(test)

test = [choice([randint(1, 100), -1]) for _ in range(100)]
print(test)
