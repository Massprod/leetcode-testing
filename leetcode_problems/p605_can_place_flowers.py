# You have a long flowerbed in which some of the plots are planted, and some are not.
# However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
#   and an integer n, return true if n new flowers can be planted in the flowerbed without violating
#   the no-adjacent-flowers rule and false otherwise.
# ---------------------
# 1 <= flowerbed.length <= 2 * 10 ** 4
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length
from random import randint


def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    # working_sol (99.21%, 63.67%) -> (143ms, 16.7mb)  time: O(n) | space: O(1)
    # Nothing to place == all_placed.
    if n == 0:
        return True
    # Unique case with only 1 place.
    # Loop is obvious error.
    if len(flowerbed) == 1:
        if flowerbed[0] != 1:
            n -= 1
        if n == 0:
            return True
        return False
    # Same for [0] and [-1] we can't check left and right of them.
    if flowerbed[0] != 1 and flowerbed[1] != 1:
        n -= 1
        flowerbed[0] = 1
        if n == 0:
            return True
    if flowerbed[-1] != 1 and flowerbed[-2] != 1:
        n -= 1
        flowerbed[-1] = 1
        if n == 0:
            return True
    # Any other indexes can be checked with left, right sides being empty,
    # and obviously spot to plant should be empty as well.
    for x in range(1, len(flowerbed) - 1):
        if n == 0:
            return True
        if flowerbed[x - 1] != 1 and flowerbed[x] != 1 and flowerbed[x + 1] != 1:
            n -= 1
            flowerbed[x] = 1
    if n == 0:
        return True
    return False


# Time complexity: O(n) -> in the worst case, if we're given n which can't be placed -> we're going to traverse
# n - len of input_array^^|  whole input_array, once => O(n).
# Auxiliary space: O(1) -> nothing extra used => O(1).
# ---------------------
# Working for big cases, and tested len == 2, 3. Dunno what's tricky part, let's fail.
# Ok. 124/127. Well at least 50%, not 32. As always rushed Easy task.
# ---------------------
# 31.2% Acceptance_rate. Hmm.
# Should be just [x - 1] and [x] and [x + 1] != 1, then we're planting.
# On the first sight, let's try.


test1 = [1, 0, 0, 0, 1]
test1_n = 1
test1_out = True
assert test1_out == can_place_flowers(test1, test1_n)

test2 = [1, 0, 0, 0, 1]
test2_n = 2
test2_out = False
assert test2_out == can_place_flowers(test2, test2_n)

test3 = [1, 0, 0, 0, 0]
test3_n = 2
test3_out = True
assert test3_out == can_place_flowers(test3, test3_n)

# test4 -> failed -> What a pathetic mistake. I literally fixed this part with n going negative,
#                    but im extra checking edge indexes and can go 0 here, so we need to check before any other index
#                    check inside a loop, and I fixed it for cases when loop was going negative cuz I wasn't breaking
#                    with n == 0. Just extra check after every n decrease.
test4 = [0, 0, 1, 0, 0]
test4_n = 1
test4_out = True
assert test4_out == can_place_flowers(test4, test4_n)

test: list[int] = [0 for _ in range(2 * 10 ** 4)]
for _ in range(0, 2 * 10 ** 4, 9):
    test[_] = 1
test_k: int = randint(0, len(test))
# print(test)
# print(test_k)
