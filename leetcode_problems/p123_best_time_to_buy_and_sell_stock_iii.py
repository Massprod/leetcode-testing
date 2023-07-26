# You are given an array prices where prices[i]
#   is the price of a given stock on the ith day.
# Find the maximum profit you can achieve.
# You may complete at most two transactions.
# Note: You may not engage in multiple transactions simultaneously
# (i.e., you must sell the stock before you buy again).
# -------------------
# 1 <= prices.length <= 10 ** 5
# 0 <= prices[i] <= 10 ** 5
from random import randint


def max_profit(prices: list[int]) -> int:
    # working_sol (5.3%, 5.38%) -> (5407ms, 558.3mb)  time: O(2 ** n) | space: O(2 ** n)
    # Recursion results by (day, operations_left).
    mem_cache: dict[tuple[int, int], int] = {}

    def trade_day(day: int, op_left: int, buy: bool) -> int:
        # If similar day is already exist.
        if (day, op_left) in mem_cache:
            return mem_cache[(day, op_left)]
        # There's 3 options to break ->
        # 1) No operations available, so we can't sell/buy more.
        # 2) Last day and we're holding stock -> forced to sell.
        # 3) Last day and we're not holding stock -> not getting profit.
        if op_left == 0 or day >= len(prices):
            if buy:
                mem_cache[day, op_left] = 0
                return 0
            mem_cache[day, op_left] = prices[-1]
            return prices[-1]
        # Set as -inf for correct comparing.
        buy_profit: int | float = float("-inf")
        sell_profit: int | float = float("-inf")
        if buy:
            # If we allowed to buy, our profit at this day is insta -prices[day]
            buy_profit = prices[day] * -1
            # We can sell on other day and increment profit.
            buy_profit += trade_day(day + 1, op_left - 1, False)
            # Or we can hold and buy on other day.
            hold: int = trade_day(day + 1, op_left, True)
            # Maximum profit of the buying_day:
            buy_profit = max(buy_profit, hold)
        if not buy:
            # If we allowed to sell, insta +prices[day].
            sell_profit = prices[day]
            # If we sell, increment profit and allow buying.
            sell_profit += trade_day(day, op_left - 1, True)
            # Or hold and sell on other day.
            hold_bought: int = trade_day(day + 1, op_left, False)
            # Maximum profit of the selling_day:
            sell_profit = max(sell_profit, hold_bought)
        # Same
        max_day_prof: int = max(buy_profit, sell_profit)
        mem_cache[(day, op_left)] = max_day_prof
        return max_day_prof

    # Always returning only maximum_profit of the calling day.
    return trade_day(0, 4, True)


# Time complexity: O(2 ** n) -> standard recursion tree with height of n, we're using every price and for every
# n - len of input_array^^|  recursion call there's 2 choices, if we allowed to buy we're either buying or holding
#                            if we aren't allowed to buy, we're either selling or holding => O(2 ** n).
# Auxiliary space: O(2 ** n) -> recursion stack with maximum size of n => O(n) -> and memory_cache to store
#                            all results of day operations with set (day, operations_left) into dictionary,
#                            we're storing every result of recursion call, so it's should be => O(2 ** n) as well.
# -------------------
# Well. It's working but slow. There's no TL, and I didn't see any solution in a speed_graph faster
# without using DP. And I have no idea how to implement DP approach here, like what we can cull?
# It's fine for my solution, but I need to extra search and learn DP approach.


test1 = [3, 3, 5, 0, 0, 3, 1, 4]
test1_out = 6
assert test1_out == max_profit(test1)

test2 = [1, 2, 3, 4, 5]
test2_out = 4
assert test2_out == max_profit(test2)

test3 = [7, 6, 4, 3, 1]
test3_out = 0
assert test3_out == max_profit(test3)

test4 = [3, 4, 5, 6, 7, 4, 3, 2, 1, 9, 10, 11, 12]
test4_out = 15
assert test4_out == max_profit(test4)

test: list[int] = []
for _ in range(10 ** 5):
    test.append(randint(0, 10 ** 5))
print(test)
