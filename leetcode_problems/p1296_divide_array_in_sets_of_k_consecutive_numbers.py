# Given an array of integers nums and a positive integer k,
#  check whether it is possible to divide this array into sets of k consecutive numbers.
# Return true if it is possible. Otherwise, return false.
# ------------------
# 1 <= k <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 9
from random import randint
from collections import defaultdict


def is_n_straights(hand: list[int], group_size: int) -> bool:
    # working_sol (79.91%, 87.55%) -> (325ms, 33.90mb)  time: O(n * log n) | space: O(n)
    if 1 == group_size:
        return True
    # {symbol: occurrences}
    occurrences: dict[int, int] = defaultdict(int)
    for val in hand:
        occurrences[val] += 1
    # We need consecutive, so it's the best way to start from lowest
    #  and take what we need in order.
    hand.sort()
    cur_group: int = 0
    for num in hand:
        if 0 == occurrences[num]:
            continue
        if 0 == cur_group:
            cur_group += 1
            occurrences[num] -= 1
        _next: int = num
        # We should always use every symbol we can, and it's consecutive cards == diff by 1 left -> right.
        while cur_group != group_size:
            _next += + 1
            if _next in occurrences and occurrences[_next] > 0:
                cur_group += 1
                occurrences[_next] -= 1
            # If we can't build a group with `group_size` == we can't rearrange them correctly.
            else:
                return False
        cur_group = 0
    return True


# Time complexity: O(n * log n) <- n - length of the input array `hand`.
# We're traversing `hand` once to get all occurrences, and extra time to build groups => O(2n).
# But, because we need some ordering for the correct consecutive sequence, we sort this array => O(n * log n).
# -----------------------
# Auxiliary space: O(n)
# Worst case: every value is unique, so we will store all values in occurrences => O(n).
# And basic `sort()` always takes O(n).


test: list[int] = [1, 2, 3, 3, 4, 4, 5, 6]
test_k: int = 4
test_out: bool = True
assert test_out == is_n_straights(test, test_k)

test = [3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11]
test_k = 3
test_out = True
assert test_out == is_n_straights(test, test_k)

test = [1, 2, 3, 4]
test_k = 3
test_out = False
assert test_out == is_n_straights(test, test_k)
