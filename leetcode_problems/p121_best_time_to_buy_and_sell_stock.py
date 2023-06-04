# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock
#   and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.
# -----------------------
# 1 <= prices.length <= 10 ** 5  ,  0 <= prices[i] <= 10 ** 4


def max_profit(prices: list[int]) -> int:
    # working_sol (73.79%, 42.37%) -> (979ms, 27.3mb)  time: O(n) | space: O(1)
    max_prof: int = 0
    lowest_value: int = prices[0]
    for price in prices:
        if price < lowest_value:
            lowest_value = price
            continue
        max_prof = max(price - lowest_value, max_prof)
    return max_prof


# Time complexity: O(n) -> traversing whole input_list only once => O(n)
# n - len of input_list^^|
# Auxiliary space: O(1) -> storing two extra INTs, doesn't depends on input => O(1)
# -----------------------
# We only allowed to move from left to right, so there's no reason to use stack or anything except the lowest value.
# Holding lowest and extracting it from any other (x + 1) we meet, changing this lowest if we find something lower,
# always taking max() out of this extraction and stored max_value.
# !
# choosing a single day to buy one stock and choosing a different day in the future to sell that stock. !
# ^^Guess we're not allowed to sell on the same day as well.


test1 = [7, 1, 5, 3, 6, 4]
test1_out = 5
print(max_profit(test1))
assert test1_out == max_profit(test1)

test2 = [7, 6, 4, 3, 1]
test2_out = 0
print(max_profit(test2))
assert test2_out == max_profit(test2)
