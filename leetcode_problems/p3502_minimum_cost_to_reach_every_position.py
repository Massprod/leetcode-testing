# You are given an integer array cost of size n.
# You are currently at position n (at the end of the line)
#  in a line of n + 1 people (numbered from 0 to n).
# You wish to move forward in the line, but each person in front of you charges
#  a specific amount to swap places. The cost to swap with person i is given by cost[i].
# You are allowed to swap places with people as follows:
#  - If they are in front of you, you must pay them cost[i] to swap with them.
#  - If they are behind you, they can swap with you for free.
# Return an array answer of size n, where answer[i]
#  is the minimum total cost to reach each position i in the line.
# ------------------------
# 1 <= n == cost.length <= 100
# 1 <= cost[i] <= 100
from random import randint

from pyperclip import copy


def min_costs(cost: list[int]) -> list[int]:
    # working_sol (100.00%, 96.42%) -> (0ms, 17.69mb)  time: O(n) | space: O(n)
    # Everything after index => right side == behind us.
    # Everyting before index => left side == in front of us.
    # So, we just need a minimum prefix for each index.
    out: list[int] = [cost[0]]
    min_prefix: int = cost[0]
    for index in range(1, len(cost)):
        min_prefix = min(min_prefix, cost[index])
        out.append(min_prefix)

    return out


# Time complexity: O(n) <- n - length of the input array `cost`.
# Traversing whole input array `cost`, once => O(n).
# ------------------------
# Auxiliary space: O(n)
# `out` <- allocates space for each value from `cost` => O(n).


test: list[int] = [5, 3, 4, 1, 3, 2]
test_out: list[int] = [5, 3, 3, 1, 1, 1]
assert test_out == min_costs(test)

test = [1, 2, 4, 6, 7]
test_out = [1, 1, 1, 1, 1]
assert test_out == min_costs(test)

test = [randint(1, 100) for _ in range(100)]
copy(test)
