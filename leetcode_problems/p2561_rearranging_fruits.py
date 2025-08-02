# You have two fruit baskets containing n fruits each.
# You are given two 0-indexed integer arrays basket1 and basket2 representing
#  the cost of fruit in each basket. You want to make both baskets equal.
# To do so, you can use the following operation as many times as you want:
#  - Chose two indices i and j, and swap the ith fruit
#    of basket1 with the jth fruit of basket2.
#  - The cost of the swap is min(basket1[i],basket2[j]).
# Two baskets are considered equal if sorting them according
#  to the fruit cost makes them exactly the same baskets.
# Return the minimum cost to make both the baskets equal or -1 if impossible.
# ----------------------
# basket1.length == basket2.length
# 1 <= basket1.length <= 10 ** 5
# 1 <= basket1[i],basket2[i] <= 10 ** 9
from collections import defaultdict

from random import randint

from pyperclip import copy


def min_cost(basket1: list[int], basket2: list[int]) -> int:
    # working_sol (5.19%, 50.65%) -> (149ms, 45.57mb)  time: O(n * log n) | space: O(n)
    # 1 <= basket1[i],basket2[i] <= 10 ** 9
    min_val: int = 10 ** 9
    # { value: occurs }
    basket1_vals: dict[int, int] = defaultdict(int)
    basket2_vals: dict[int, int] = defaultdict(int)
    for val in basket1:
        basket1_vals[val] += 1
        min_val = min(min_val, val)
    for val in basket2:
        basket2_vals[val] += 1
        min_val = min(min_val, val)
    
    # Difference between values in the backet, gives us actual number of 
    #  value we need to move. Because we need to make them equal.
    for val, occurs in basket2_vals.items():
        basket1_vals[val] -= occurs
    
    out: int = 0
    moves_array: list[int] = []
    for value, occurs in basket1_vals.items():
        # We can't disperse `odd`` number of the values.
        if occurs % 2:
            return - 1
        # We need to move half to make it equal.
        to_move: int = abs(occurs) // 2
        moves_array.extend([value for _ in range(to_move)])
    # Sorting to always use the minimum possible option.
    moves_array.sort()
    # And the cost to move is either swap with a minimum value.
    # Or, we just move it with swapping to w.e higher/equal value 
    #  we still need to swap == higher_index.
    for index in range(len(moves_array) // 2):
        out += min(2 * min_val, moves_array[index])

    return out


# Time complexity: O(n * log n) <- n - length of the input arrays `basket1` | `basket2`.
# In the worst case there's only unique values in both baskets.
# Traversing both input array to get all the occurrences => O(2 * n).
# Extra traversing `basket2` to get all the occurrences we need to move => O(3 * n).
# Traversing every unique key from the `basket1` and `basket2` => O(4 *n).
# Sorting the array to get the correct sequence to use values => O(n * log n + 4 * n).
# ----------------------
# Auxiliary space: O(n)
# `basket1_vals` <- allocates space for each unique value from `basket1` => O(n).
# `basket2_vals` <- allocates space for each unique value from `basket2` => O(2 n).
# `moves_array`  <- allocates space for each value from `basket1` | `basket2` => O(3 * n).


test_basket1: list[int] = [4, 2, 2, 2]
test_basket2: list[int] = [1, 4, 1, 2]
test_out: int = 1
assert test_out == min_cost(test_basket1, test_basket2)

test_basket1 = [2, 3, 4, 1]
test_basket2 = [3, 2, 5, 1]
test_out = -1
assert test_out == min_cost(test_basket1, test_basket2)

test_basket1 = [randint(1, 10 ** 9) for _ in range(10 ** 5)]
copy(test_basket1)  # type: ignore
