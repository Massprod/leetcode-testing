# Alice and Bob continue their games with piles of stones.
# There are a number of piles arranged in a row,
#  and each pile has a positive integer number of stones piles[i].
# The objective of the game is to end with the most stones.
# Alice and Bob take turns, with Alice starting first.
# Initially, M = 1.
# On each player's turn,
#  that player can take all the stones in the first X remaining piles,
#  where 1 <= X <= 2M.
# Then, we set M = max(M, X).
# The game continues until all the stones have been taken.
# Assuming Alice and Bob play optimally,
#  return the maximum number of stones Alice can get.
# -----------------------
# 1 <= piles.length <= 100
# 1 <= piles[i] <= 10 ** 4
from functools import cache
from random import randint


def stone_game_ii(piles: list[int]) -> int:
    # working_sol (94.90%, 57.35%) -> (134ms, 18.36mb)  time: O(n ** 3) | space: O(n * n)
    suffixes: list[int] = piles[:]
    for ind in range(len(suffixes) - 2, -1, -1):
        suffixes[ind] += suffixes[ind + 1]

    @cache
    def check(start_index: int, max_start: int) -> int:
        # We can take everything in One turn. Ignoring Bob.
        if start_index + 2 * max_start >= len(suffixes):
            return suffixes[start_index]
        bob_stones: int = 10 ** 4 * 100
        # We need to maximize Alice, so we search for the worst outcome of Bob's move.
        for index in range(1, 2 * max_start + 1):
            bob_stones = min(
                bob_stones,
                check(start_index + index, max(index, max_start))
            )
        # {whats_left_after_start - whats_taken_by_bob}
        return suffixes[start_index] - bob_stones

    return check(0, 1)


# Time complexity: O(n ** 3) <- n - length of the input array `piles`.
# There's `n * n` states of `start_index` and `max_start`.
# We check every one of them, and for each state we loop `1 -> 2 * max_start + 1`.
# `2 * max_start + 1` can be of `len(suffixes) - 1` => O(n * n * n).
# -----------------------
# Auxiliary space: O(n * n).
# `cache` <- will store `output` for every of the `n * n` states => O(n * n).
# `suffixes` <- extra copy of the original array with size `n` => O(n * n + n).


test: list[int] = [2, 7, 9, 4, 4]
test_out: int = 10
assert test_out == stone_game_ii(test)

test = [1, 2, 3, 4, 5, 100]
test_out = 104
assert test_out == stone_game_ii(test)

test = [randint(1, 10 ** 4) for _ in range(100)]
print(test)
