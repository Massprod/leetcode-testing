# You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
# Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.
# ----------------------
# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999
from random import randint


def min_cost_stairs(cost: list[int]) -> int:
    # working_sol (86.3%, 99.1%) -> (59ms, 16.3mb)  time: O(n) | space: O(1)
    cost.append(0)
    # Standard choose lowest option from [-1] [-2] index options.
    for x in range(2, len(cost)):
        cost[x] = cost[x] + min(cost[x - 2], cost[x - 1])
    return cost[-1]


# Time complexity: O(n) -> could say O(log n), cuz we're skipping first 2 indexes, but better to stick with => O(n).
# n - len of input_array^^|
# Auxiliary space: O(1) -> nothing extra, only 1 index appended, and it doesn't depend on input => O(1).
# ----------------------
# Standard min([-2], [-1]) + current? Yep.


test: list[int] = [10, 15, 20]
test_out: int = 15
assert test_out == min_cost_stairs(test)

test = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
test_out = 6
assert test_out == min_cost_stairs(test)

test = []
for _ in range(10 ** 3):
    test.append(randint(0, 999))
print(test)
