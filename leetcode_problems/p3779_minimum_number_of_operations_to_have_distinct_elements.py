# You are given an integer array nums.
# In one operation, you remove the first three elements of the current array.
# If there are fewer than three elements remaining, all remaining elements are removed.
# Repeat this operation until the array is empty or contains no duplicate values.
# Return an integer denoting the number of operations required.
# --- --- --- ---
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 5
from collections import Counter


def min_operations(nums: list[int]) -> int:
    # working_solution: (6.76%, 22.33%) -> (567ms, 39.42mb)  Time: O(n) Space: O(n)
    # Better option is to get indexes of the duplicates,
    #  and just calc how many deletions we need to make to leave only the one.
    # We always start from `0` -> `preLast` index of the value.
    # Last value is what we leave. But, not rebuilding it for now.
    # ---
    # Count everything higher than 1 occurrence, but with `-1`.
    # And while we're still going to have something in the dict.
    # Means, we have some elements with more than `1` occurence => delete.
    occurs = Counter(nums)
    to_del: set[int] = set()
    for val, occ in occurs.items():
        if 1 == occ:
            to_del.add(val)
    for val in to_del:
        del occurs[val]
    out: int = 0
    if not occurs:
        return out
    cur_ind: int = 0
    cur_len: int = len(nums)
    while (
        (cur_ind + 3) < cur_len
        and occurs
        ):
        for index in range(cur_ind, cur_ind + 3):
            cur_val: int = nums[index]
            if cur_val in occurs:
                occurs[cur_val] -= 1
                if 1 == occurs[cur_val]:
                    del occurs[cur_val]
        out += 1
        cur_ind += 3
    # In case if we still have duplicates within last 3 elements.
    # But, we didn't hit the right indexes and skipped the check.
    if occurs:
        out += 1

    return out


# Time complexity: O(n)
# n - length of the input array `nums`.
# --- --- --- ---
# Space complexity: O(n)
# `occurs` <- allocates space for each unique value of the `nums` => O(n).
# `to_del` <- in the worst case, there's no duplicates, so we delete everything => O(n).


test: list[int] = [3, 8, 3, 6, 5, 8]
test_out: int = 1
assert test_out == min_operations(test)

test = [2, 2]
test_out = 1
assert test_out == min_operations(test)

test = [4, 3, 5, 1, 2]
test_out = 0
assert test_out == min_operations(test)
