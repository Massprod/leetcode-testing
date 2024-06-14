# Alice has some number of cards and she wants to rearrange the cards
#  into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.
# Given an integer array hand where hand[i] is the value written
#  on the ith card and an integer groupSize,
#  return true if she can rearrange the cards, or false otherwise.
# -----------------------
# 1 <= hand.length <= 10 ** 4
# 0 <= hand[i] <= 10 ** 9
# 1 <= groupSize <= hand.length
from random import randint
from collections import defaultdict


def is_n_straights(hand: list[int], group_size: int) -> bool:
    # working_sol (71.12%, 63.87%) -> (159ms, 18.36mb)  time: O(n * log n) | space: O(n)
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


test: list[int] = [1, 2, 3, 6, 2, 3, 4, 7, 8]
test_size: int = 3
test_out: bool = True
assert test_out == is_n_straights(test, test_size)

test = [1, 2, 3, 4, 5]
test_size = 4
test_out = False
assert test_out == is_n_straights(test, test_size)

test = [randint(0, 10 ** 9) for _ in range(10 ** 4)]
print(test)
