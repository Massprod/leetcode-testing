# Given an integer n and an integer array rounds.
# We have a circular track which consists of n sectors labeled from 1 to n.
# A marathon will be held on this track, the marathon consists of m rounds.
# The ith round starts at sector rounds[i - 1] and ends at sector rounds[i].
# For example, round 1 starts at sector rounds[0] and ends at sector rounds[1]
# Return an array of the most visited sectors sorted in ascending order.
# Notice that you circulate the track in ascending order of sector numbers in the counter-clockwise direction.
# -----------------------------
# 2 <= n <= 100
# 1 <= m <= 100
# rounds.length == m + 1
# 1 <= rounds[i] <= n
# rounds[i] != rounds[i + 1] for 0 <= i < m
from random import randint


def most_visited(n: int, rounds: list[int]) -> list[int]:
    # working_sol (86.12%, 84.90%) -> (39ms, 16.45mb)  time: O(n + (m * k)) | space: O(n)
    # Circular array of the size.
    sectors: list[int] = [0 for _ in range(n + 1)]
    # We start from `rounds[0]`.
    sectors[rounds[0]] += 1
    for index in range(1, len(rounds)):
        start = rounds[index - 1]
        end = rounds[index]
        # We need to make a circle.
        if start > end:
            end = n + end
        for sector in range(start + 1, end + 1):
            # But we still use standard indexing, 1-indexed tho.
            if sector > n:
                sector -= n
            sectors[sector] += 1
    out: list[int] = []
    max_visits: int = 0
    for sector, visits in enumerate(sectors):
        if max_visits < visits:
            out = [sector]
            max_visits = visits
        elif max_visits == visits:
            out.append(sector)
    return sorted(out)


# Time complexity: O(n + (m * k)) <- m - length of the input array `rounds`,
#                                    k - average length of the visited in round sectors
# Always building `sectors` of the size `n` => O(n).
# Always traversing whole input array `rounds` => O(n + m)
# For each round in `rounds` we traverse values from `start` -> `end`,
#  which is average of the ranges in `rounds` => O(n + (m * k)).
# -----------------------------
# Auxiliary space: O(n)
# `sectors` <- always of the size `n` => O(n).
# `out` <- in the worst case, every sector will be visited equal # of times, all of them will be in `out` => O(2 * n).


test_n: int = 4
test_rounds: list[int] = [1, 3, 1, 2]
test_out: list[int] = [1, 2]
assert test_out == most_visited(test_n, test_rounds)

test_n = 2
test_rounds = [2, 1, 2, 1, 2, 1, 2, 1, 2]
test_out = [2]
assert test_out == most_visited(test_n, test_rounds)

test_n = 7
test_rounds = [1, 3, 5, 7]
test_out = [1, 2, 3, 4, 5, 6, 7]
assert test_out == most_visited(test_n, test_rounds)

test_n = 100
test_rounds = sorted(set([randint(1, test_n) for _ in range(100)]))
print(test_rounds)
