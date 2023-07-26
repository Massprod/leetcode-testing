# You are given an integer array prices where prices[i] is the price
#   of a given stock on the ith day, and an integer k.
# Find the maximum profit you can achieve.
# You may complete at most k transactions: i.e. you may buy
#   at most k times and sell at most k times.
# Note: You may not engage in multiple transactions simultaneously
# (i.e., you must sell the stock before you buy again).
# -------------------
# 1 <= k <= 100
# 1 <= prices.length <= 1000
# 0 <= prices[i] <= 1000


def max_profit(k: int, prices: list[int]) -> int:
    # working_sol (5.8%, 5%) -> (592ms, 86mb)  time: O(2 ** n) | space: O(2 ** n)
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

    # Always returning only maximum_profit of the calling day,
    # with set operations limit.
    return trade_day(0, k * 2, True)


# Time complexity: O(2 ** n) -> standard recursion tree with height of n, we're using every price and for every
# n - len of input_array^^|  recursion call there's 2 choices, if we allowed to buy we're either buying or holding
#                            if we aren't allowed to buy, we're either selling or holding => O(2 ** n).
# Auxiliary space: O(2 ** n) -> recursion stack with maximum size of n => O(n) -> and memory_cache to store
#                            all results of day operations with set (day, operations_left) into dictionary,
#                            we're storing every result of recursion call, so it's should be => O(2 ** n) as well.
# -------------------
# Well my recursion is already set for this task. So let's just try to use it with set operations to k * 2.
# Obviously it's either TLE or just extra slow. But w.e.
# Don't want to just copy DP, cuz it's an only way to make it faster and I didn't learn it properly.
# Like it's not even default DP it's STATE_MACHINE which I never encounter before.
