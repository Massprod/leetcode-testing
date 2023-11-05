# Given an integer array arr of distinct integers and an integer k.
# A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]).
# In each round of the game, we compare arr[0] with arr[1], the larger integer wins
#  and remains at position 0, and the smaller integer moves to the end of the array.
# The game ends when an integer wins k consecutive rounds.
# Return the integer which will win the game.
# It is guaranteed that there will be a winner of the game.
# --------------------------
# 2 <= arr.length <= 10 ** 5
# 1 <= arr[i] <= 10 ** 6
# arr contains distinct integers.
# 1 <= k <= 10 ** 9
from random import randint


def get_winner(arr: list[int], k: int) -> int:
    # working_sol (85.87%, 74.46%) -> (514ms, 29.68mb)  time: O(n) | space: O(1)
    # Only maximum value can eliminate others ! >= len(arr) ! times.
    if k >= len(arr):
        return max(arr)
    # Otherwise we need to eliminate others ! < len(arr)! times.
    # Which is essentially just a left -> right walk with updating of current 'highest'.
    highest: int = arr[0]
    count: int = 0
    for x in range(1, len(arr)):
        if arr[x] > highest:
            highest = arr[x]
            count = 1
        else:
            count += 1
        if count == k:
            break
    return highest


# Time complexity: O(n) -> worst case == (k = len(arr) - 1) or (k >= len(arr)) -> in both cases we will use every index
# n - len of input array 'arr'^^|  of the array once => O(n).
# Auxiliary space: O(1) -> only 2 constant INTs used, none of them depends on input => O(1).
# --------------------------
# Well, first we don't care about k >= len(arr).
# Because only highest value of the array, can eliminate everything else for k >= len(arr) times.
# We will only need to  check (len(arr) - 1) elements.
# Update highest so far, and check for how many eliminations this value did.
# Should be correct.


test: list[int] = [2, 1, 3, 5, 4, 6, 7]
test_k: int = 2
test_out: int = 5
assert test_out == get_winner(test, test_k)

test = [3, 2, 1]
test_k = 10
test_out = 3
assert test_out == get_winner(test, test_k)

# Failed -> I was ignoring last element, thinking that case with k == len(arr).
#           But case with (k == len(arr) is case when we need to cover [0] as well.
#           Otherwise, we will need a value which covers (len(arr) - 1) elements.
test = [1, 25, 35, 42, 68, 70]
test_k = 2
test_out = 70
assert test_out == get_winner(test, test_k)

test = list(set([randint(1, 10 ** 6) for _ in range(10 ** 5)]))
print(test)
print('---------------!')
print(len(test) - 1)
