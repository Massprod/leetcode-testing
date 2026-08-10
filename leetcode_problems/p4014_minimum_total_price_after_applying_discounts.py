# You are given two integer arrays prices and discounts.
# The value prices[i] represents the price of the ith item,
#  and discounts[j] represents a discount percentage.
# You may apply discounts subject to the following rules:
#  - Each discount can be applied to at most one item.
#  - Each item can receive at most one discount.
#  - An item may also receive no discount.
# If a discount of d percent is applied to an item with price p,
#  its final price becomes (p * (100 - d)) / 100. The final price is not rounded.
# Return the minimum possible sum of final prices after assigning discounts optimally.
# Answers within 10 ** -5 of the actual answer will be accepted.
# --- --- --- ---
# 1 <= prices.length, discounts.length <= 10 ** 5
# 1 <= prices[i] <= 10 ** 5
# 1 <= discounts[j] <= 100


def min_price(prices: list[int], discounts: list[int]) -> float:
    # working_solution: (100%, 0%) -> (163ms, 37.68mb)  Time: O(n * log n + g * log n) Space: O(n + g)
    # best_approach: highest discount to the highest price
    # But, double sorting is slow.
    out: float = 0.0
    sort_prices: list[int] = sorted(prices)
    sort_discounts: list[int] = sorted(discounts, reverse=True)
    for discount in sort_discounts:
        if not sort_prices:
            break
        out += (sort_prices.pop() * (100 - discount)) / 100
    out += sum(sort_prices)
    
    return out


# Time complexity: O(n * log n + g * log n)
# n - length of the input array `prices`
# g - length of the input array `discounts`
# --- --- --- ---
# Space complexity: O(n + g)


test: list[int] = [10, 30, 21]
test_disc: list[int] = [50, 60]
test_out: float = 32.5
assert test_out == min_price(test, test_disc)

test = [100, 70]
test_disc = [10, 40, 50]
test_out = 92.0
assert test_out == min_price(test, test_disc)

test = [7, 3, 9]
test_disc = [100, 100]
test_out = 3.0
assert test_out == min_price(test, test_disc)
