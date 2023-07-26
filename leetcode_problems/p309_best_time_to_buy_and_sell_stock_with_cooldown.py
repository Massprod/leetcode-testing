# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve.
# You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times)
# with the following restrictions:
#   - After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously
# (i.e., you must sell the stock before you buy again).
# ----------------------
# 1 <= prices.length <= 5000
# 0 <= prices[i] <= 1000
from random import randint


def max_profit(prices: list[int]) -> int:
    # working_sol (45.79%, 6.74%) -> (63ms, 22.6mb)  time: O(2 ** n) | space: O(2 ** n)
    # Recursion results by (day, operations_left).
    mem_cache: dict[tuple[int, bool, bool], int] = {}

    def trade_day(day: int, buy: bool, cooldown: bool) -> int:
        # If similar day is already exist.
        if (day, buy, cooldown) in mem_cache:
            return mem_cache[day, buy, cooldown]
        # There's 2 options to break ->
        # 1) Last day, and we're holding stock -> forced to sell.
        # 2) Last day, and we're not holding stock -> not getting profit.
        if day >= len(prices):
            if buy:
                mem_cache[day, buy, cooldown] = 0
                return 0
            mem_cache[day, buy, cooldown] = prices[-1]
            return prices[-1]
        # Set as -inf for correct comparing.
        buy_profit: int | float = float("-inf")
        sell_profit: int | float = float("-inf")
        if buy:
            # Placeholder for cooldown.
            buy_profit = 0
            # If we're allowed to buy, insta -prices[day].
            if not cooldown:
                buy_profit = prices[day] * -1
            # If we're not allowed to buy, then buy_profit is set to 0,
            # and we're just recalling without cooldown.
            if cooldown:
                buy_profit += trade_day(day + 1, True, False)
            # If we're allowed to buy, increment already set profit of this day.
            if not cooldown:
                buy_profit += trade_day(day + 1, False, False)
            # Hold and buy on another day.
            hold: int = trade_day(day + 1, True, False)
            # Maximum profit of the day.
            buy_profit = max(buy_profit, hold)
        if not buy:
            # Same placeholder for cooldown.
            sell_profit = 0
            # If we're allowed to sell, insta +prices[day]
            if not cooldown:
                sell_profit = prices[day]
            # If we're not allowed to sell, then sell_profit is set to 0,
            # and we're just recalling without cooldown.
            if cooldown:
                sell_profit += trade_day(day + 1, True, False)
            # Otherwise, just increment already set profit of this day.
            if not cooldown:
                sell_profit += trade_day(day + 1, True, True)
            # Hold and sell on another day.
            hold_bought: int = trade_day(day + 1, False, False)
            # Maximum profit of the day.
            sell_profit = max(sell_profit, hold_bought)
        # Essentially the same profit, just better looking than:
        #   if buy_profit != float("-inf"), same for sell.
        max_day_prof: int = max(buy_profit, sell_profit)
        # Store result of the call.
        mem_cache[day, buy, cooldown] = max_day_prof
        return max_day_prof

    # Always returning only maximum_profit of the calling day.
    return trade_day(0, True, False)


# Time complexity: O(2 ** n) -> standard recursion tree with height of n, we're using every price and for every
# n - len of input_array^^|  recursion call there's 2 choices, if we allowed to buy we're either buying or holding
#                            if we aren't allowed to buy, we're either selling or holding => O(2 ** n).
# Auxiliary space: O(2 ** n) -> recursion stack with maximum size of n => O(n) -> and memory_cache to store
#                            all results of day operations with set (day, operations_left) into dictionary,
#                            we're storing every result of recursion call, so it's should be => O(2 ** n) as well.
# ----------------------
# Guess they're all mostly the same. This is why I need to rebuild them all with DP later.
# Especially state_machine.


test1 = [1, 2, 3, 0, 2]
test1_out = 3
assert test1_out == max_profit(test1)

test2 = [1]
test2_out = 0
assert test2_out == max_profit(test2)

test: list[int] = []
for _ in range(5000):
    test.append(randint(0, 1000))
print(test)
