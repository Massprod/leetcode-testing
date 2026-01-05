# You are given an integer array nums and an integer k.
# Return the minimum length of a subarray whose sum of the distinct values
#  present in that subarray (each value counted once) is at least k.
# If no such subarray exists, return -1.
# --- --- --- ---
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 5
# 1 <= k <= 10 ** 9
from collections import defaultdict, deque
from pyperclip import copy
from random import randint


def min_length(nums: list[int], k: int) -> int:
    # working_solution: (100%, 100%) -> (628ms, 37.90mb)  Time: O(n) Space: O(n)
    used: dict[int, int] = defaultdict(int)
    que: deque[int] = deque([])
    que_sum: int = 0
    limit: int = len(nums) + 2
    out: int = limit

    for num in nums:
        que.append(num)
        que_sum += num if 0 == used[num] else 0
        used[num] += 1
        while que and k <= que_sum:
            out = min(out, len(que))
            cur: int = que.popleft()
            used[cur] -= 1
            que_sum -= cur if 0 == used[cur] else 0
    
    return out if out != limit else -1


# Time complexity: O(n)
# n - length of the input array `nums`.
# At most traversing the whole input array `nums`, twice => O(2 * n).
# --- --- --- ---
# Space complexity: O(n)
# In the worst case the whole input array `nums` can be used.
# `used` <- allocates space for each value from `nums` => O(n).
# `que`  <- allocates space for each value from `nums` => O(2 * n).


test: list[int] = [2, 2, 3, 1]
test_k: int = 4
test_out: int = 2
assert test_out == min_length(test, test_k)

test = [3, 2, 3, 4]
test_k = 5
test_out = 2
assert test_out == min_length(test, test_k)

test = [5, 5, 4]
test_k = 5
test_out = 1
assert test_out == min_length(test, test_k)

test = [randint(1, 10 ** 5) for _ in range(10 ** 5)]
copy(test)  # type: ignore
