# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock
#   and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.
# -----------------------
# 1 <= prices.length <= 10 ** 5
# 0 <= prices[i] <= 10 ** 4


def max_profit(prices: list[int]) -> int:
    # working_sol (80.40%, 52.61%) -> (821ms, 27.38mb)  time: O(n) | space: O(1)
    max_prof: int = 0
    lowest_value: int = prices[0]
    # We need only 1 transaction.
    for price in prices:
        # Buy lowest.
        if price < lowest_value:
            lowest_value = price
            continue
        # Sell for any profit, but take only highest.
        max_prof = max(price - lowest_value, max_prof)
    return max_prof


# Time complexity: O(n) -> traversing whole input array, once => O(n)
# n - len of input_list^^|
# Auxiliary space: O(1) -> 2 extra constant INTs, none of them depends on input => O(1)
# -----------------------
# We only allowed to move from left to right, so there's no reason to use stack or anything except the lowest value.
# Holding lowest and extracting it from any other (x + 1) we meet, changing this lowest if we find something lower,
# always taking max() out of this extraction and stored max_value.
# !
# choosing a single day to buy one stock and choosing a different day in the future to sell that stock. !
# ^^We're not allowed to sell on the same day as buying.


test: list[int] = [7, 1, 5, 3, 6, 4]
test_out: int = 5
assert test_out == max_profit(test)

test = [7, 6, 4, 3, 1]
test_out = 0
assert test_out == max_profit(test)
