# There is a bag that consists of items, each item has a number 1, 0, or -1 written on it.
# You are given four non-negative integers numOnes, numZeros, numNegOnes, and k.
# The bag initially contains:
#   numOnes items with 1s written on them.
#   numZeroes items with 0s written on them.
#   numNegOnes items with -1s written on them.
# We want to pick exactly k items among the available items.
# Return the maximum possible sum of numbers written on the items.
# -------------------------
# 0 <= numOnes, numZeros, numNegOnes <= 50
# 0 <= k <= numOnes + numZeros + numNegOnes


def k_items_max_sum(numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
    # working_sol (86.61%, 94.80%) -> (38ms, 16.1mb)  time: O(k) | space: O(1)
    summ: int = 0
    while k and numOnes:
        summ += 1
        numOnes -= 1
        k -= 1
    while k and numZeros:
        numZeros -= 1
        k -= 1
    while k and numNegOnes:
        summ -= 1
        k -= 1
    return summ


# Time complexity: O(k) -> taking from anything while we still didn't picked k items => O(k).
# k - input value^^|
# Auxiliary space: O(1) -> only 1 extra constant INT used => O(1).


test_ones: int = 3
test_zeroes: int = 2
test_neg_ones: int = 0
test_k: int = 2
test_out: int = 2
assert test_out == k_items_max_sum(test_ones, test_zeroes, test_neg_ones, test_k)

test_ones = 3
test_zeroes = 2
test_neg_ones = 0
test_k = 4
test_out = 3
assert test_out == k_items_max_sum(test_ones, test_zeroes, test_neg_ones, test_k)
