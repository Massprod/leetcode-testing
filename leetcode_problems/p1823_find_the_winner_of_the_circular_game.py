# There are n friends that are playing a game.
# The friends are sitting in a circle and are numbered from 1 to n in clockwise order.
# More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n,
#  and moving clockwise from the nth friend brings you to the 1st friend.
# The rules of the game are as follows:
#  1. Start at the 1st friend.
#  2. Count the next k friends in the clockwise direction including the friend you started at.
#     The counting wraps around the circle and may count some friends more than once.
#  3. The last friend you counted leaves the circle and loses the game.
#  4. If there is still more than one friend in the circle,
#     go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat.
#  5. Else, the last friend in the circle wins the game.
# Given the number of friends, n, and an integer k,
#  return the winner of the game.
# ---------------
# 1 <= k <= n <= 500


def find_the_winner(n: int, k: int) -> int:
    # working_sol (38.92%, 49.47%) -> (45ms, 16.53mb)  time: O(n * n) | space: O(n)
    friends: list[int] = [val for val in range(1, n + 1)]
    while 1 < len(friends):
        cur_index: int = 0
        target: int = cur_index + k - 1
        # We need to make some extra full circles.
        if target >= len(friends):
            target %= len(friends)
        friends = friends[target + 1:] + friends[:target]
    return friends[0]


# Time complexity: O(n * n) <- n - input value of friends `n`.
# Always creating array `friends` with size of `n` => O(n).
# Depleting it to the size of `1` with slicing an entire array on every index => O(n * n).
# ---------------
# Auxiliary space: O(n)
# `friends` is always allocate space to store `n` values => O(n).
# And slicing will use (n - 1) values, until 1 value is left, still linear => O(2n).


test_n: int = 5
test_k: int = 2
test_out: int = 3
assert test_out == find_the_winner(test_n, test_k)

test_n = 6
test_k = 5
test_out = 1
assert test_out == find_the_winner(test_n, test_k)
