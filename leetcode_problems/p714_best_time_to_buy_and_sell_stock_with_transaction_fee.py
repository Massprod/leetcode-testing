# You are given an array prices where prices[i] is the price of a given stock on the ith day,
#   and an integer FEE representing a transaction fee.
# Find the maximum profit you can achieve. You may complete as many transactions as you like,
#   but you need to pay the transaction fee for each transaction.
# Note:
#   You may not engage in multiple transactions simultaneously
#     (i.e., you must sell the stock before you buy again).
#   The transaction fee is only charged once for each stock purchase and sale.
# ----------------------
# 1 <= prices.length <= 5 * 10 ** 4
# 1 <= prices[i] < 5 * 10 ** 4
# 0 <= fee < 5 * 10 ** 4
from random import randint


def max_profit(prices: list[int], fee: int) -> int:
    # working_sol (5.2%, 7.72%) -> (1835ms, 246.9mb)  time: O(2 ** n) | space: O(2 ** n)
    # Store already existed (day, buy) couple.
    mem_cache: dict[tuple[int, bool], int] = {}

    def trade_day(day: int, buy: bool) -> int:
        # If similar day is already exist.
        if (day, buy) in mem_cache:
            return mem_cache[day, buy]
        # There's 2 options to break ->
        # 1) Last day, and we're holding stock -> forced to sell.
        # 2) Last day, and we're not holding stock -> not getting profit.
        if day >= len(prices):
            if buy:
                mem_cache[day, buy] = 0
                return 0
            mem_cache[day, buy] = prices[-1]
            return prices[-1]
        # Set as -inf for correct comparing.
        buy_profit: int | float = float("-inf")
        sell_profit: int | float = float("-inf")
        if buy:
            # Only 1fee taken for the whole cycle of BUY/SELL.
            # So it's either here or in sell_profit doesn't matter.
            buy_profit = prices[day] * -1 - fee
            # Buy and sell later.
            buy_profit += trade_day(day + 1, False)
            # Hold and buy on another day.
            hold: int = trade_day(day + 1, True)
            # Maximum profit of the day.
            buy_profit = max(buy_profit, hold)
        if not buy:
            sell_profit = prices[day]
            # Sell and buy new one.
            sell_profit += trade_day(day + 1, True)
            # Hold and sell on another day.
            hold_bought: int = trade_day(day + 1, False)
            # Maximum profit of the day.
            sell_profit = max(sell_profit, hold_bought)
        # Essentially the same profit, just better looking than:
        #   if buy_profit != float("-inf"), same for sell.
        max_day_prof: int = max(buy_profit, sell_profit)
        # Store result of the call.
        mem_cache[day, buy] = max_day_prof
        return max_day_prof

    # Always returning only maximum_profit of the calling day.
    return trade_day(0, True)


# Time complexity: O(2 ** n) -> standard recursion tree with height of n, we're using every price and for every
# n - len of input_array^^|  recursion call there's 2 choices, if we allowed to buy we're either buying or holding
#                            if we aren't allowed to buy, we're either selling or holding => O(2 ** n).
# Auxiliary space: O(2 ** n) -> recursion stack with maximum size of n => O(n) -> and memory_cache to store
#                            all results of day operations with set (day, operations_left) into dictionary,
#                            we're storing every result of recursion call, so it's should be => O(2 ** n) as well.
# ----------------------
# Same slow af, only change is to take -2 either from BUY moment or SELL dunno why they calling it in description ->
# -> ! you need to pay the transaction fee for each transaction ! -> When in the 1 test_case they literally take only
# ONE fee for BUY/SELL cycle not BUY AND SELL.
# Rebuild every task with stocks to DP later. 5% lame :)


test1 = [1, 3, 2, 8, 4, 9]
test1_fee = 2
test1_out = 8
assert test1_out == max_profit(test1, test1_fee)

test2 = [1, 3, 7, 5, 10, 3]
test2_fee = 3
test2_out = 6
assert test2_out == max_profit(test2, test2_fee)

test: list[int] = []
for _ in range(5 * 10 ** 4):
    test.append(randint(1, 5 * 10 ** 4))
test_fee: int = randint(0, 5 * 10 ** 4)
print(test)
print(test_fee)
