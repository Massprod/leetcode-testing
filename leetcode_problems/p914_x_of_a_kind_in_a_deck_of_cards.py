# You are given an integer array deck where deck[i]
#  represents the number written on the ith card.
# Partition the cards into one or more groups such that:
#   - Each group has exactly x cards where x > 1, and
#   - All the cards in one group have the same integer written on them.
# Return true if such partition is possible, or false otherwise.
# --------------------
# 1 <= deck.length <= 10 ** 4
# 0 <= deck[i] < 10 ** 4
from random import randint
from collections import Counter


def has_group_size_x(deck: list[int]) -> bool:
    # working_sol (68.41%, 67.47%) -> (109ms, 16.88mb)  time: O(n * k) | space: O(n)
    # The most tricky part of the problem is that.
    # We can break one group into multiple groups,
    #  and all the groups should be of an equal size.
    # So, we just need to find minimum group size.
    # Because we can break longer ones, by the minium.
    # And a minimum group can be broken in w.e sizes from 2 -> `min_size` (inclusive).
    cards: dict[int, int] = Counter(deck)
    min_size: int = 10 ** 5
    for group, size in cards.items():
        if 1 == size:
            return False
        min_size = min(min_size, size)
    check: int = 2
    correct: bool = True
    while check <= min_size:
        if min_size % check:
            check += 1
            continue
        correct: bool = True
        for group, size in cards.items():
            if size % check:
                correct = False
                break
        if correct:
            return correct
        check += 1
    return correct


# Time complexity: O(n * k) <- n - length of the input array `deck`, k - minimum group of the same integer.
# We're always traversing the whole `deck` to get all the occurrences, once => O(n).
# Another traverse to check for 1 sized group, and find minimum => O(2n).
# And another `k` traverses to check all the options we have in range (2 -> k) inclusive => O(2n + n * k)
# --------------------
# Auxiliary space: O(n)
# `cards` is going to allocate space for every unique value in `deck`,
#  and in the worst case, every value is unique => O(n).


test: list[int] = [1, 2, 3, 4, 4, 3, 2, 1]
test_out: bool = True
assert test_out == has_group_size_x(test)

test = [1, 1, 1, 2, 2, 2, 3, 3]
test_out = False
assert test_out == has_group_size_x(test)

test = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2]
test_out = True
assert test_out == has_group_size_x(test)

test = [randint(0, 10 ** 4) for _ in range(10 ** 4)]
print(test)
