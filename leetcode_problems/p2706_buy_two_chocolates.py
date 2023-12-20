# You are given an integer array prices representing the prices of various chocolates in a store.
# You are also given a single integer money, which represents your initial amount of money.
# You must buy exactly two chocolates in such a way that you still have some non-negative leftover money.
# You would like to minimize the sum of the prices of the two chocolates you buy.
# Return the amount of money you will have leftover after buying the two chocolates.
# If there is no way for you to buy two chocolates without ending up in debt, return money.
# Note that the leftover must be non-negative.
# ------------------
# 2 <= prices.length <= 50
# 1 <= prices[i] <= 100
# 1 <= money <= 100
from random import randint


def buy_choco(prices: list[int], money: int) -> int:
    # working_sol (95.62%, 23.41%) -> (55ms, 17.2mb)  time: O(n) | space: O(1)
    # ! You would like to minimize the sum of the prices of the two chocolates you buy. !
    # So, just take 2 minimum values if we can afford it.
    lowest: int = 100
    second_lowest: int = 100
    for price in prices:
        if price <= lowest:
            lowest, second_lowest = price, lowest
        elif price < second_lowest:
            second_lowest = price
    out: int = money - lowest - second_lowest
    if out >= 0:
        return out
    return money


# Time complexity: O(n) <- n - length of input array `prices`.
# Full traverse to get 2 lowest values.
# Auxiliary space: O(1).
# Only 3 extra constant INTs used, none of them depends on input.


test: list[int] = [1, 2, 2]
test_money: int = 3
test_out: int = 0
assert test_out == buy_choco(test, test_money)

test = [3, 2, 3]
test_money = 3
test_out = 3
assert test_out == buy_choco(test, test_money)

test = [randint(1, 100) for _ in range(50)]
print(test)
