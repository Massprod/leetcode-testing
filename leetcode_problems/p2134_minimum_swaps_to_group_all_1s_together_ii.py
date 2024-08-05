# A swap is defined as taking two distinct positions
#  in an array and swapping the values in them.
# A circular array is defined as an array where we consider the first element
#  and the last element to be adjacent.
# Given a binary circular array nums,
#  return the minimum number of swaps required to group all 1's present
#  in the array together at any location.
# ---------------------------
# 1 <= nums.length <= 10 ** 5
# nums[i] is either 0 or 1.


def min_swaps(nums: list[int]) -> int:
    # working_sol (80.63%, 71.40%) -> (673ms, 20.24mb)  time: O(n) | space: O(n)
    out: int = 10 ** 5
    # The Maximum size of subarray we can build with using every `1`.
    window_size: int = nums.count(1)
    # The Current amount of `0` we have in our sliding window.
    cur_window: int = 0
    for index in range(window_size):
        cur_window += 1 if nums[index] == 0 else 0
    out = min(out, cur_window)
    # If we already have a window with the correct size, and no `0` => best option.
    if 0 == out:
        return out
    # Circular copy of the `nums` to escape circular indexing.
    circular: list[int] = nums + nums[:window_size + 1]
    left: int = 0
    right: int = window_size - 1
    while right < len(circular) - 1:
        # If we had `0` in our previous window placement => delete it.
        cur_window -= 1 if circular[left] == 0 else 0
        left += 1
        right += 1
        # If we got `0` in out new window placement => add it.
        cur_window += 1 if circular[right] == 0 else 0
        out = min(out, cur_window)
        if 0 == out:
            return out
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing `nums`, once to get all occurrences of `1`s => O(n).
# Building `circular` with `2 * n` size => O(n + 2 * n)
# Extra traversing every index in circular `nums`, once => O(n + 4 * n).
# ---------------------------
# Auxiliary space: O(n)
# `circular` <- in the worst case, where every value is `1` size ==  `2 * n` => O(2 * n).


test: list[int] = [0, 1, 0, 1, 1, 0, 0]
test_out: int = 1
assert test_out == min_swaps(test)

test = [0, 1, 1, 1, 0, 0, 1, 1, 0]
test_out = 2
assert test_out == min_swaps(test)

test = [1, 1, 0, 0, 1]
test_out = 0
assert test_out == min_swaps(test)
