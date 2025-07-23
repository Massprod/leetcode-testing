# Given an array of non-negative integers arr,
#  you are initially positioned at start index of the array.
# When you are at index i, you can jump to i + arr[i] or i - arr[i],
#  check if you can reach any index with value 0.
# Notice that you can not jump outside of the array at any time.
# ----------------------------
# 1 <= arr.length <= 5 * 10 ** 4
# 0 <= arr[i] < arr.length
# 0 <= start < arr.length
from collections import deque

from random import randint

from pyperclip import copy


def can_reach(arr: list[int], start: int) -> bool:
    # working_sol (96.82%, 65.03%) -> (7ms, 22.90mb)  time: O(n) | space: O(n)
    out: bool = False

    que: deque[int] = deque([start])
    visited: set[int] = {start}
    while que:
        current: int = que.popleft()
        if 0 == arr[current]:
            out = True
            break
        next: int = current + arr[current]
        if 0 <= next < len(arr) and next not in visited:
            que.append(next)
            visited.add(next)
        next = current - arr[current]
        if 0 <= next < len(arr) and next not in visited:
            que.append(next)
            visited.add(next)

    return out


# Time complexity: O(n) <- n - length of the input array `n`.
# Standard BFS, using every index of the `arr` once => O(n).
# ----------------------------
# Auxiliary space: O(n)
# `que` <- allocates space for each index of the input array `n` => O(n).
# `visited` <- allocates space for each index of the input array `n` => O(2 * n).


test: list[int] = [4, 2, 3, 0, 3, 1, 2]
test_start: int = 5
test_out: bool = True
assert test_out == can_reach(test, test_start)

test = [4, 2, 3, 0, 3, 1, 2]
test_start = 0
test_out = True
assert test_out == can_reach(test, test_start)

test = [3, 0, 2, 1, 2]
test_start = 2
test_out = False
assert test_out == can_reach(test, test_start)

test = [randint(0, 5 * 10 ** 3) for _ in range(5 * 10 ** 4)]
copy(test)  # type: ignore
