# There are 3n piles of coins of varying size,
#  you and your friends will take piles of coins as follows:
#  - In each step, you will choose any 3 piles of coins (not necessarily consecutive).
#  - Of your choice, Alice will pick the pile with the maximum number of coins.
#  - You will pick the next pile with the maximum number of coins.
#  - Your friend Bob will pick the last pile.
#  - Repeat until there are no more piles of coins.
# Given an array of integers piles where piles[i] is the number of coins in the ith pile.
# Return the maximum number of coins that you can have.
# -----------------
# 3 <= piles.length <= 10 ** 5
# piles.length % 3 == 0
# 1 <= piles[i] <= 10 ** 4
from random import randint


def max_coins(piles: list[int]) -> int:
    # working_sol (91.29%, 51.60%) -> (507ms, 28.7mb)  time: O(n * log n) | space: O(n)
    # Most optimal way, is to leave smallest for Bob and take second to highest.
    # highest => alice , second => us, lowest => bob.
    # ! piles.length % 3 == 0 !
    # We always can take everything.
    # So, bob is always taking 1/3 of all options. -1 for 0-indexed.
    bob_part: int = len(piles) // 3 - 1
    out: int = 0
    piles.sort()
    for x in range(len(piles) - 2, bob_part, -2):
        out += piles[x]
    return out


# Time complexity: O(n * log n) -> builtin sorting => O(n * log n) -> extra traverse of 2/3 of the array => O(2/3 * n).
# n - length of input array 'piles'.
# Auxiliary space: O(n) -> builtin sorting takes 'n' space + 2 extra constant INTs => O(n).


test: list[int] = [2, 4, 1, 2, 7, 8]
test_out: int = 9
assert test_out == max_coins(test)

test = [2, 4, 5]
test_out = 4
assert test_out == max_coins(test)

test = [9, 8, 7, 6, 5, 1, 2, 3, 4]
test_out = 18
assert test_out == max_coins(test)

test = [randint(1, 10 ** 4) for _ in range(99999)]
# print(test)
