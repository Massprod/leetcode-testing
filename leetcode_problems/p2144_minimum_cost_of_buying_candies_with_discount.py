# A shop is selling candies at a discount.
# For every two candies sold, the shop gives a third candy for free.
# The customer can choose any candy to take away for free as long as the cost of the chosen candy
#  is less than or equal to the minimum cost of the two candies bought.
# For example, if there are 4 candies with costs 1, 2, 3, and 4,
#  and the customer buys candies with costs 2 and 3,
#  they can take the candy with cost 1 for free, but not the candy with cost 4.
# Given a 0-indexed integer array cost, where cost[i] denotes the cost of the ith candy,
#  return the minimum cost of buying all the candies.
# -------------------------------
# 1 <= cost.length <= 100
# 1 <= cost[i] <= 100
from random import randint


def minimum_cost(cost: list[int]) -> int:
    # working_sol (98.83%, 68.33%) -> (34ms, 16.42mb)  time: O(n * log n) | space: O(n)
    sorted_costs: list[int] = sorted(cost)
    out: int = 0
    # Best option is to take `highest_cost` + `pre_highest_cost` and take next `pre_highest_cost` for free.
    while sorted_costs:
        try:
            out += sorted_costs.pop()
            out += sorted_costs.pop()
            sorted_costs.pop()
        except Exception as e:
            pass
    return out


# Time complexity: O(n * log n) <- n - length of the input array `cost`.
# Always sorting original input array `cost` => O(n * log n).
# Extra using every value in it, after sorting => O(n * log n + n).
# -------------------------------
# Auxiliary space: O(n)
# `sorted_costs` <- always of the same size as `cost` => O(n).


test: list[int] = [1, 2, 3]
test_out: int = 5
assert test_out == minimum_cost(test)

test = [6, 5, 7, 9, 2, 2]
test_out = 23
assert test_out == minimum_cost(test)

test = [5, 5]
test_out = 10
assert test_out == minimum_cost(test)

test = [randint(1, 100) for _ in range(100)]
print(test)
