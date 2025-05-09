# There are n friends that are playing a game.
# The friends are sitting in a circle and are numbered from 1 to n in clockwise order.
# More formally, moving clockwise from the ith friend brings you to the (i+1)th
#  friend for 1 <= i < n, and moving clockwise from the nth friend brings you to the 1st friend.
# The rules of the game are as follows:
# 1st friend receives the ball.
#  - After that, 1st friend passes it to the friend who is k steps away
#    from them in the clockwise direction.
#  - After that, the friend who receives the ball should pass it to the friend
#    who is 2 * k steps away from them in the clockwise direction.
#  - After that, the friend who receives the ball should pass it to the friend
#    who is 3 * k steps away from them in the clockwise direction, and so on and so forth.
# In other words, on the ith turn, the friend holding the ball should
#  pass it to the friend who is i * k steps away from them in the clockwise direction.
# The game is finished when some friend receives the ball for the second time.
# The losers of the game are friends who did not receive the ball in the entire game.
# Given the number of friends, n, and an integer k, return the array answer,
#  which contains the losers of the game in the ascending order.
# ----------------------------
# 1 <= k <= n <= 50


def circular_game_losers(n: int, k: int) -> list[int]:
    # working_sol (100.0%, 49.52%) -> (0ms, 17.82mb)  time: O(n) | space: O(n)
    start: int = 1
    multiplier: int = 1
    visited: set[int] = {start}
    unvisited: set[int] = set(range(start + 1, n + 1))
    while True:
        # -1 to get 0-indexed, +1 to get 1-indexed again
        start = (start - 1 + multiplier * k) % n + 1
        if start in unvisited:
            unvisited.remove(start)
        elif start in visited:
            break
        visited.add(start)
        multiplier += 1

    return sorted(unvisited)


# Time complexity: O(n)
# ----------------------------
# Auxiliary space: O(n)
# In the worst case, we visit everything.
# `visited` <- allocates space for each value from 1 -> n, inclusive => O(n).
# `unvisited` <- allocates space for each value from 2 -> n, inclusive => O(2 * n).


test_n: int = 5
test_k: int = 2
test_out: list[int] = [4, 5]
assert test_out == circular_game_losers(test_n, test_k)

test_n = 4
test_k = 4
test_out = [2, 3, 4]
assert test_out == circular_game_losers(test_n, test_k)
