# Alice and Bob are playing a turn-based game on a field,
#  with two lanes of flowers between them.
# There are x flowers in the first lane between Alice and Bob,
#  and y flowers in the second lane between them.
# The game proceeds as follows:
#  1. Alice takes the first turn.
#  2. In each turn, a player must choose either one of the lane
#    and pick one flower from that side.
#  3. At the end of the turn, if there are no flowers left at all,
#    the current player captures their opponent and wins the game.
# Given two integers, n and m, the task is to compute the number of possible pairs
#  (x, y) that satisfy the conditions:
#  1. Alice must win the game according to the described rules.
#  2. The number of flowers x in the first lane must be in the range [1,n].
#  3. The number of flowers y in the second lane must be in the range [1,m].
# Return the number of possible pairs (x, y) that satisfy
#  the conditions mentioned in the statement.
# --- --- --- ---
# 1 <= n, m <= 10 ** 5


def flower_game(n: int, m: int) -> int:
    # working_solution: (100%, 87.50%) -> (0ms, 17.62mb)  Time: O(1) Space: O(1)
    # Alice can win, only when number of turns are `odd`.
    # We can either loop and get it. Or math:
    # Both even => (n / 2) * (m / 2) = all pairs
    # Both odd => ((n + 1) / 2) * ((m - 1) / 2) + ((n - 1) / 2) * ((m + 1) / 2) = (n * m - 1) / 2
    # Diff parity => ((n + 1) / 2) * (m / 2) + ((n - 1) / 2) * (m / 2) = (n * m) / 2
    # Only `both odd` option stands out, and we can simplify it.
    # By simply using a floor division, essentially taking this `-1`.
    return (n * m) // 2


# Time complexity: O(1)
# --- --- --- ---
# Space complexity: O(1)


test_n: int = 3
test_m: int = 2
test_out: int = 3
assert test_out == flower_game(test_n, test_m)

test_n = 1
test_m = 1
test_out = 0
assert test_out == flower_game(test_n, test_m)
