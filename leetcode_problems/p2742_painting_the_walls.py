# You are given two 0-indexed integer arrays, cost and time,
#  of size n representing the costs and the time taken to paint n different walls respectively.
# There are two painters available:
#   A paid painter that paints the ith wall in time[i] units of time and takes cost[i] units of money.
#   A free painter that paints any wall in 1 unit of time at a cost of 0.
#    But the free painter can only be used if the paid painter is already occupied.
# Return the minimum amount of money required to paint the n walls.
# ------------------
# 1 <= cost.length <= 500
# cost.length == time.length
# 1 <= cost[i] <= 10 ** 6
# 1 <= time[i] <= 500
from random import randint


def paint_walls(cost: list[int], time: list[int]) -> int:
    # working_sol (20.74%, 33.70%) -> (2568ms, 427.8mb)  time: O(n * n) | space: O(n * n)
    recur_cache: dict[tuple[int, int], int] = {}
    # We can only paint indexes of cost or time, a.k.a walls.
    # And we need minimum, so if we go out -> insta failed.
    # ! 1 <= cost[i] <= 10 ** 6 , 1 <= cost.length <= 500 !
    max_limit: int = 10 ** 6 * 500

    def check(wall: int, walls_left: int) -> int:
        if (wall, walls_left) in recur_cache:
            return recur_cache[wall, walls_left]
        # All painted, and we have extra free painter walls.
        if walls_left <= 0:
            return 0
        # Still need walls to paint, and we already out.
        if wall >= len(cost):
            return max_limit
        min_cost: int = min(
            cost[wall] + check(wall + 1, walls_left - 1 - time[wall]),  # paint current wall and (time == free walls)
            check(wall + 1, walls_left),  # don't start painting from this wall
        )
        recur_cache[wall, walls_left] = min_cost
        return min_cost

    return check(0, len(cost))


# Time complexity: O(n * n) -> recursion with 'n' states for 'wall' input and same for 'walls_left' => O(n * n).
# n - len of input array 'cost'|'time'^^|
# Auxiliary space: O(n * n) -> using dictionary for memorization(cache) to store all these call states => O(n * n).
# ------------------
# Tags: DynamicP.
# So it should be top-down recursion, for start. What we need?
# Essentially all we care is that did we start painting?
# Because if we do, then we can paint some ('k' == cost[start]) walls for free:
# ! A free painter that paints any wall in 1 unit of time at a cost of 0.
#    But the free painter can only be used if the paid painter is already occupied. !
# Start painting from every index(wall) until all walls are done and choose min?
# Let's try.


test_cost: list[int] = [1, 2, 3, 2]
test_time: list[int] = [1, 2, 3, 2]
test_out: int = 3
assert test_out == paint_walls(test_cost, test_time)

test_cost = [2, 3, 4, 2]
test_time = [1, 1, 1, 1]
test_out = 4
assert test_out == paint_walls(test_cost, test_time)

test_cost = [randint(1, 10 ** 6) for _ in range(500)]
test_time = [randint(1, 500) for _ in range(500)]
print(test_cost)
print('!=====================!')
print(test_time)
