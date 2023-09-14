# You are visiting a farm that has a single row of fruit trees arranged from left to right.
# The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
# You want to collect as much fruit as possible.
# However, the owner has some strict rules that you must follow:
#   - You only have two baskets, and each basket can only hold a single type of fruit.
#     There is no limit on the amount of fruit each basket can hold.
#   - Starting from any tree of your choice, you must pick exactly one fruit from every tree
#     (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
#   - Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.
# --------------------
# 1 <= fruits.length <= 10 ** 5
# 0 <= fruits[i] < fruits.length
from random import randint


def total_fruit(fruits: list[int]) -> int:
    # working_sol (77.79%, 55.45%) -> (754ms, 22.5mb)  time: O(n) | space: O(n)
    if len(fruits) == 1:
        return 1
    # ! 0 <= fruits[i] < fruits.length !
    # No reasons for a dict.
    gathered: list[int] = [0 for _ in fruits]
    type1: int = -1
    type2: int = -1
    # Standard sliding window.
    l_limit: int = 0
    r_limit: int = 0
    max_fruits: int = 0
    # Expand and count while we can.
    while r_limit != len(fruits):
        if fruits[r_limit] == type1:
            gathered[type1] += 1
        elif fruits[r_limit] == type2:
            gathered[type2] += 1
        elif type1 == -1:
            type1 = fruits[r_limit]
            gathered[type1] += 1
        elif type2 == -1:
            type2 = fruits[r_limit]
            gathered[type2] += 1
        # Shrink when encounter different type3.
        elif fruits[r_limit] != type1 or fruits[r_limit] != type2:
            # We need to reassign type1 or type2 to a new type.
            # Exhaust one of them.
            while gathered[type1] != 0 and gathered[type2] != 0:
                gathered[fruits[l_limit]] -= 1
                l_limit += 1
            # And reassign.
            if gathered[type1] == 0:
                type1 = fruits[r_limit]
                gathered[type1] += 1
            if gathered[type2] == 0:
                type2 = fruits[r_limit]
                gathered[type2] += 1
        # 0-indexed, +1 for correct length.
        max_fruits = max(max_fruits, (r_limit - l_limit) + 1)
        r_limit += 1
    return max_fruits


# Time complexity: O(n) -> worst case == continuous sub until last element, so we will extra delete every index once
# n - len of input_array^^| until n - 2 => O(n + (n - 2)) => O(n).
# Auxiliary space: O(n) -> creating extra array with same size as input_array => O(n).


test: list[int] = [1, 2, 1]
test_out: int = 3
assert test_out == total_fruit(test)

test = [0, 1, 2, 2]
test_out = 3
assert test_out == total_fruit(test)

test = [1, 2, 3, 2, 2]
test_out = 4
assert test_out == total_fruit(test)

test = [randint(0, 10 ** 3 - 1) for _ in range(10 ** 3)]
print(test)
