# You are given an integer array coins representing coins of different denominations
#   and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.
# ---------------------
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2 ** 31 - 1
# 0 <= amount <= 10 ** 4
from random import randint


def coin_change(coins: list[int], amount: int) -> int:
    # working_sol (90.65%, 10.62%) -> (1115ms, 43.7mb)  time: O(n * m ** n) | space: O(m ** n)
    # Unique case, we don't need coins.
    # We can't build this amount, but we just don't need them == 0.
    if amount == 0:
        return 0
    recur_cache: dict[int, int] = {}

    def take(amount_left: int) -> int | None:
        if amount_left in recur_cache:
            return recur_cache[amount_left]
        # We have taken correct amount, nothing more is needed.
        if amount_left == 0:
            return 0
        # Current minimum coins taken.
        min_taken: int | None = None
        for coin in coins:
            # Taking every coin possible.
            if coin <= amount_left:
                try_take: int = take(amount_left - coin)
                # There's overtake or no correct coin to take after.
                if try_take is None:
                    continue
                # First return, can be changed to +inf, but w.e.
                if min_taken is None:
                    min_taken = 1 + try_take
                # Always taking +1 coin and w.e coins will be after this,
                # we need minimum of it.
                min_taken = min(min_taken, 1 + try_take)
        # Caching.
        recur_cache[amount_left] = min_taken
        return min_taken

    min_coins: int = take(amount)
    # Using None, so if we can't take any correct coin
    # it's always None.
    if min_coins:
        return min_coins
    return -1


# Time complexity: O(n * m ** n) -> in the case amount == 100, coins == [1,1,1,1,1 ..etc.. for len(12)] ->
# m - len of input_coins array^^| -> for every coin option we're going to call recursion until all amount is exhausted
# n - input amount^^|             and because we're caching all calls, after we reach 0, every other will be reused ->
#                                 -> in this case is just loop n and m calls => O(m * n) ->
#                                 -> but for cases with different values it's still, recursion tree with depth of n
#                                 and m options to turn + extra loop inside => O(n * m ** n).
#  ^^Should be correct, but memorization is culling most of the calls and I don't understand how to calc it correctly.
# Auxiliary space: O(m ** n) -> storing every recursion call => O(m ** n).
# ---------------------
# Take every coin one by one and record recursion returns as always.
# Standard recursion with memorization.
# Actually DP problem, but I'm not rebuilding it for bottom -> up for now. Need to learn more.
# At least, im capable of seeing them more correctly and doing top -> bottom with recursion and cache.
# Great dailies' week for DP.


test1 = [1, 2, 5]
test1_amount = 11
test1_out = 3
assert test1_out == coin_change(test1, test1_amount)

test2 = [2]
test2_amount = 3
test2_out = -1
assert test2_out == coin_change(test2, test2_amount)

test3 = [1]
test3_amount = 0
test3_out = 0
assert test3_out == coin_change(test3, test3_amount)

test: list[int] = []
for _ in range(12):
    test.append(randint(1, 2 ** 31 - 1))
test_amount: int = randint(1, 10 ** 4)
print(test)
print(test_amount)
