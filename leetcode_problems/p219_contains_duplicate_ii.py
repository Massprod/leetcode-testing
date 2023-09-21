# Given an integer array nums and an integer k, return true if there are two distinct
#  indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
# --------------
# 1 <= nums.length <= 10 ** 5
# -10 ** 9 <= nums[i] <= 10 ** 9
# 0 <= k <= 10 ** 5
from random import randint


def contains_duplicate(nums: list[int], k: int) -> bool:
    # working_sol (49.67%, 93.6%) -> (530ms, 27.8mb)  time: O(n) | space: O(k)
    # Standard sliding window.
    insides: set[int] = set()
    # index + k elements on both sides == window of k + 1 size.
    max_window: int = k + 1
    cur_window: int = 0
    start_index: int = 0
    for x in range(len(nums)):
        # Expand.
        cur_window += 1
        # Shrink when exceeding.
        while cur_window > max_window:
            insides.remove(nums[start_index])
            start_index += 1
            cur_window -= 1
        if nums[x] in insides:
            return True
        insides.add(nums[x])
    return False


# Time complexity: O(n) -> traversing whole input array once => O(n).
# Auxiliary space: O(k) -> extra set with 'k + 1' max elements inside => O(k).
# --------------
# !
# abs(i - j) <= k
# !
# Essentially it's a range of value from i - k to i + k inclusive.
# So it's should be correct to just use sliding window and add everything inside of it into dictionary.
# And if anything new we add is already here, we return True.
# Window size should be k + 1, 1 for index and k indexes on both sides. Let's try.


test: list[int] = [1, 2, 3, 1]
test_k: int = 3
test_out: bool = True
assert test_out == contains_duplicate(test, test_k)

test = [1, 0, 1, 1]
test_k = 1
test_out = True
assert test_out == contains_duplicate(test, test_k)

test = [1, 2, 3, 1, 2, 3]
test_k = 2
test_out = False
assert test_out == contains_duplicate(test, test_k)

test = [randint(-10 ** 9, 10 ** 9) for _ in range(10 ** 3)]
print(test)
