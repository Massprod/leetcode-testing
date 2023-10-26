# Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.
# We make a binary tree using these integers, and each number may be used for any number of times.
# Each non-leaf node's value should be equal to the product of the values of its children.
# Return the number of binary trees we can make.
# The answer may be too large so return the answer modulo 10 ** 9 + 7.
# -----------------
# 1 <= arr.length <= 1000
# 2 <= arr[i] <= 10 ** 9
# All the values of arr are unique.
from random import randint


def num_factored_bt(arr: list[int]) -> int:
    # working_sol (83.33%, 68.75%) -> (280ms, 16.48mb)  time: O(n * log n) | space: O(n)
    # All unique roots we can start building from.
    # (root: combinations) , every root is '1' combination by itself.
    roots: dict[int, int] = {root: 1 for root in arr}
    # Essentially we need all combinations of subtrees we can build.
    # So, it's better to start from lower -> higher.
    # Then we will have all combinations with lower values
    #  and reuse them for higher value roots.
    asc_arr: list[int] = sorted(set(arr))
    for x in range(len(asc_arr)):
        root: int = asc_arr[x]
        for y in range(x):
            prod_1: int = asc_arr[y]
            # ! Each non-leaf node's value should be equal
            #   to the product of the values of its children !
            if root % prod_1 == 0:
                prod_2: int = root // prod_1
                if prod_2 in roots:
                    # Increment by all combinations we can have.
                    roots[root] += roots[prod_1] * roots[prod_2]
    return sum(roots.values()) % (10 ** 9 + 7)


# Time complexity: O(n * log n) -> traversing input array 'arr' to get all unique roots => O(n) ->
# n - len of input array 'arr'^^| -> sorting this array in ascending => O(n * log n) ->
#                                 -> traversing from 0 -> len('arr') nested loop for every x (0 -> x) => O(n * log n).
# Auxiliary space: O(n) -> all values are unique, so we're recreating (dictionary + list) with the same size => O(2n).
# -----------------
# We can start building from any value == 'root', so it's insta '1' combination for every value.
# And we need all combinations we can build from them.
# Lower -> Higher, because if we start from Higher we will miss Lower combinations.
# Start from Lowest, try to build from it with 2 products and because every product == leaf is root by itself.
# We can reuse their combinations, comb(prod1) * comb(prod2) == comb(cur_root).
# Should be correct, but slow.


test: list[int] = [2, 4]
test_out: int = 3
assert test_out == num_factored_bt(test)

test = [2, 4, 5, 10]
test_out = 7
assert test_out == num_factored_bt(test)

test = [12, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 55]
test_out = 34
assert test_out == num_factored_bt(test)

test = [15, 13, 22, 7, 11]
test_out = 5
assert test_out == num_factored_bt(test)

test = [randint(2, 10 ** 9) for _ in range(1000)]
print(test)
