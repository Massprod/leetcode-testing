# You are given an integer array nums.
# You start with an empty array ans. Repeat the following operation until nums is empty:
#  - Identify all distinct values currently present in nums.
#  - Remove one occurrence of every distinct value currently in nums,
#     and append those values to ans in ascending order.
# Return the array ans.
# --- --- --- ---
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
from random import randint
from collections import Counter
from pyperclip import copy


def rearrange_array(nums: list[int]) -> list[int]:
    # working_solution: (38.66%, 12.46%) -> (9ms, 19.50mb)  Time: O(n) Space: O(n)
    out: list[int] = []
    distinct: dict[int, int] = Counter(nums)
    while distinct:
        current: list[int] = []
        t_remove: set[int] = set()
        for key, value in distinct.items():
            if 0 == value:
                t_remove.add(key)
                continue
            current.append(key)
            distinct[key] -= 1
        for key in t_remove:
            distinct.pop(key)
        out.extend(sorted(current))

    return out


# Time complexity: O(n)
# n - length of the input array `nums`
# --- --- --- ---
# Space complexity: O(n)


test_nums: list[int] = [3, 1, 3, 2, 1, 3]
test_out: list[int] = [1, 2, 3, 1, 3, 3]
assert test_out == rearrange_array(test_nums)

test_nums = [7, 7, 4, 4, 4]
test_out = [4, 7, 4, 7, 4]
assert test_out == rearrange_array(test_nums)

test_nums = [randint(1, 100) for _ in range(100)]
copy(test_nums)
