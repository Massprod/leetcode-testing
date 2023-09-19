# There is a street with n * 2 plots, where there are n plots on each side of the street.
# The plots on each side are numbered from 1 to n. On each plot, a house can be placed.
# Return the number of ways houses can be placed such that no two houses are adjacent
#  to each other on the same side of the street.
# Since the answer may be very large, return it modulo 10 ** 9 + 7.
# Note that if a house is placed on the ith plot on one side of the street,
#  a house can also be placed on the ith plot on the other side of the street.
# ---------------
# 1 <= n <= 10 ** 4


def count_house_placements(n: int) -> int:
    # working_sol (48.84%, 50%) -> (151ms, 21mb)  time: O(n) | space: O(n)
    if n == 1:
        return 4
    if n == 2:
        return 9
    # ! The DP for one side of the street will bear
    #   resemblance to the Fibonacci sequence. !
    fibo: list[int] = [2, 3] + [0 for _ in range(n - 2)]
    for x in range(2, len(fibo)):
        fibo[x] = fibo[x - 2] + fibo[x - 1]
    # ! The number of different arrangements on
    #   both side of the street is the same. !
    # Means, (arrangements * arrangements) == all.
    return (fibo[-1] ** 2) % (10 ** 9 + 7)


# Time complexity: O(n) -> creating and traversing array with size of n => O(n).
# Auxiliary space: O(n) -> extra list with size == n => O(n).
# ---------------
# !
# The DP for one side of the street will bear resemblance to the Fibonacci sequence.
# The number of different arrangements on both side of the street is the same.
# !
# So it's starting with 2 and 3 and fibo after.
# [0] <- place, or not place at all == 2 ways.
# [1] <- place at [0] or place at [1] or not place at all == 3 ways.
# Every other is continuation of this 2 options.


test: int = 1
test_out: int = 4
assert test_out == count_house_placements(test)

test = 2
test_out = 9
assert test_out == count_house_placements(test)

test = 1111
test_out = 716735676
assert test_out == count_house_placements(test)
