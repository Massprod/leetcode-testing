# You are given a 0-indexed integer array candies.
# Each element in the array denotes a pile of candies of size candies[i].
# You can divide each pile into any number of sub piles,
#  but you cannot merge two piles together.
# You are also given an integer k. You should allocate piles of candies to k children
#  such that each child gets the same number of candies.
# Each child can be allocated candies from only one pile of candies
#  and some piles of candies may go unused.
# Return the maximum number of candies each child can get.
# ----------------------------
# 1 <= candies.length <= 10 ** 5
# 1 <= candies[i] <= 10 ** 7
# 1 <= k <= 10 ** 12
from pyperclip import copy

from random import randint


def maximum_candies(candies: list[int], k: int) -> int:
    # working_sol (84.28%, 88.94%) -> (211ms, 29.61mb)
    #                               time: O(log_(sum(candies) // k) * n)
    #                               space: O(1)
    # Binary search with limits from 1 -> min(candies)?
    # Because we're forced to use piles, and we can split them into subPiles.
    # But, we don't want to split the minimum value, because we need:
    # !
    # Return the maximum number of candies each child can get
    # !
    # Nah, we can just leave minimum unused and split highest
    #  into subs with like: [1, 10000] k = 100,
    # We will just split 10000 into 100 for each and we good.
    # So, limits are 1 -> max(candies)?
    # Nah, because we can have less candies then childrens == 0 => 0 -> max(candies).
    def bs_check(value: int, check_array: list[int], childs_target: int) -> bool:
        childs_served: int = 0
        for index in range(len(check_array)):
            cur_value: int = check_array[index]
            childs_served += cur_value // value
            if childs_served >= childs_target:
                return True
            
        return False

    # Or, we can just check total candies and children.
    # Because every child should get at least 1 candy.
    total_candies: int = sum(candies)
    if total_candies < k:
        return 0
    # And now we can start from 1.
    left_l: int = 1
    # And maximum limit is not the max(candies).
    # Because it's only works in the case when we have only 1 child to serve.
    # Otherwise we will use all piles avg.
    right_l: int = total_candies // k + 1  # +1 for odd.
    # Standard BS.
    while left_l < right_l:
        middle: int = ((left_l + right_l) // 2) + 1
        if bs_check(middle, candies, k):
            left_l = middle
        else:
            right_l = middle - 1
    
    return left_l


# Time complexity: O(log_(sum(candies) // k) * n) <- n - length of the input array `candies`.
# BS with limits 1 -> (sum(candies) // k) and in the worst case.
# We're going to traverse whole input array for each check => O(log_(sum(candies) // k) * n).
# ----------------------------
# Auxiliary space: O(1)
# Only constants INTs are used, none of them depends on input => O(1)


test: list[int] = [5, 8, 6]
test_k: int = 3
test_out: int = 5
assert test_out == maximum_candies(test, test_k)

test = [2, 5]
test_k = 11
test_out = 0
assert test_out == maximum_candies(test, test_k)

test = [4, 7, 5]
test_k = 4
test_out = 3
assert test_out == maximum_candies(test, test_k)

test = [randint(1, 10 ** 7) for _ in range(10 ** 5)]
copy(test)
