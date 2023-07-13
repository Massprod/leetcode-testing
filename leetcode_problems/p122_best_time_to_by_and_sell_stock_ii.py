# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock.
# You can only hold at most one share of the stock at any time.
# However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.
# ----------------------
# 1 <= prices.length <= 3 * 10 ** 4
# 0 <= prices[i] <= 10 ** 4


def max_profit(prices: list[int]) -> int:
    # working_sol (77.29%, 33.47%) -> (73ms, 17.6mb)  time: O(n) | space: O(1)
    profit: int = 0
    for x in range(1, len(prices)):
        if prices[x] > prices[x - 1]:
            profit += prices[x] - prices[x - 1]
    return profit


# Time complexity: O(n) -> traverse of whole input array, once => O(n).
# n - len of input_array^^|
# Auxiliary space: O(1) -> only 1 extra constant to store profit as INT, doesn't depends on input => O(n).
# ----------------------
# Buy low, sell high. Daily => MaxProfit.
# Only if we can sell on the days with profit, otherwise ignore.
# Like 1 2 3 4 5 6 7 -> if we buy at 1 and hold until 7 it the same max profit as if we sell everything instantly.
# 1 + 1 + 1 + 1 + 1 + 1 = 6 and 1 - 7 = 6, if there's days with less value than we bought stock always ignore.
# Like 1 2 3 4 5 6 7 4 3 2 1 10 12 10 10 -> no reasons to buy or hold after 7.
# There's 3 cases if we can buy and sell it later with Trend going higher than every_day trade will make max_profit.
# If we hold it we're going to lose profit, because if we hold from day with 1 until day 10 and ignore selling at 7
# or any other day we're only getting 11 by selling at 12. But if we trade every day, from 1 to 7 we profit 6 and
# buying with 1 insta selling this at 10 extra +9 and extra +2 if we can buy at this day as well ->
# -> ! On each day, you may decide to buy and/or sell the stock ! <- If I understand correctly we can BUY and SELL
# on the same day, so we're selling already bought stock at 10 and BUY new one with value of 10, if this allowed
# than it's correct. Otherwise, I need extra search, let's test.


test1 = [7, 1, 5, 3, 6, 4]
test1_out = 7
print(max_profit(test1))
assert test1_out == max_profit(test1)

test2 = [1, 2, 3, 4, 5]
test2_out = 4
print(max_profit(test2))
assert test2_out == max_profit(test2)

test3 = [7, 6, 4, 3, 1]
test3_out = 0
print(max_profit(test3))
assert test3_out == max_profit(test3)
