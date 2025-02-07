# You are given an integer limit and a 2D array queries of size n x 2.
# There are limit + 1 balls with distinct labels in the range [0, limit].
# Initially, all balls are uncolored. For every query in queries that is of the form
#  [x, y], you mark ball x with the color y.
# After each query, you need to find the number of distinct colors among the balls.
# Return an array result of length n, where result[i] denotes the number
#  of distinct colors after ith query.
# Note that when answering a query, lack of a color will not be considered as a color.
# ---------------------------
# 1 <= limit <= 10 ** 9
# 1 <= n == queries.length <= 10 ** 5
# queries[i].length == 2
# 0 <= queries[i][0] <= limit
# 1 <= queries[i][1] <= 10 ** 9
from pyperclip import copy

from random import randint

from collections import defaultdict


def query_results(limit: int, queries: list[list[int]]) -> list[int]:
    # working_sol (69.09%, 80.80%) -> (70ms, 63.05mb)  time: O(n) | space: O(n)
    # { color: time of usage }
    used_colors: dict[int, int] = defaultdict(int)
    # { ball: cur color of the ball }
    colored_balls: dict[int, int] = defaultdict(int)
    out: list[int] = []
    cur_colors: int = 0
    for ball, color in queries:
        if ball in colored_balls:
            if colored_balls[ball] != color:
                prev_color: int = colored_balls[ball]
                used_colors[prev_color] -= 1
                colored_balls[ball] = color
                used_colors[color] += 1
                # No balls are using this color anymore.
                if 0 == used_colors[prev_color]:
                    cur_colors -= 1
                # New ball are using this color.
                if 1 == used_colors[color]:
                    cur_colors += 1
        else:
            colored_balls[ball] = color
            used_colors[color] += 1
            if 1 == used_colors[color]:
                cur_colors += 1
        out.append(cur_colors)
    
    return out


# Time complexity: O(n) <- n - length of the input array `queries`.
# Always traversing whole input array `queries`, once => O(n).
# ---------------------------
# Auxiliary space: O(n)
# In the worst case, every `query` from `queries` are unique.
# For every `query` we're going to have unique ball in `colored_balls`
#  and unique color in `used_colors` => O(2 * n).


test: int = 4
test_queries: list[list[int]] = [
    [1, 4], [2, 5], [1, 3], [3, 4]
]
test_out: list[int] = [1, 2, 2, 3]
assert test_out == query_results(
    test, test_queries
)

test = 4
test_queries = [
    [0, 1], [1, 2], [2, 2], [3, 4], [4, 5]
]
test_out = [1, 2, 2, 3, 4]
assert test_out == query_results(
    test, test_queries
)

test_limit: int = randint(1, 10 ** 9)
test_queries = [
    [randint(1, test_limit), randint(1, 10 ** 9)] for _ in range(10 ** 3)
]
print('\nLimit:', test_limit)
copy(test_queries)
