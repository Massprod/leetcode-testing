# It is a sweltering summer day, and a boy wants to buy some ice cream bars.
# At the store, there are n ice cream bars. You are given an array costs of length n,
#  where costs[i] is the price of the ith ice cream bar in coins.
# The boy initially has coins coins to spend,
#  and he wants to buy as many ice cream bars as possible.
# Note: The boy can buy the ice cream bars in any order.
# Return the maximum number of ice cream bars the boy can buy with coins coins.
# You must solve the problem by counting sort.
# --- --- --- ---
# costs.length == n
# 1 <= n <= 10 ** 5
# 1 <= costs[i] <= 10 ** 5
# 1 <= coins <= 10 ** 8


def max_ice_cream(costs: list[int], coins: int) -> int:
    # working_solution: (82.76%, 90.37%) -> (69ms, 28.96mb)  Time: O(n * log n) Space: O(n)
    costs.sort()
    out: int = 0
    for cost in costs:
        if cost > coins:
            break
        out += 1
        coins -= cost
    
    return out


# Time complexity: O(n * log n) <- n - length of the input array `costs`.
# Always sorting and traversing the whole input array `costs` => O(n * log n + n).
# --- --- --- ---
# Auxiliary space: O(n)


test: list[int] = [1, 3, 2, 4, 1]
test_coins: int = 7
test_out: int = 4
assert test_out == max_ice_cream(test, test_coins)

test = [10, 6, 8, 7, 7, 8]
test_coins = 5
test_out = 0
assert test_out == max_ice_cream(test, test_coins)

test = [1, 6, 3, 1, 2, 5]
test_coins = 20
test_out = 6
assert test_out == max_ice_cream(test, test_coins)
