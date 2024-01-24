# You have n coins and you want to build a staircase with these coins.
# The staircase consists of k rows where the ith row has exactly i coins.
# The last row of the staircase may be incomplete.
# Given the integer n, return the number of complete rows of the staircase you will build.
# ---------------------
# 1 <= n <= 2 ** 31 - 1


def arrange_coins(n: int) -> int:
    # working_sol (97.77%, 56.06%) -> (30ms, 16.54mb)  time: O(log n) | space: O(1)
    # ! 1 + 2 + 3 + .... + n = n * (n + 1) / 2 ! <- # of steps.
    # In our case # of coins used on all rows to fully fill.
    left: int = 1
    right: int = n
    while left < right:
        middle: int = (left + right) // 2 + 1
        # If we have enough coins or more.
        if middle * (middle + 1) // 2 <= n:
            left = middle
        else:
            right = middle - 1
    return left


# Time complexity: O(log n).
# Standard BS from 1 -> `n` => O(log n).
# ---------------------
# Auxiliary space: O(1)


test: int = 5
test_out: int = 2
assert test_out == arrange_coins(test)

test = 8
test_out = 3
assert test_out == arrange_coins(test)

test = 2 ** 31 - 1
test_out = 65535
assert test_out == arrange_coins(test)
