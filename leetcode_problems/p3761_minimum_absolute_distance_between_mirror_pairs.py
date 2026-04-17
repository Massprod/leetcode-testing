# You are given an integer array nums.
# A mirror pair is a pair of indices (i, j) such that:
#  - 0 <= i < j < nums.length, and
#  - reverse(nums[i]) == nums[j], where reverse(x) denotes the integer formed
#    by reversing the digits of x. Leading zeros are omitted after reversing,
#    for example reverse(120) = 21.
# Return the minimum absolute distance between the indices of any mirror pair.
# The absolute distance between indices i and j is abs(i - j).
# If no mirror pair exists, return -1.
# --- --- --- ---
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 9
from collections import deque, defaultdict
from random import randint
from pyperclip import copy


def min_mirror_pair_distance(nums: list[int]) -> int:
    # working_solution: (19.38%, 5.04%) -> (357ms, 109.87mb)  Time: O(n) Space: O(n)
    _limit: int = 10 ** 6
    out: int = _limit
    indexes: dict[int, deque] = defaultdict(deque)
    for index, num in enumerate(nums):
        indexes[num].append(index)
    for index, num in enumerate(nums):
        rev_num: int = int(str(num)[::-1])
        if rev_num not in indexes or 0 == len(indexes[rev_num]):
            continue
        t_index: int = indexes[rev_num][0]
        while t_index <= index and indexes[rev_num]:
            t_index = indexes[rev_num].popleft()
        if t_index <= index:
            continue
        out = min(
            out,
            abs(index - t_index)
        )
    
    return out if out != _limit else -1


# Time complexity: O(n)
# --- --- --- ---
# Space complexity: O(n)


test: list[int] = [12, 21, 45, 33, 54]
test_out: int = 1
assert test_out == min_mirror_pair_distance(test)

test = [120, 21]
test_out = 1
assert test_out == min_mirror_pair_distance(test)

test = [21, 120]
test_out = -1
assert test_out == min_mirror_pair_distance(test)

test = [randint(1, 10 ** 9) for _ in range(10 ** 5)]
copy(test)  # type: ignore
