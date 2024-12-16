# You are given an array nums consisting of positive integers.
# Starting with score = 0, apply the following algorithm:
#  - Choose the smallest integer of the array that is not marked.
#    If there is a tie, choose the one with the smallest index.
#  - Add the value of the chosen integer to score.
#  - Mark the chosen element and its two adjacent elements if they exist.
#  - Repeat until all the array elements are marked.
# Return the score you get after applying the above algorithm.
# ------------------------
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 6
import heapq
import pyperclip
from random import randint


def find_score(nums: list[int]) -> int:
    # working_sol: (65.46%, 30.23%) -> (503ms, 43.84mb)  time: O(n * log n) | space: O(n)
    cur_val: int
    cur_index: int
    # Standard min-Heap to get values in correct order.
    marked: set[int] = set()
    heap: list[int] = [
        (value, index) for index, value in enumerate(nums)
    ]
    heapq.heapify(heap)
    out: int = 0
    while heap:
        cur_val, cur_index = heapq.heappop(heap)
        if cur_index in marked:
            continue
        out += cur_val
        # Not using iterable to save some time :)
        marked.add(cur_index)
        marked.add(cur_index + 1)
        marked.add(cur_index - 1)
    return out


# Time complexity: O(n * log n) <- n - length of the input array `nums`.
# Creating `heap` of size `n` and using every every element of it, once => O(n * log n).
# ------------------------
# Auxiliary space: O(n)
# `heap` <- allocates space for each element of `nums` => O(n).
# `marked` <- allocates space for each element of `nums` + 2 extra indexes for `n + 1` and `n - 1` => O(2 * n).


test: list[int] = [2,1,3,4,5,2]
test_out: int = 7
assert test_out == find_score(test)

test = [2,3,5,1,3,2]
test_out = 5
assert test_out == find_score(test)

test = [randint(1, 10 ** 6) for _ in range(10 ** 3)]
pyperclip.copy(test)
