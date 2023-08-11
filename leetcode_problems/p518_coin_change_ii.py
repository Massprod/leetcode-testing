# You are given an integer array coins representing coins of different denominations
#   and an integer amount representing a total amount of money.
# Return the number of combinations that make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return 0.
# You may assume that you have an infinite number of each kind of coin.
# The answer is guaranteed to fit into a signed 32-bit integer.
# -------------------------
# 1 <= coins.length <= 300
# 1 <= coins[i] <= 5000
# All the values of coins are unique.
# 0 <= amount <= 5000
from random import randint


def change(amount: int, coins: list[int]) -> int:
    # working_sol (33.73%, 15.42%) -> (544ms, 165mb)  time: O(2 ** m ) | space: O(2 ** m)
    # Don't know why this is 1.
    # Guess, it's logic -> we can take 0 coins only in 1 way,
    # never take any == 1 way.
    if amount == 0:
        return 1
    recur_cache: dict[tuple[int, int], int] = {}

    def take(amount_left: int, coin_index: int) -> int:
        # Correct way, leading to exhausted coin_purse.
        if amount_left == 0:
            return 1
        # We're using coin_index to take coins from purse,
        # so we bounded by its size.
        if coin_index == len(coins):
            return 0
        # Reuse stored.
        if (amount_left, coin_index) in recur_cache:
            return recur_cache[amount_left, coin_index]
        # Correct ways to take everything ->
        correct_ways: int = 0
        # -> if we can use current coin on coin_index ->
        if coins[coin_index] <= amount_left:
            # -> we can take this coin_value from current amount, and try to reuse this coin ->
            correct_ways += take(amount_left - coins[coin_index], coin_index)
        # -> otherwise, try another coin. Starting from 0, so it's +1 until we reach end.
        correct_ways += take(amount_left, coin_index + 1)
        # Cache.
        recur_cache[amount_left, coin_index] = correct_ways
        return correct_ways

    return take(amount, 0)


# Time complexity: O(2 ** m) -> in case like [1, 2, 3, 4, 5, 6, 7] with amount == 100, we're going to call
# m - input amount^^|       recursion for [0] index, like 100 times and after that another it's the deepest level ->
#                           -> every other value is either lower calls, or reusing stored -> so it should be
#                           standard recursion tree with depth of m and 2 options => O(2 ** m).
#                           Caching is culling some calls, but I don't know how to calc this correctly.
# Auxiliary space: O(2 ** m) -> every unique call is stored => O(2 ** m).
# -------------------------
# Same as p322 but with counting correct ways, not minimum path?
# Ok. Instead of a loop I can use indexes of coins to correctly store recursion calls to reuse.


test: list[int] = [1, 2, 5]
test_amount: int = 5
test_out: int = 4
assert test_out == change(test_amount, test)

test = [2]
test_amount = 3
test_out = 0
assert test_out == change(test_amount, test)

test = [10]
test_amount = 10
test_out = 1
assert test_out == change(test_amount, test)

test = [
    434, 2779, 3557, 4967, 1975, 1448, 142, 4208, 1865,
    3155, 3321, 1532, 1087, 2320, 3699, 1072, 1837, 337, 4732, 4771
]
test_amount = 3824
test_out = 1
assert test_out == change(test_amount, test)

test = []
test_used: set[int] = set()
for _ in range(300):
    value: int = randint(1, 5000)
    if value not in test_used:
        test.append(value)
        test_used.add(value)
test_amount = randint(0, 5000)
# print(test)
# print(test_amount)
