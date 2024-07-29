# You are given an integer array prices where prices[i]
#  is the price of the ith item in a shop.
# There is a special discount for items in the shop.
# If you buy the ith item, then you will receive a discount equivalent to prices[j]
#  where j is the minimum index such that j > i and prices[j] <= prices[i].
# Otherwise, you will not receive any discount at all.
# Return an integer array answer where answer[i]
#  is the final price you will pay for the ith item of the shop, considering the special discount.
# --------------------
# 1 <= prices.length <= 500
# 1 <= prices[i] <= 1000
from random import randint


def final_prices(prices: list[int]) -> list[int]:
    # working_sol (77.30%, 77.20%) -> (46ms, 16.50mb)  time: O(n) | space: O(n)
    target: int
    value: int
    out: list[int] = [0 for _ in range(len(prices))]
    stack: list[tuple[int, int]] = []
    for index, price in enumerate(prices):
        while stack and stack[-1][1] >= price:
            target, value = stack.pop()
            out[target] = value - price
        stack.append((index, price))
    while stack:
        target, value = stack.pop()
        out[target] = value
    return out


# Time complexity: O(n) <- n - length of the input array `prices`.
# Always creating `out` with the same size as `prices` => O(n).
# Traversing whole `prices` with `enumerate` and loop to add them in a `stack` => O(3 * n).
# In the worst case, none of the values will be discounted, and we will extra traverse every value => O(4 * n).
# --------------------
# Auxiliary space: O(n).
# `out` <- always of the size `prices` => O(n).
# `stack` <- in the worst case will hold every pair from `enumerate(prices)` => O(2 * n).


test: list[int] = [8, 4, 6, 2, 3]
test_out: list[int] = [4, 2, 4, 2, 3]
assert test_out == final_prices(test)

test = [1, 2, 3, 4, 5]
test_out = [1, 2, 3, 4, 5]
assert test_out == final_prices(test)

test = [10, 1, 1, 6]
test_out = [9, 0, 1, 6]
assert test_out == final_prices(test)

test = [randint(1, 1000) for _ in range(500)]
print(test)
